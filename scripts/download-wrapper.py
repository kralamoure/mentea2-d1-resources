import os
import requests
import shutil

OUT_PLATFORM = "windows" # windows | darwin | linux
OUT_VERSION = "main" # main | beta
OUT_FOLDER = "wrapper"

TEMP_FOLDER = "temp"
CYTRUS_URL = "https://launcher.cdn.ankama.com/cytrus.json"
RELEASE_URL = "https://launcher.cdn.ankama.com/retro/releases/"
HASH_URL = "https://launcher.cdn.ankama.com/retro/hashes/"

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

def moveFiles(dirPath, newDirPath):
    for filename in os.listdir(dirPath):
        filePath = os.path.join(dirPath, filename)
        newFilePath = os.path.join(newDirPath, filename)
        os.rename(filePath, newFilePath)

def downloadFile(url, path):
    ensureDirs([os.path.dirname(path)])
    with open(path, "wb") as f:
        for chunk in requests.get(url, stream=True).iter_content(1024):
            f.write(chunk)

def getVersion():
    cytrus = requests.get(CYTRUS_URL).json()
    version = cytrus["games"]["retro"]["platforms"][OUT_PLATFORM][OUT_VERSION]
    return version

def downloadHash(hash):
    url = HASH_URL + hash[:2] + "/" + hash
    path = os.path.join(OUT_FOLDER, TEMP_FOLDER, hash)
    downloadFile(url, path)

def downloadPacks(packs):
    fileHashes = []
    for packHash in packs:
        fileHashes += packs[packHash]["hashes"]
        downloadHash(packHash)
    return fileHashes

def downloadFiles(files, excludedFileHashes):
    for filePath in files:
        fileHash = files[filePath]["hash"]
        if fileHash not in excludedFileHashes:
            downloadHash(fileHash)

def extractPacks(packs):
    for packHash in packs:
        packPath = os.path.join(OUT_FOLDER, TEMP_FOLDER, packHash)
        shutil.unpack_archive(packPath, os.path.dirname(packPath), "tar")
        os.remove(packPath)

def renameFiles(files):
    for filePath in files:
        fileHash = files[filePath]["hash"]
        oldFilePath = os.path.join(OUT_FOLDER, TEMP_FOLDER, fileHash)
        if not os.path.isfile(oldFilePath):
            for filePath2 in files:
                fileHash2 = files[filePath2]["hash"]
                if fileHash == fileHash2:
                    newFilePath2 = os.path.join(OUT_FOLDER, TEMP_FOLDER, filePath2.replace("/", os.path.sep))
                    shutil.copyfile(newFilePath2, oldFilePath)
                    break
        newFilePath = os.path.join(OUT_FOLDER, TEMP_FOLDER, filePath.replace("/", os.path.sep))
        newDirPath = os.path.dirname(newFilePath)
        ensureDirs([newDirPath])
        os.rename(oldFilePath, newFilePath)

def downloadReleasePart(part):
    downloadedFileHashes = downloadPacks(part["packs"])
    downloadFiles(part["files"], downloadedFileHashes)
    extractPacks(part["packs"])
    renameFiles(part["files"])

def downloadRelease(version):
    release = requests.get(RELEASE_URL + OUT_VERSION + "/" + OUT_PLATFORM + "/" + version + ".json").json()
    downloadReleasePart(release[OUT_PLATFORM])

def downloadWrapper():
    version = getVersion()
    downloadRelease(version)

def cleanWrapper():
    tempPath = os.path.join(OUT_FOLDER, TEMP_FOLDER)
    windowsLinuxPath = os.path.join(tempPath, "resources", "app", "retroclient")
    darwinPath = os.path.join(tempPath, "Dofus Retro.app", "Contents", "Resources", "app", "retroclient")
    if os.path.isdir(windowsLinuxPath):
        clientPath = windowsLinuxPath
    elif os.path.isdir(darwinPath):
        clientPath = darwinPath
    else:
        return
    for filename in os.listdir(clientPath):
        filePath = os.path.join(clientPath, filename)
        if os.path.isdir(filePath):
            if filename != "js":
                shutil.rmtree(filePath)
        elif os.path.isfile(filePath):
            if filename != "D1ElectronLauncher.html":
                os.remove(filePath)
    moveFiles(tempPath, OUT_FOLDER)
    shutil.rmtree(tempPath)
    
cleanPaths([OUT_FOLDER])
ensureDirs([OUT_FOLDER])
downloadWrapper()
cleanWrapper()