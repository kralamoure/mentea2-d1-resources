import asyncio
import glob
import io
import json
import math
import os
import time
import urllib.parse

LOGIN_PROXY_PORT = 446
GAME_PROXY_PORT = 447
JSON_FOLDER = "json"
DATA_FILE = "proxy.json"

CONFIGS = (
    {
        "login_address": ("127.0.0.1", 443),
        "keep_data": False
    },
    {
        "login_address": ("co-retro.ankama-games.com", 443),
        "keep_data": True
    },
    {
        "login_address": ("retro-co-staging.ankama-games.com", 443),
        "keep_data": True
    }
)

def get_reader(io):
    return io[0]

def get_writer(io):
    return io[1]

def set_state(io, state):
    io[2] = state

def get_state(io):
    return io[2]

def get_host(address):
    return address[0]

def get_port(address):
    return address[1]

class ProxyClient:
    def __init__(self, local_io, remote_io, server):
        self.local_io = local_io
        self.remote_io = remote_io
        self.server = server

    async def read_local(self):
        while True:
            try:
                data = await get_reader(self.local_io).readuntil(self.server.local_separator.encode())
            except asyncio.IncompleteReadError:
                if self.server.local_disconnection != None:
                    self.server.local_disconnection(self.local_io)
                await self.close_remote()
                return
            message = data.decode()[:-len(self.server.local_separator)]
            await self.server.handle_local_message(message, self)

    async def read_remote(self):
        while True:
            try:
                data = await get_reader(self.remote_io).readuntil(self.server.remote_separator.encode())
            except asyncio.IncompleteReadError:
                if self.server.remote_disconnection != None:
                    self.server.remote_disconnection(self.local_io, self.remote_io)
                await self.close_local()
                return
            message = data.decode()[:-len(self.server.remote_separator)]
            await self.server.handle_remote_message(message, self)

    async def write_local(self, message):
        data = (message + self.server.remote_separator).encode()
        get_writer(self.local_io).write(data)
        await get_writer(self.local_io).drain()

    async def write_remote(self, message):
        data = (message + self.server.local_separator).encode()
        get_writer(self.remote_io).write(data)
        await get_writer(self.remote_io).drain()

    async def close_local(self):
        get_writer(self.local_io).close()
        await get_writer(self.local_io).wait_closed()
        if self in self.server.clients:
            self.server.clients.remove(self)

    async def close_remote(self):
        get_writer(self.remote_io).close()
        await get_writer(self.remote_io).wait_closed()

class ProxyServer:
    def __init__(self, local_address, get_remote_address, local_separator, remote_separator, handle_local_message, handle_remote_message):
        self.local_address = local_address
        self.get_remote_address = get_remote_address
        self.local_separator = local_separator
        self.remote_separator = remote_separator
        self.handle_local_message = handle_local_message
        self.handle_remote_message = handle_remote_message
        self.clients = []

    def set_callbacks(self, local_connection, remote_connection, local_disconnection, remote_disconnection):
        self.local_connection = local_connection
        self.remote_connection = remote_connection
        self.local_disconnection = local_disconnection
        self.remote_disconnection = remote_disconnection

    async def client_connected(self, local_reader, local_writer):
        local_io = [local_reader, local_writer, None]
        if self.local_connection != None:
            self.local_connection(local_io)
        remote_address = await self.get_remote_address(local_io, self)
        if remote_address == None:
            get_writer(local_io).close()
            await get_writer(local_io).wait_closed()
            return
        remote_reader, remote_writer = await asyncio.open_connection(get_host(remote_address), get_port(remote_address))
        remote_io = [remote_reader, remote_writer, None]
        if self.remote_connection != None:
            self.remote_connection(local_io, remote_io)
        client = ProxyClient(local_io, remote_io, self)
        self.clients.append(client)
        loop = asyncio.get_event_loop()
        loop.create_task(client.read_local())
        loop.create_task(client.read_remote())

    async def start(self):
        self.server = await asyncio.start_server(self.client_connected, get_host(self.local_address), get_port(self.local_address))
    
    async def serve(self):
        async with self.server:
            await self.server.serve_forever()

def format_address(address):
    return get_host(address) + ":" + str(get_port(address))

def format_message(message):
    return message.replace("\n", "\\n")

def split_message_recursion(part, separators):
    if len(separators) == 0:
        return part
    if separators[0] not in part:
        return split_message_recursion(part, separators[1:])
    sub_parts = part.split(separators[0])
    for i in range(0, len(sub_parts)):
        sub_parts[i] = split_message_recursion(sub_parts[i], separators[1:])
    return sub_parts

def split_message(message, start):
    separators = ("|", ";", ",", "^")
    return split_message_recursion(message[start:], separators)

def split_address(address):
    if ":" in address:
        parts = address.split(":")
        return (parts[0], parts[1])
    return (address, 443)

class MessageRegistry():
    def __init__(self):
        self.registry = {}

    def register(self, header, handler):
        self.registry[header] = handler

    async def handle(self, message, client):
        for header in sorted(self.registry, key=len, reverse=True):
            if message.startswith(header):
                await self.registry[header](message, client)
                return

class Proxy:
    def __init__(self):
        self.local_registry = MessageRegistry()
        self.remote_registry = MessageRegistry()

    def get_name(self):
        raise NotImplementedError

    def log(self, text, io=None):
        header = "[" + self.get_name() + "] "
        if io is not None:
            header += "[" + format_address(get_writer(io).get_extra_info("peername")) + "] "
        print(header + text)

    async def write_local_message(self, message, client, custom=False):
        arrow = "<~~" if custom else "<--"
        self.log(arrow + " " + format_message(message), client.local_io)
        await client.write_local(message)

    async def write_remote_message(self, message, client, custom=False):
        arrow = "~~>" if custom else "-->"
        self.log(arrow + " " + format_message(message), client.local_io)
        await client.write_remote(message)

    def local_connection(self, local_io):
        self.log("Connected to proxy", local_io)

    def remote_connection(self, local_io, remote_io):
        self.log("Connected to server", local_io)

    def local_disconnection(self, local_io):
        self.log("Disconnected from proxy", local_io)

    def remote_disconnection(self, local_io, remote_io):
        self.log("Disconnected from server", local_io)

    def get_local_address(self):
        raise NotImplementedError

    async def get_remote_address(self, local_io, server):
        raise NotImplementedError

    async def handle_local_message(self, message, client):
        await self.local_registry.handle(message, client)

    async def handle_remote_message(self, message, client):
        await self.remote_registry.handle(message, client)

    async def start(self):
        server = ProxyServer(self.get_local_address(), self.get_remote_address, "\n\0", "\0", self.handle_local_message, self.handle_remote_message)
        server.set_callbacks(self.local_connection, self.remote_connection, self.local_disconnection, self.remote_disconnection)
        await server.start()
        self.log("Proxy started")
        await server.serve()

DEFAULT_STATE = {
    "map_change": False,
    "mark_maps": False,
    "mark_maps_dist": 2
}

def decode_64(encoded_value):
    array = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    value = array.index(encoded_value)
    return value

def decode_ip(encoded_ip):
    parts = []
    for i in range(0, 8, 2):
        e0 = ord(encoded_ip[i]) - 48
        e1 = ord(encoded_ip[i + 1]) - 48
        part = (e0 << 4) & ((1 << 7) | (1 << 6) | (1 << 5) | (1 << 4))
        part |= e1 & ((1 << 3) | (1 << 2) | (1 << 1) | 1)
        parts.append(part)
    ip = ".".join(list(map(str, parts)))
    return ip

def decode_port(encoded_port):
    e0 = decode_64(encoded_port[0])
    e1 = decode_64(encoded_port[1])
    e2 = decode_64(encoded_port[2])
    port = ((e0 << 12) & ((1 << 17) | (1 << 16) | (1 << 15) | (1 << 14) | (1 << 13) | (1 << 12)))
    port |= ((e1 << 6) & ((1 << 11) | (1 << 10) | (1 << 9) | (1 << 8) | (1 << 7) | (1 << 6)))
    port |= (e2 & ((1 << 5) | (1 << 4) | (1 << 3) | (1 << 2) | (1 << 1) | 1))
    return port

def encode_64(value):
    array = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    encoded_value = array[value]
    return encoded_value

def encode_ip(ip):
    parts = list(map(int, ip.split(".")))
    encodedIp = ""
    for i in range(0, 4):
        e0 = (parts[i] & ((1 << 7) | (1 << 6) | (1 << 5) | (1 << 4))) >> 4
        e1 = parts[i] & ((1 << 3) | (1 << 2) | (1 << 1) | 1)
        encodedIp += chr(e0 + 48) + chr(e1 + 48)
    return encodedIp

def encode_port(port):
    e0 = (port & ((1 << 17) | (1 << 16) | (1 << 15) | (1 << 14) | (1 << 13) | (1 << 12))) >> 12
    e1 = (port & ((1 << 11) | (1 << 10) | (1 << 9) | (1 << 8) | (1 << 7) | (1 << 6))) >> 6
    e2 = port & ((1 << 5) | (1 << 4) | (1 << 3) | (1 << 2) | (1 << 1) | 1)
    encoded_port = encode_64(e0) + encode_64(e1) + encode_64(e2)
    return encoded_port

class LoginProxy(Proxy):
    def __init__(self):
        super().__init__()
        self.local_registry.register("", self.default_local_message)
        self.remote_registry.register("AX", self.AX_remote_message)
        self.remote_registry.register("AY", self.AY_remote_message)
        self.remote_registry.register("Al", self.Al_remote_message)
        self.remote_registry.register("", self.default_remote_message)

    def get_name(self):
        return "LOGIN"

    def get_local_address(self):
        return ("127.0.0.1", LOGIN_PROXY_PORT)

    async def get_remote_address(self, local_io, server):
        message = "HC"
        data = (message + server.remote_separator).encode()
        get_writer(local_io).write(data)
        await get_writer(local_io).drain()
        for i in range(0, 3):
            try:
                data = await get_reader(local_io).readuntil(server.local_separator.encode())
            except asyncio.IncompleteReadError:
                if server.local_disconnection != None:
                    server.local_disconnection(local_io)
                return None
            if i == 1:
                message = data.decode()[:-len(server.local_separator)]
        if "\n" in message:
            split = message.split("\n")
            username = split[0]
            config = 0
            if "@" in username:
                split = username.split("@")
                config = int(split[1])
            set_state(local_io, DEFAULT_STATE)
            get_state(local_io)["config"] = config
            return CONFIGS[config]["login_address"]
        return None

    async def default_local_message(self, message, client):
        if "\n" in message:
            split = message.split("\n")
            username = split[0]
            password = split[1]
            if "@" in username:
                split = username.split("@")
                username = split[0]
                custom_message = username + "\n" + password
                await self.write_remote_message(custom_message, client, True)
                return
        await self.write_remote_message(message, client)

    async def AX_remote_message(self, message, client):
        success = message[2] == "K"
        if not success:
            await self.write_local_message(message, client)
            return
        ip = decode_ip(message[3:11])
        port = decode_port(message[11:14])
        ticket = message[14:]
        get_state(client.local_io)["game_address"] = (ip, port)
        tickets[ticket] = get_state(client.local_io)
        custom_message = "AXK" + encode_ip(get_host(game_proxy.get_local_address())) + encode_port(get_port(game_proxy.get_local_address())) + ticket
        await self.write_local_message(custom_message, client, True)

    async def AY_remote_message(self, message, client):
        success = message[2] == "K"
        if not success:
            await self.write_local_message(message, client)
            return
        split = split_message(message, 3)
        address = split_address(split[0])
        ticket = split[1]
        get_state(client.local_io)["game_address"] = address
        tickets[ticket] = get_state(client.local_io)
        custom_message = "AYK" + format_address(game_proxy.get_local_address()) + ";" + ticket
        await self.write_local_message(custom_message, client, True)

    async def Al_remote_message(self, message, client):
        success = message[2] == "K"
        if not success:
            await self.write_local_message(message, client)
            return
        is_admin = message[3] == "1"
        get_state(client.local_io)["is_admin"] = is_admin
        custom_message = "AlK1"
        await self.write_local_message(custom_message, client, True)

    async def default_remote_message(self, message, client):
        await self.write_local_message(message, client)

def get_map_full_id(map_id, map_date):
    return map_id + "_" + map_date

def get_map_id(map_full_id):
    return map_full_id.split("_")[0]

def get_map_ids():
    map_ids = []
    for map_full_id in data["maps"]:
        map_id = get_map_id(map_full_id)
        map_ids.append(map_id)
    return map_ids

def decode_path_last_cell(encoded_path):
    e1 = decode_64(encoded_path[-2])
    e2 = decode_64(encoded_path[-1])
    cell_id = ((e1 << 6) & ((1 << 9) | (1 << 8) | (1 << 7) | (1 << 6))) | e2
    return cell_id

def decrypt_map(encrypted_map, key):
    prepared_key = ""
    for i in range(0, len(key), 2):
        prepared_key += chr(int(key[i:i+2], 16))
    prepared_key = urllib.parse.unquote(prepared_key)
    checksum = 0
    for i in range(0, len(prepared_key)):
        checksum += ord(prepared_key[i])
    checksum %= 16
    checksum *= 2
    decrypted_map = ""
    for i in range(0, len(encrypted_map), 2):
        decrypted_map += chr(int(encrypted_map[i:i+2], 16) ^ ord(prepared_key[(int(i / 2) + checksum) % len(prepared_key)]))
    return urllib.parse.unquote(decrypted_map)

def decode_cell(encoded_cell):
    e = []
    for i in range(0, len(encoded_cell)):
        e.append(decode_64(encoded_cell[i]))
    cell = {}
    cell["isActive"] = (e[0] & (1 << 5)) >> 5
    if cell["isActive"]:
        cell["layerGroundId"] = ((e[0] << 6) & ((1 << 10) | (1 << 9))) | ((e[2] << 6) & ((1 << 8) | (1 << 7) | (1 << 6))) | e[3]
        cell["layerObject1Id"] = ((e[4] << 12) & (1 << 12)) | ((e[0] << 11) & (1 << 13)) | (e[5] << 6) | e[6]
        cell["layerObject2Id"] = ((e[0] << 12) & (1 << 13)) | ((e[7] << 12) & (1 << 12)) | (e[8] << 6) | e[9]
        cell["hasLineOfSight"] = e[0] & 1
        cell["layerGroundRotation"] = (e[1] >> 4) & ((1 << 1) | 1)
        cell["groundLevel"] = e[1] & ((1 << 3) | (1 << 2) | (1 << 1) | 1)
        cell["movement"] = (e[2] >> 3) & ((1 << 2) | (1 << 1) | 1)
        cell["groundSlope"] = (e[4] >> 2) & ((1 << 3) | (1 << 2) | (1 << 1) | 1)
        cell["isLayerGroundFlipped"] = (e[4] >> 1) & 1
        cell["layerObject1Rotation"] = (e[7] >> 4) & ((1 << 1) | 1)
        cell["isLayerObject1Flipped"] = (e[7] >> 3) & 1
        cell["isLayerObject2Flipped"] = (e[7] >> 2) & 1
        cell["isLayerObject2Interactive"] = (e[7] >> 1) & 1
    return cell

def decode_map(encoded_map):
    cells = []
    cell_id = 0
    for i in range(0, len(encoded_map), 10):
        cell = decode_cell(encoded_map[i:i+10])
        cell["id"] = cell_id
        cells.append(cell)
        cell_id += 1
    return cells

async def mark_triggers(client):
    map_full_id = get_state(client.local_io)["map_full_id"]
    map_id = get_map_id(map_full_id)
    if map_id not in maps:
        return
    if "data" not in maps[map_id]:
        return
    map_key = data["maps"][map_full_id]["key"]
    map_triggers = list(map(int, data["maps"][map_full_id]["triggers"]))
    map_data = maps[map_id]["data"]["mapData"]
    decrypted_map = decrypt_map(map_data, map_key)
    cells = decode_map(decrypted_map)
    trigger_object_ids = (1029, 1030, 4088)
    trigger_cell_ids = []
    for cell in cells:
        if not cell["isActive"]:
            continue
        if (cell["layerObject1Id"] in trigger_object_ids) or (cell["layerObject2Id"] in trigger_object_ids):
            trigger_cell_ids.append(cell["id"])
    character_id = get_state(client.local_io)["character_id"]
    for trigger_cell_id in trigger_cell_ids:
        if trigger_cell_id in map_triggers:
            continue
        custom_message = "Gf" + str(character_id) + "|" + str(trigger_cell_id)
        await game_proxy.write_local_message(custom_message, client, True)

async def mark_maps(client):
    mark_maps_dist = get_state(client.local_io)["mark_maps_dist"]
    curr_map_full_id = get_state(client.local_io)["map_full_id"]
    curr_map_id = get_map_id(curr_map_full_id)
    curr_map_x = maps[curr_map_id]["x"]
    curr_map_y = maps[curr_map_id]["y"]
    map_coords = []
    for map_id in maps:
        if map_id in get_map_ids():
            continue
        map_x = maps[map_id]["x"]
        map_y = maps[map_id]["y"]
        dist = math.sqrt((curr_map_x - map_x) ** 2 + (curr_map_y - map_y) ** 2)
        if dist > mark_maps_dist:
            continue
        map_coords.append((map_x, map_y))
    map_coords = list(dict.fromkeys(map_coords))
    custom_message = "IH" + "|".join(map(lambda map_coord: str(map_coord[0]) + ";" + str(map_coord[1]) + ";;3", map_coords))
    await game_proxy.write_local_message(custom_message, client, True)
    await mark_triggers(client)

class GameProxy(Proxy):
    def __init__(self):
        super().__init__()
        self.local_registry.register("BA", self.BA_local_message)
        self.local_registry.register("BM", self.BM_local_message)
        self.local_registry.register("BaM", self.BaM_local_message)
        self.local_registry.register("", self.default_local_message)
        self.remote_registry.register("AS", self.AS_remote_message)
        self.remote_registry.register("GA", self.GA_remote_message)
        self.remote_registry.register("GDK", self.GDK_remote_message)
        self.remote_registry.register("GDM", self.GDM_remote_message)
        self.remote_registry.register("GM", self.GM_remote_message)
        self.remote_registry.register("", self.default_remote_message)

    def get_name(self):
        return "GAME"

    def get_local_address(self):
        return ("127.0.0.1", GAME_PROXY_PORT)

    async def get_remote_address(self, local_io, server):
        message = "HG"
        data = (message + server.remote_separator).encode()
        get_writer(local_io).write(data)
        await get_writer(local_io).drain()
        try:
            data = await get_reader(local_io).readuntil(server.local_separator.encode())
        except asyncio.IncompleteReadError:
            if server.local_disconnection != None:
                server.local_disconnection(local_io)
            return None
        message = data.decode()[:-len(server.local_separator)]
        if message.startswith("AT"):
            ticket = message[2:]
            if ticket in tickets:
                set_state(local_io, tickets[ticket])
                return get_state(local_io)["game_address"]
        return None

    async def BA_local_message(self, message, client):
        command = message[2:]
        split = command.split(" ")
        if split[0] == "mark" and split[1] == "maps":
            if len(split) == 2:
                get_state(client.local_io)["mark_maps"] = not get_state(client.local_io)["mark_maps"]
                if get_state(client.local_io)["mark_maps"]:
                    await mark_maps(client)
                else:
                    await self.write_local_message("IH", client, True)
            elif len(split) == 3:
                get_state(client.local_io)["mark_maps_dist"] = int(split[2])
                if get_state(client.local_io)["mark_maps"]:
                    await mark_maps(client)
            return
        if not get_state(client.local_io)["is_admin"]:
            await self.write_local_message("BN", client, True)
            return
        await self.default_local_message(message, client)

    async def BM_local_message(self, message, client):
        split = split_message(message, 2)
        channel = split[0]
        if channel == "@" and not get_state(client.local_io)["is_admin"]:
            await self.write_local_message("BN", client, True)
            return
        await self.default_local_message(message, client)

    async def BaM_local_message(self, message, client):
        if not get_state(client.local_io)["is_admin"]:
            await self.write_local_message("BN", client, True)
            return
        await self.default_local_message(message, client)

    async def default_local_message(self, message, client):
        await self.write_remote_message(message, client)

    async def AS_remote_message(self, message, client):
        await self.default_remote_message(message, client)
        success = message[2] == "K"
        if not success:
            return
        split = split_message(message, 4)
        character_id = split[0]
        get_state(client.local_io)["character_id"] = int(character_id)

    async def GA_remote_message(self, message, client):
        await self.default_remote_message(message, client)
        if message.startswith("GAF") or message.startswith("GAS"):
            return
        character_id = get_state(client.local_io)["character_id"]
        split = split_message(message, 2)
        action_type = int(split[1])
        if action_type != 0:
            entity_id = int(split[2])
            if action_type == 1 and entity_id == character_id:
                encoded_path = split[3]
                cell_id = decode_path_last_cell(encoded_path)
                if "cell_id" in get_state(client.local_io):
                    get_state(client.local_io)["prev_cell_id"] = get_state(client.local_io)["cell_id"]
                get_state(client.local_io)["cell_id"] = cell_id

    async def GDK_remote_message(self, message, client):
        await self.default_remote_message(message, client)
        config = get_state(client.local_io)["config"]
        keep_data = CONFIGS[config]["keep_data"]
        if keep_data:
            write_data()
        if get_state(client.local_io)["mark_maps"]:
            await mark_maps(client)

    async def GDM_remote_message(self, message, client):
        await self.default_remote_message(message, client)
        config = get_state(client.local_io)["config"]
        keep_data = CONFIGS[config]["keep_data"]
        split = split_message(message, 4)
        map_id = split[0]
        map_date = split[1]
        map_key = split[2]
        full_id = get_map_full_id(map_id, map_date)
        get_state(client.local_io)["map_change"] = True
        if "map_full_id" in get_state(client.local_io):
            get_state(client.local_io)["prev_map_full_id"] = get_state(client.local_io)["map_full_id"]
        get_state(client.local_io)["map_full_id"] = full_id
        if full_id not in data["maps"]:
            if keep_data:
                data["maps"][full_id] = {
                    "key": map_key,
                    "triggers": {},
                    "monsterGroups": [],
                    "npcs": []
                }

    async def GM_remote_message(self, message, client):
        await self.default_remote_message(message, client)
        config = get_state(client.local_io)["config"]
        keep_data = CONFIGS[config]["keep_data"]
        map_full_id = get_state(client.local_io)["map_full_id"]
        split = split_message(message, 2)
        for entity in split:
            if len(entity) == 0:
                continue
            if not entity[0].startswith("+"):
                continue
            entity[0] = entity[0][1:]
            character_id = get_state(client.local_io)["character_id"]
            if entity[3] == str(character_id):
                cell_id = int(entity[0])
                if "cell_id" in get_state(client.local_io):
                    get_state(client.local_io)["prev_cell_id"] = get_state(client.local_io)["cell_id"]
                get_state(client.local_io)["cell_id"] = cell_id
                if get_state(client.local_io)["map_change"]:
                    get_state(client.local_io)["map_change"] = False
                    if "prev_map_full_id" in get_state(client.local_io):
                        prev_map_full_id = get_state(client.local_io)["prev_map_full_id"]
                        prev_cell_id = get_state(client.local_io)["prev_cell_id"]
                        map_id = int(get_map_id(get_state(client.local_io)["map_full_id"]))
                        if keep_data:
                            data["maps"][prev_map_full_id]["triggers"][prev_cell_id] = (map_id, cell_id)
                continue
            if not isinstance(entity[5], str):
                continue
            entity_type = int(entity[5])
            if entity_type == -3:
                if keep_data:
                    data["maps"][map_full_id]["monsterGroups"].append(entity)
            elif entity_type == -4:
                if keep_data:
                    data["maps"][map_full_id]["npcs"].append(entity)

    async def default_remote_message(self, message, client):
        await self.write_local_message(message, client)

def read_data():
    global data

    if os.path.isfile(DATA_FILE):
        with io.open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.loads(f.read())
    else:
        data = {
            "maps": {}
        }

def write_data():
    with io.open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False))

MAP_FILE = os.path.join(JSON_FOLDER, "lang", "swf", "maps_*_*.json")
MAP_FOLDER = os.path.join(JSON_FOLDER, "maps")

def read_maps():
    global maps

    file_paths = glob.glob(MAP_FILE)
    if len(file_paths) > 0:
        file_path = file_paths[0]
        with io.open(file_path, "r", encoding="utf-8") as f:
            maps = json.loads(f.read())["MA"]["m"]
        if os.path.isdir(MAP_FOLDER):
            for filename in os.listdir(MAP_FOLDER):
                if not filename.endswith(".json"):
                    continue
                split = os.path.splitext(filename)[0].split("_")
                map_id = split[0]
                map_date = split[1][:-1]
                if map_id in maps:
                    maps[map_id]["date"] = map_date
                    file_path = os.path.join(MAP_FOLDER, filename)
                    with io.open(file_path, "r", encoding="utf-8") as f:
                        file_data = json.loads(f.read())
                        maps[map_id]["data"] = file_data
    else:
        maps = {}

def main():
    global tickets, login_proxy, game_proxy

    tickets = {}
    login_proxy = LoginProxy()
    game_proxy = GameProxy()

    read_data()
    read_maps()

    loop = asyncio.get_event_loop()
    loop.create_task(login_proxy.start())
    loop.create_task(game_proxy.start())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

main()