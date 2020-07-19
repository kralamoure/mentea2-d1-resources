import io
import json
import os
import re
import shutil

IN_FOLDER = "as"
OUT_FOLDER = "json"

def emptyDir(path):
    for filename in os.listdir(path):
        filePath = os.path.join(path, filename)
        if os.path.isfile(filePath):
            os.remove(filePath)
        elif os.path.isdir(filePath):
            shutil.rmtree(filePath)

def cleanPaths(paths):
    for path in paths:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            emptyDir(path)

def ensureDirs(paths):
    for path in paths:
        if not os.path.isdir(path):
            os.makedirs(path, exist_ok=True)

def cleanContent(content, enforceBegin=False, enforceEnd=False):
    lines = content.splitlines()
    if enforceBegin:
        lines = lines[lines.index("FILE_BEGIN = true;") + 1:]
    if enforceEnd:
        lines = lines[:lines.index("FILE_END = true;")]
    lines = [line for line in lines if (" = " in line) and (line != "FILE_BEGIN = true;") and (line != "FILE_END = true;") and (not line.startswith("VERSION = ")) and (not line.endswith(" = new Object();")) and (not line.endswith(" = new Array();")) and ("_root." not in line) and ("_global." not in line) and (not line.startswith("   "))]
    tempLineIds = []
    tempLines = []
    for line in reversed(lines):
        lineId = line[:line.index(" = ")]
        if lineId not in tempLineIds:
            tempLineIds.append(lineId)
            tempLines.append(line)
    lines = list(reversed(tempLines))
    lines.sort()
    content = "\n".join(lines)
    content = content.replace(";", "").replace("this.", "").replace("\\'", "'")
    content = re.sub("(?:String|Boolean|Number)\\((.+)\\)", "\\1", content)
    content = re.sub("(?<=[\\[,])(undefined)(?=[,\\]}])", "\"\\1\"", content)
    return content

def prelinkContent(content):
    lines = content.splitlines()
    for i in range(0, len(lines)):
        if "new Object()" in lines[i]:
            lines[i] = lines[i][:lines[i].index(",")].replace(" = {", ".").replace(":", " = ")
    content = "\n".join(lines)
    return content

def linkContent(content):
    lines = content.splitlines()
    root = {}
    for line in lines:
        lineId = line[:line.index(" = ")]
        lineId = lineId.replace("]", "").replace("[", ".").replace("\"", "")
        subIds = lineId.split(".")
        elem = root
        for subId in subIds[:-1]:
            if subId not in elem:
                elem[subId] = {}
            elem = elem[subId]
        value = line[line.index(" = ") + len(" = "):]
        value = re.sub("(?<=[{,])(\\w+)(?=:[^:])", "\"\\1\"", value)
        value = value.replace("\" + \"", "")
        elem[subIds[-1]] = json.loads(value)
    content = json.dumps(root, ensure_ascii=False)
    return content

def convertAs():
    for root, dirs, files in os.walk(IN_FOLDER):
        for filename in files:
            if not filename.endswith(".as"):
                continue
            filePath = os.path.join(root, filename)
            relPath = os.path.splitext(os.path.sep.join(filePath.split(os.path.sep)[1:]))[0]
            convertedFilePath = os.path.join(OUT_FOLDER, relPath + ".json")
            convertedDirPath = os.path.dirname(convertedFilePath)
            ensureDirs([convertedDirPath])
            with io.open(filePath, "r", encoding="utf-8") as i:
                content = i.read()
            content = cleanContent(content)
            content = prelinkContent(content)
            content = linkContent(content)
            with io.open(convertedFilePath, "w", encoding="utf-8") as o:
                o.write(content)

cleanPaths([OUT_FOLDER])
ensureDirs([OUT_FOLDER])
convertAs()