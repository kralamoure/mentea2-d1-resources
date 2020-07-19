import fnmatch
import os
import shutil

CLIENT_FOLDER = "client"
LANG_FOLDER = "lang"
OUT_FOLDER = "swf"

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

def deleteEmptyDirs(path):
    for root, dirs, files in list(os.walk(path, topdown=False))[:-1]:
        if len(os.listdir(root)) == 0:
            os.rmdir(root)

def include_patterns(*patterns):
    def _ignore_patterns(path, all_names):
        keep = (name for pattern in patterns
                        for name in fnmatch.filter(all_names, pattern))
        dir_names = (name for name in all_names if os.path.isdir(os.path.join(path, name)))
        return set(all_names) - set(keep) - set(dir_names)
    return _ignore_patterns

def copySwf():
    dataPath = os.path.join(CLIENT_FOLDER, "data")
    for filename in os.listdir(dataPath):
        filePath = os.path.join(dataPath, filename)
        if os.path.isdir(filePath):
            shutil.copytree(filePath, os.path.join(OUT_FOLDER, filename), ignore=include_patterns("*.swf"))
    shutil.copytree(LANG_FOLDER, os.path.join(OUT_FOLDER, "lang"), ignore=include_patterns("*.swf"))
    deleteEmptyDirs(OUT_FOLDER)

cleanPaths([OUT_FOLDER])
ensureDirs([OUT_FOLDER])
copySwf()