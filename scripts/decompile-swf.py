import glob
import io
import os
import platform
import shutil
import subprocess

FFDEC_PATH = os.path.join("ffdec_*", "ffdec")
IN_FOLDER = "swf"
OUT_FOLDER = "as"

TEMP_FOLDER = "temp"

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

def getDirs(dirPath):
    dirs = []
    for filename in os.listdir(dirPath):
        filePath = os.path.join(dirPath, filename)
        if os.path.isdir(filePath):
            dirs.append(filePath)
    return dirs

def deleteEmptyDirs(path):
    for root, dirs, files in list(os.walk(path, topdown=False))[:-1]:
        if len(os.listdir(root)) == 0:
            os.rmdir(root)

def getFiles(dirPath):
    files = []
    for filename in os.listdir(dirPath):
        filePath = os.path.join(dirPath, filename)
        if os.path.isfile(filePath):
            files.append(filePath)
    return files

def getFileIndex(filePath):
    filename = os.path.splitext(os.path.basename(filePath))[0]
    if "_" not in filename:
        return 1
    return int(filename.split("_")[-1])

def getFfdecPath():
    searchPath = FFDEC_PATH + "."
    if platform.system() == "Darwin" or platform.system() == "Linux":
        searchPath += "sh"
    elif platform.system() == "Windows":
        searchPath += "bat"
    else:
        return None
    filePaths = glob.glob(searchPath)
    if len(filePaths) > 0:
        return filePaths[0]
    else:
        return None

def decompileSwf():
    ffdecFilePath = getFfdecPath()
    if ffdecFilePath is None:
        return
    for root, dirs, files in os.walk(IN_FOLDER):
        swfFilenames = list(filter(lambda filename: filename.endswith(".swf"), files))
        if len(swfFilenames) == 0:
            continue
        relDirPath = os.path.sep.join(root.split(os.path.sep)[1:])
        tempDirPath = os.path.join(OUT_FOLDER, TEMP_FOLDER, relDirPath)
        defDirPath = os.path.join(OUT_FOLDER, relDirPath)
        ensureDirs([tempDirPath, defDirPath])
        subprocess.run([ffdecFilePath, "-export", "script", os.path.abspath(tempDirPath), os.path.abspath(root)])
        for fileDirPath in getDirs(tempDirPath):
            if not fileDirPath.endswith(".swf"):
                continue
            scriptDirPath = os.path.join(fileDirPath, "scripts", "frame_1")
            if not os.path.isdir(scriptDirPath):
                continue
            defFilename = os.path.splitext(os.path.basename(fileDirPath))[0] + ".as"
            defFilePath = os.path.join(defDirPath, defFilename)
            with io.open(defFilePath, "w", encoding="utf-8") as o:
                scriptFilePaths = getFiles(scriptDirPath)
                scriptFilePaths.sort(key=getFileIndex)
                for scriptFilePath in scriptFilePaths:
                    with io.open(scriptFilePath, "r", encoding="utf-8") as i:
                        o.write(i.read())
    tempPath = os.path.join(OUT_FOLDER, TEMP_FOLDER)
    shutil.rmtree(tempPath)
    deleteEmptyDirs(OUT_FOLDER)

cleanPaths([OUT_FOLDER])
ensureDirs([OUT_FOLDER])
decompileSwf()