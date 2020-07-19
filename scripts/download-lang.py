import os
import requests
import shutil

OUT_VERSION = "main" # main | beta
OUT_LANGS = ["fr"] # fr | en | de | es | pt | it | nl
OUT_FOLDER = "lang"

LANG_URL = {
    "main": "http://dofusretro.cdn.ankama.com/",
    "beta": "http://dofusretro.cdn.ankama.com/beta/"
}

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

def readFile(path):
    with open(path, "r") as f:
        content = f.read()
    return content

def downloadFile(url, path):
    ensureDirs([os.path.dirname(path)])
    with open(path, "wb") as f:
        for chunk in requests.get(url, stream=True).iter_content(1024):
            f.write(chunk)

def downloadUrlPath(urlPath):
    url = LANG_URL[OUT_VERSION] + "lang/" + urlPath
    filePath = os.path.join(OUT_FOLDER, urlPath.replace("/", os.path.sep))
    downloadFile(url, filePath)
    return filePath

def downloadLang():
    downloadUrlPath("versions.swf")
    for lang in OUT_LANGS:
        filePath = downloadUrlPath("versions_" + lang + ".txt")
        content = readFile(filePath)
        swfs = content[3:-1].split("|")
        for swf in swfs:
            downloadUrlPath("swf/" + swf.replace(",", "_") + ".swf")

cleanPaths([OUT_FOLDER])
ensureDirs([OUT_FOLDER])
downloadLang()