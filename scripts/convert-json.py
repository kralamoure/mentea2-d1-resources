import glob
import io
import json
import numpy
import os

IN_FOLDER = "renamed_json"
DATA_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

def getFiles(dirPath):
    files = []
    for filename in os.listdir(dirPath):
        filePath = os.path.join(dirPath, filename)
        if os.path.isfile(filePath):
            files.append(filePath)
    return files

def getFilePath(pattern):
    filePaths = glob.glob(pattern)
    if len(filePaths) > 0:
        return filePaths[0]
    else:
        return None

def readJson(filePath):
    with io.open(filePath, "r", encoding="utf-8") as i:
        content = i.read()
    return json.loads(content)

def escapeText(text):
    return text.replace("'", "\\'")

def convertAreas():
    pattern = os.path.join(IN_FOLDER, "lang", "swf", "maps_*_*.json")
    filePath = getFilePath(pattern)
    if filePath is None:
        return
    data = readJson(filePath)
    areas = data["map"]["areas"]
    for areaId in areas:
        area = areas[areaId]
        areaName = area["name"]
        superareaId = area["superAreaId"]
        print("INSERT INTO `area` (`area_id`, `area_name`, `superarea_id`)" +
            " VALUES ('" + str(areaId) + "', '" + escapeText(areaName) + "', '" + str(superareaId) + "');")

def convertItemSets():
    pattern = os.path.join(IN_FOLDER, "lang", "swf", "itemsets_*_*.json")
    filePath = getFilePath(pattern)
    if filePath is None:
        return
    data = readJson(filePath)
    itemSets = data["itemsets"]
    for itemSetId in itemSets:
        itemSet = itemSets[itemSetId]
        itemSetName = itemSet["name"]
        print("INSERT INTO `item_set` (`item_set_id`, `item_set_name`, `item_set_bonus`)" +
            " VALUES ('" + str(itemSetId) + "', '" + escapeText(itemSetName) + "', '');")

SUPPORTED_EFFECTS = [0, 7, 10, 81, 84, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 108, 110, 111, 112, 114, 115, 116, 117, 118, 119, 121, 122, 123, 124, 125, 126, 127, 128, 130, 138, 139, 146, 149, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 182, 183, 184, 193, 194, 197, 206, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 225, 226, 240, 241, 242, 243, 244, 246, 245, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 600, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 620, 621, 654, 700, 702, 705, 706, 710, 795, 800, 810, 811, 812, 930, 931, 932, 933, 934, 935, 936, 937, 939, 940, 948, 970, 971, 972, 973, 974]

def convertItemTemplates():
    pattern = os.path.join(IN_FOLDER, "lang", "swf", "items_*_*.json")
    filePath = getFilePath(pattern)
    if filePath is None:
        return
    data = readJson(filePath)
    itemTemplates = data["item"]["items"]
    for itemTemplateId in itemTemplates:
        itemTemplate = itemTemplates[itemTemplateId]
        itemType = itemTemplate["type"]
        itemName = itemTemplate["name"]
        itemLevel = itemTemplate["level"]
        weight = itemTemplate["weight"]
        price = itemTemplate["buyPrice"]
        conditions = ""
        if "conditions" in itemTemplate:
            conditions = itemTemplate["conditions"]
        weaponInfo = ""
        if "fightEffect" in itemTemplate:
            allWeaponInfo = itemTemplate["fightEffect"]
            weaponInfo = str(allWeaponInfo["apCost"]) + ";" + str(allWeaponInfo["minRange"]) + ";" + str(allWeaponInfo["maxRange"]) + ";" + str(allWeaponInfo["criticalHitRate"]) + ";" + str(allWeaponInfo["criticalFailureRate"]) + ";" + str(allWeaponInfo["criticalHitBonus"]) + ";" + str(1 if "isTwoHands" in itemTemplate else 0)
        print("INSERT INTO `item_template` (`item_template_id`, `item_type`, `item_name`, `item_level`, `item_effects`, `weight`, `item_set_id`, `price`, `conditions`, `weapon_info`)" +
            " VALUES ('" + str(itemTemplateId) + "', '" + str(itemType) + "', '" + escapeText(itemName) + "', '" + str(itemLevel) + "', '', '" + str(weight) + "', NULL, '" + str(price) + "', '" + conditions + "', '" + weaponInfo + "');")
    pattern = os.path.join(IN_FOLDER, "lang", "swf", "itemstats_*_*.json")
    filePath = getFilePath(pattern)
    if filePath is None:
        return
    data = readJson(filePath)
    allItemEffects = data["itemstats"]
    for itemTemplateId in allItemEffects:
        itemEffects = allItemEffects[itemTemplateId]
        itemEffectsSplit = itemEffects.split(",")
        newItemEffects = []
        for itemEffect in itemEffectsSplit:
            if itemEffect != "":
                itemEffectSplit = itemEffect.split("#")
                for itemEffectPartIndex in range(len(itemEffectSplit)):
                    itemEffectPart = itemEffectSplit[itemEffectPartIndex]
                    if itemEffectPart == "":
                        itemEffectSplit[itemEffectPartIndex] = "0"
                id = int(itemEffectSplit[0], 16)
                if id in SUPPORTED_EFFECTS:
                    newItemEffects.append("#".join(itemEffectSplit))
        newItemEffects = ",".join(newItemEffects)
        print("UPDATE `item_template` SET `item_effects` = '" + newItemEffects + "' WHERE (`item_template_id` = '" + str(itemTemplateId) + "');")
    pattern = os.path.join(IN_FOLDER, "lang", "swf", "itemsets_*_*.json")
    filePath = getFilePath(pattern)
    if filePath is None:
        return
    data = readJson(filePath)
    itemSets = data["itemsets"]
    for itemSetId in itemSets:
        itemSet = itemSets[itemSetId]
        itemTemplateIds = itemSet["itemIds"]
        for itemTemplateId in itemTemplateIds:
            print("UPDATE `item_template` SET `item_set_id` = '" + str(itemSetId) + "' WHERE (`item_template_id` = '" + str(itemTemplateId) + "');")

def convertItemTypes():
    pattern = os.path.join(IN_FOLDER, "lang", "swf", "items_*_*.json")
    filePath = getFilePath(pattern)
    if filePath is None:
        return
    data = readJson(filePath)
    itemTypes = data["item"]["types"]
    for typeId in itemTypes:
        itemType = itemTypes[typeId]
        typeName = itemType["name"]
        superType = itemType["superType"]
        effectArea = ""
        if "zones" in itemType:
            effectArea = itemType["zones"]
        print("INSERT INTO `item_type` (`type_id`, `type_name`, `super_type`, `effect_area`)" +
            " VALUES ('" + str(typeId) + "', '" + escapeText(typeName) + "', '" + str(superType) + "', " + ("'" + effectArea + "'" if effectArea != "" else "NULL") + ");")

def convertMaps():
    pattern = os.path.join(IN_FOLDER, "lang", "swf", "maps_*_*.json")
    filePath = getFilePath(pattern)
    if filePath is None:
        return
    data = readJson(filePath)
    maps = data["map"]["maps"]
    for id in maps:
        map = maps[id]
        places = "|"
        if "fightStartPositions1" in map and "fightStartPositions2" in map:
            places = map["fightStartPositions1"] + "|" + map["fightStartPositions2"]
        mapX = map["x"]
        mapY = map["y"]
        subareaId = map["subAreaId"]
        print("INSERT INTO `maps` (`id`, `date`, `width`, `height`, `key`, `mapdata`, `places`, `map_x`, `map_y`, `subarea_id`, `indoor`)" +
            " VALUES ('" + str(id) + "', '', '-1', '-1', '', '', '" + places + "', '" + str(mapX) + "', '" + str(mapY) + "', '" + str(subareaId) + "', '0');")
    path = os.path.join(IN_FOLDER, "maps")
    for filePath in getFiles(path):
        data = readJson(filePath)
        fileName = os.path.splitext(os.path.basename(filePath))[0]
        fileNameSplit = fileName.split("_")
        id = fileNameSplit[0]
        date = fileNameSplit[1][:-1]
        width = data["width"]
        height = data["height"]
        indoor = 0 if data["isOutdoor"] else 1
        print("UPDATE `maps` SET `date` = '" + date + "', `width` = '" + str(width) + "', `height` = '" + str(height) + "', `indoor` = '" + str(indoor) + "' WHERE (`id` = '" + id + "');")
    filePattern = os.path.join(DATA_FOLDER, "maps_*.json")
    filePaths = glob.glob(filePattern)
    for filePath in filePaths:
        data = readJson(filePath)
        maps = data["maps"]
        for id in maps:
            map = maps[id]
            date = map["date"]
            key = map["key"]
            mapData = map["decryptedData"]
            print("UPDATE `maps` SET `key` = '" + key + "', `mapData` = '" + mapData + "' WHERE (`id` = '" + id + "' AND `date` = '" + date + "');")

RESISTANCE_STAT_INFO = [
    ("neutral", 37),
    ("earth", 33),
    ("fire", 34),
    ("water", 35),
    ("air", 36),
    ("dodgeApLoss", 27),
    ("dodgeMpLoss", 28)
]

def convertMonsterTemplates():
    pattern = os.path.join(IN_FOLDER, "lang", "swf", "monsters_*_*.json")
    filePath = getFilePath(pattern)
    if filePath is None:
        return
    data = readJson(filePath)
    monsterTemplates = data["monsters"]
    for monsterId in monsterTemplates:
        monsterTemplate = monsterTemplates[monsterId]
        monsterName = monsterTemplate["name"]
        gfxid = monsterTemplate["gfxId"]
        grades = [monsterTemplate[key] for key in monsterTemplate if key.startswith("grade")]
        characteristics = ""
        for gradeIndex in range(len(grades)):
            grade = grades[gradeIndex]
            level = grade["level"]
            characteristics += str(level) + "@"
            for resistanceStatInfoIndex in range(len(RESISTANCE_STAT_INFO)):
                resistanceStatInfo = RESISTANCE_STAT_INFO[resistanceStatInfoIndex]
                characteristics += str(numpy.base_repr(resistanceStatInfo[1], 32)) + ":" + str(numpy.base_repr(grade["resistancePercents"][resistanceStatInfo[0]], 32))
                if resistanceStatInfoIndex < len(RESISTANCE_STAT_INFO) - 1:
                    characteristics += ";"
            if gradeIndex < len(grades) - 1:
                characteristics += "|"
        print("INSERT INTO `monster_template` (`monster_id`, `monster_name`, `gfxid`, `colors`, `ai`, `characteristics`, `life_points`, `initiatives`, `spells`)" +
            " VALUES ('" + str(monsterId) + "', '" + escapeText(monsterName) + "', '" + str(gfxid) + "', '-1,-1,-1', '-1', '" + characteristics + "', '" + "|".join(["-1"] * len(grades)) + "', '" + "|".join(["-1"] * len(grades)) + "', '" + "|".join([""] * len(grades)) + "');")

def convertNpcQuestions():
    pattern = os.path.join(IN_FOLDER, "lang", "swf", "dialog_*_*.json")
    filePath = getFilePath(pattern)
    if filePath is None:
        return
    data = readJson(filePath)
    questions = data["dialog"]["questions"]
    for questionId in questions:
        print("INSERT INTO `npc_question` (`question_id`, `response_ids`, `parameters`, `conditions`)" +
            " VALUES ('" + str(questionId) + "', '', '', '');")

def convertNpcResponses():
    pattern = os.path.join(IN_FOLDER, "lang", "swf", "dialog_*_*.json")
    filePath = getFilePath(pattern)
    if filePath is None:
        return
    data = readJson(filePath)
    responses = data["dialog"]["responses"]
    for responseId in responses:
        print("INSERT INTO `npc_response_action` (`response_id`, `action`, `arguments`)" +
            " VALUES ('" + str(responseId) + "', '', '');")

def convertNpcTemplates():
    pattern = os.path.join(IN_FOLDER, "lang", "swf", "npc_*_*.json")
    filePath = getFilePath(pattern)
    if filePath is None:
        return
    data = readJson(filePath)
    npcTemplates = data["npc"]["npcs"]
    for npcTemplateId in npcTemplates:
        print("INSERT INTO `npc_template` (`npc_template_id`, `gfxid`, `scale_x`, `scale_y`, `sex`, `color1`, `color2`, `color3`, `accessories`, `extra_clip`, `custom_artwork`, `store_items`)" +
            " VALUES ('" + str(npcTemplateId) + "', '-1', '-1', '-1', '0', '-1', '-1', '-1', '-1,-1,-1,-1,-1', '-1', '-1', NULL);")

BOOST_STAT_INFO = [
    ("upradeStrength", 10),
    ("upradeVitality", 11),
    ("upradeWisdom", 12),
    ("upradeChance", 13),
    ("upradeAgility", 14),
    ("upradeIntelligence", 15)
]

def convertPlayerRaces():
    pattern = os.path.join(IN_FOLDER, "lang", "swf", "classes_*_*.json")
    filePath = getFilePath(pattern)
    if filePath is None:
        return
    data = readJson(filePath)
    playerRaces = data["classes"]
    for raceId in playerRaces:
        playerRace = playerRaces[raceId]
        raceName = playerRace["shortName"]
        statsBoost = ""
        for boostStatInfoIndex in range(len(BOOST_STAT_INFO)):
            boostStatInfo = BOOST_STAT_INFO[boostStatInfoIndex]
            stat = playerRace[boostStatInfo[0]]
            statsBoost += str(boostStatInfo[1]) + ":"
            for intervalIndex in range(len(stat)):
                interval = stat[intervalIndex]
                start = interval["min"]
                cost = interval["cost"]
                statsBoost += str(start) + "@" + str(cost)
                if "count" in interval:
                    boost = interval["count"]
                    statsBoost += "@" + str(boost)
                if intervalIndex < len(stat) - 1:
                    statsBoost += ","
            if boostStatInfoIndex < len(BOOST_STAT_INFO) - 1:
                statsBoost += ";"
        raceSpells = "|".join(map(str, playerRace["spellIds"]))
        print("INSERT INTO `player_race` (`race_id`, `race_name`, `race_stats`, `start_discernment`, `start_pods`, `start_life`, `per_level_life`, `stats_boost`, `race_spells`, `map_id`, `cell_id`, `astrub_map_id`, `astrub_cell_id`)" +
            " VALUES ('" + str(raceId) + "', '" + escapeText(raceName) + "', '', '-1', '-1', '-1', '-1', '" + statsBoost + "', '" + raceSpells + "', '-1', '-1', '-1', '-1');")

SPELL_INFO = [
    ("level1", 1),
    ("level2", 2),
    ("level3", 3),
    ("level4", 4),
    ("level5", 5),
    ("level6", 6),
]

def convertSpells():
    pattern = os.path.join(IN_FOLDER, "lang", "swf", "spells_*_*.json")
    filePath = getFilePath(pattern)
    if filePath is None:
        return
    data = readJson(filePath)
    spells = data["spells"]
    for spellId in spells:
        spell = spells[spellId]
        spellName = spell["name"]
        spellLevels = {}
        for spellInfo in SPELL_INFO:
            if spellInfo[0] in spell:
                spellLvl = spell[spellInfo[0]]
                normal = spellLvl["normalHit"]
                normalEffects = ""
                for normalEffectIndex in range(len(normal)):
                    normalEffect = normal[normalEffectIndex]
                    effect = normalEffect["effectType"]
                    min = normalEffect["effectParam1"]
                    max = normalEffect["effectParam2"]
                    special = normalEffect["effectParam3"]
                    duration = normalEffect["effectRemainingTurn"]
                    probability = normalEffect["effectProbability"]
                    normalEffects += str(effect) + "," + (str(min) if min != None else "") + "," + (str(max) if max != None else "") + "," + (str(special) if special != None else "") + "," + str(duration) + "," + str(probability)
                    if "effectParam4" in normalEffect:
                        text = normalEffect["effectParam4"]
                        normalEffects += "," + text
                    if normalEffectIndex < len(normal) - 1:
                        normalEffects += ";"
                critical = spellLvl["criticalHit"]
                criticalEffects = ""
                if critical is not None:
                    for criticalEffectIndex in range(len(critical)):
                        criticalEffect = critical[criticalEffectIndex]
                        effect = criticalEffect["effectType"]
                        min = criticalEffect["effectParam1"]
                        max = criticalEffect["effectParam2"]
                        special = criticalEffect["effectParam3"]
                        duration = criticalEffect["effectRemainingTurn"]
                        probability = criticalEffect["effectProbability"]
                        criticalEffects += str(effect) + "," + (str(min) if min != None else "") + "," + (str(max) if max != None else "") + "," + (str(special) if special != None else "") + "," + str(duration) + "," + str(probability)
                        if "effectParam4" in criticalEffect:
                            text = criticalEffect["effectParam4"]
                            criticalEffects += "," + text
                        if criticalEffectIndex < len(critical) - 1:
                            criticalEffects += ";"
                apCost = spellLvl["apCost"]
                rangeMin = spellLvl["minRange"]
                rangeMax = spellLvl["maxRange"]
                criticalRate = spellLvl["criticalHitRate"]
                failureRate = spellLvl["criticalFailureRate"]
                lineOnly = 1 if spellLvl["isLineOnly"] else 0
                lineOfSight = 1 if spellLvl["hasLineOfSight"] else 0
                freeCell = 1 if spellLvl["needsFreeCell"] else 0
                boostRange = 1 if spellLvl["canBoostRange"] else 0
                classId = spellLvl["raceId"]
                launchByTurn = spellLvl["maxByTurn"]
                launchByPlayer = spellLvl["maxByPlayerByTurn"]
                launchDelay = spellLvl["turnsBetween"]
                effectAreas = spellLvl["zones"]
                requiredStates = ";".join(map(str, spellLvl["requiredStates"]))
                forbiddenStates = ";".join(map(str, spellLvl["forbiddenStates"]))
                minPlayerLevel = spellLvl["minPlayerLevel"]
                endsTurnOnFailure = spellLvl["criticalFailureEndsTurn"]
                spellLevels[spellInfo[1]] = (normalEffects if normalEffects != "" else ",,,,,") + "|" + (criticalEffects if criticalEffects != "" else ",,,,,") + "|" + str(apCost) + "|" + str(rangeMin) + "|" + (str(rangeMax) if rangeMin <= rangeMax else str(rangeMin)) + "|" + str(criticalRate) + "|" + str(failureRate) + "|" + str(lineOnly) + "|" + str(lineOfSight) + "|" + str(freeCell) + "|" + str(boostRange) + "|" + str(classId) + "|" + str(launchByTurn) + "|" + str(launchByPlayer) + "|" + str(launchDelay) + "|" + (effectAreas + ("" if normalEffects != "" else "Pa") + ("" if criticalEffects != "" else "Pa")) + "|" + requiredStates + "|" + forbiddenStates + "|" + str(minPlayerLevel) + "|" + str(endsTurnOnFailure).lower()
            else:
                spellLevels[spellInfo[1]] = ""
        print("INSERT INTO `spell` (`spell_id`, `spell_name`, `spell_sprite`, `spell_sprite_arg`, `spell_lvl_1`, `spell_lvl_2`, `spell_lvl_3`, `spell_lvl_4`, `spell_lvl_5`, `spell_lvl_6`, `spell_target`)" +
            " VALUES ('" + str(spellId) + "', '" + escapeText(spellName) + "', '-1', '-1,-1,-1', '" + spellLevels[1] + "', '" + spellLevels[2] + "', '" + spellLevels[3] + "', '" + spellLevels[4] + "', '" + spellLevels[5] + "', '" + spellLevels[6] + "', '');")

def convertSubareas():
    pattern = os.path.join(IN_FOLDER, "lang", "swf", "maps_*_*.json")
    filePath = getFilePath(pattern)
    if filePath is None:
        return
    data = readJson(filePath)
    subareas = data["map"]["subAreas"]
    for subareaId in subareas:
        subarea = subareas[subareaId]
        areaId = subarea["areaId"]
        subareaName = subarea["name"]
        print("INSERT INTO `subarea` (`subarea_id`, `area_id`, `subarea_name`, `conquestable`, `alignment`)" +
            " VALUES ('" + str(subareaId) + "', '" + str(areaId) + "', '" + escapeText(subareaName) + "', '-1', '-1');")

def convertJson():
    convertAreas()
    convertItemSets()
    convertItemTemplates()
    convertItemTypes()
    convertMaps()
    convertMonsterTemplates()
    convertNpcQuestions()
    convertNpcResponses()
    convertNpcTemplates()
    convertPlayerRaces()
    convertSpells()
    convertSubareas()

convertJson()