import io
import json
import os
import re
import shutil

IN_FOLDER = "json"
OUT_FOLDER = "renamed_json"

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

def insertInDict(d, key, value, index):
    return {**dict(list(d.items())[:index]), **{key: value}, **dict(list(d.items())[index:])}

def convertList(l):
    d = {}
    for i in range(0, len(l)):
        d[i] = l[i]
    return d

def isList(value):
    return isinstance(value, list)

def isDict(value):
    return isinstance(value, dict)

def cleanContent(content):
    return re.sub("(?<![:,])(\\s|\\\\r|\\\\\\\\r|\\\\n|\\\\\\\\n)+\"", "\"", content)

ANY = -1

def renameData(data, descr):
    if isList(data) and isList(descr):
        for i in range(0, len(data)):
            data[i] = renameData(data[i], descr[0])
    elif isList(data) and isDict(descr):
        data = convertList(data)
        data = renameData(data, descr)
    elif isDict(data) and isDict(descr):
        oldKeys = list(map(lambda x: x[0] if isinstance(x, tuple) else x, descr.keys()))
        newKeys = list(map(lambda x: x[1] if isinstance(x, tuple) else None, descr.keys()))
        for key in list(data.keys()):
            if len(oldKeys) == 1 and oldKeys[0] == ANY:
                data[key] = renameData(data[key], list(descr.values())[0])
            elif key in oldKeys:
                descrIndex = oldKeys.index(key)
                newKey = newKeys[descrIndex]
                if newKey is not None:
                    dataIndex = list(data.keys()).index(key)
                    data = insertInDict(data, newKey, data.pop(key), dataIndex)
                    key = newKey
                data[key] = renameData(data[key], list(descr.values())[descrIndex])
    return data

def renameContent(content, path):
    descr = None
    if path.startswith("docs" + os.path.sep):
        descr = {"author": ANY,
                "chapters":
                    {ANY:
                        {(0,"name"): ANY,
                        (1,"number"): ANY,
                        (2,"isPageAfterLeftNamePageBlank"): ANY,
                        (3,"hasNamePage"): ANY}},
                "pages":
                    {ANY: ANY},
                ("style","styleId"): ANY,
                "subtitle": ANY,
                "title": ANY,
                "type": ANY}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "alignment_"):
        descr = {("A","alignment"):
                    {("a","alignements"):
                        {ANY:
                            {("n","name"): ANY,
                            ("c","c"): ANY}},
                    ("at","canAttack"):
                        {ANY:
                            {ANY: ANY}},
                    ("b","balances"):
                        {ANY:
                            {("s","minPercent"): ANY,
                            ("e","maxPercent"): ANY,
                            ("n","name"): ANY,
                            ("d","description"): ANY}},
                    ("f","feats"):
                        {ANY:
                            {("n","name"): ANY,
                            ("g","gfxId"): ANY,
                            ("e","effectId"): ANY}},
                    ("fe","featEffects"):
                        {ANY: ANY},
                    ("g","canViewGainOf"):
                        {ANY:
                            {ANY: ANY}},
                    ("jo","canJoin"):
                        {ANY:
                            {ANY: ANY}},
                    ("o","orders"):
                        {ANY:
                            {("n","name"): ANY,
                            ("a","alignementId"): ANY}},
                    ("s","specializations"):
                        {ANY:
                            {("n","name"): ANY,
                            ("d","description"): ANY,
                            ("o","orderId"): ANY,
                            ("av","alignmentLevel"): ANY,
                            ("f","feats"):
                                [{(0, "id"): ANY,
                                (1, "level"): ANY,
                                (2, "params"): [ANY]}]}}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "audio_"):
        descr = {("AUAC", "environmentIds"): ANY,
                ("AUA", "environments"):
                    {ANY:
                        {("bg","effectId"): [ANY],
                        ("mind","minSeconds"): ANY,
                        ("maxd","maxExtraSeconds"): ANY,
                        ("n","effectIds"): [ANY]}},
                ("AUEC", "effectIds"): ANY,
                ("AUE", "effects"):
                    {ANY:
                        {("f","file"): ANY,
                        ("v","baseVolume"): ANY,
                        ("l","isLooping"): ANY,
                        ("s","isStreaming"): ANY,
                        ("o","offset"): ANY}},
                ("AUMC", "musicIds"): ANY,
                ("AUM", "musics"):
                    {ANY:
                        {("f","file"): ANY,
                        ("v","baseVolume"): ANY,
                        ("l","isLooping"): ANY,
                        ("s","isStreaming"): ANY,
                        ("o","offset"): ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "classes_"):
        descr = {("G","classes"):
                    {ANY:
                        {("sn","shortName"): ANY,
                        ("ln","longName"): ANY,
                        ("ep","ep"): ANY,
                        ("d","longDescription"): ANY,
                        ("sd","shortDescription"): ANY,
                        ("s","spellIds"): [ANY],
                        ("cc","closeCombat"):
                            {(0,"normalHit"):
                                [{(0, "effectType"): ANY,
                                (1, "effectParam1"): ANY,
                                (2, "effectParam2"): ANY,
                                (3, "effectParam3"): ANY}],
                            (1,"criticalHitBonus"): ANY,
                            (2,"apCost"): ANY,
                            (3,"minRange"): ANY,
                            (4,"maxRange"): ANY,
                            (5,"criticalHitRate"): ANY,
                            (6,"criticalFailureRate"): ANY,
                            (7,"isLineOnly"): ANY,
                            (8,"hasLineOfSight"): ANY,
                            (9,"requiredStates"): ANY,
                            (10,"forbiddenStates"): ANY},
                        ("b10","upradeStrength"):
                            [{(0,"min"): ANY,
                            (1,"cost"): ANY,
                            (2,"count"): ANY}],
                        ("b11","upradeVitality"):
                            [{(0,"min"): ANY,
                            (1,"cost"): ANY,
                            (2,"count"): ANY}],
                        ("b12","upradeWisdom"):
                            [{(0,"min"): ANY,
                            (1,"cost"): ANY,
                            (2,"count"): ANY}],
                        ("b13","upradeChance"):
                            [{(0,"min"): ANY,
                            (1,"cost"): ANY,
                            (2,"count"): ANY}],
                        ("b14","upradeAgility"):
                            [{(0,"min"): ANY,
                            (1,"cost"): ANY,
                            (2,"count"): ANY}],
                        ("b15","upradeIntelligence"):
                            [{(0,"min"): ANY,
                            (1,"cost"): ANY,
                            (2,"count"): ANY}]}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "crafts_"):
        descr = {("CR","crafts"):
                    {ANY:
                        [{(0, "itemModelId"): ANY,
                        (1, "itemQuantity"): ANY}]}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "dialog_"):
        descr = {("D","dialog"):
                    {("a","responses"): ANY,
                    ("q","questions"): ANY}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "dungeons_"):
        descr = {("DU","dungeons"):
                    {ANY:
                        {("n","name"): ANY,
                        ("m","maps"):
                            {ANY:
                                {("x","x"): ANY,
                                ("y","y"): ANY,
                                ("z","z"): ANY,
                                ("n","name"): ANY,
                                ("i","i"): ANY}}}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "effects_"):
        descr = {("EDMG","damageEffectIds"): ANY,
                ("EHEL","healingEffectIds"): ANY,
                ("E","effects"):
                    {ANY:
                        {("d","description"): ANY,
                        ("c","statId"): ANY,
                        ("o","operator"): ANY,
                        ("t","hasTooltip"): ANY,
                        ("j","isDice"): ANY,
                        ("e","element"): ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "emotes_"):
        descr = {("EM","emotes"):
                    {ANY:
                        {("n","name"): ANY,
                        ("s","shortcut"): ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "fightChallenge_"):
        descr = {("FC","fightChallenges"):
                    {ANY:
                        {("n","name"): ANY,
                        ("d","description"): ANY,
                        ("g","gfxId"): ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "guilds_"):
        descr = {("GU","guild"):
                    {("b","upgrades"):
                        {("w","taxCollectorPods"):
                            [{(0,"min"): ANY,
                            (1,"cost"): ANY,
                            (2,"count"): ANY}],
                        ("p","taxCollectorProspecting"):
                            [{(0,"min"): ANY,
                            (1,"cost"): ANY,
                            (2,"count"): ANY}],
                        ("c","taxCollectorMaxCount"):
                            [{(0,"min"): ANY,
                            (1,"cost"): ANY,
                            (2,"count"): ANY}],
                        ("x","taxCollectorWisdom"):
                            [{(0,"min"): ANY,
                            (1,"cost"): ANY,
                            (2,"count"): ANY}],
                        ("s","taxCollectorSpellLevels"):
                            [{(0,"min"): ANY,
                            (1,"cost"): ANY}],
                        ("wm","maxTaxCollectorPods"): ANY,
                        ("pm","maxTaxCollectorProspecting"): ANY,
                        ("cm","maxTaxCollectorMaxCount"): ANY,
                        ("xm","maxTaxCollectorWisdom"): ANY,
                        ("sm","maxTaxCollectorSpellLevels"): ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "hints_"):
        descr = {("HI","hints"):
                    {ANY:
                        {("n","name"): ANY,
                        ("c","categoryId"): ANY,
                        ("g","gfxId"): ANY,
                        ("m","mapId"): ANY}},
                ("HIC","hintCategories"):
                    {ANY:
                        {("n","name"): ANY,
                        ("c","color"): ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "houses_"):
        content = content.replace("\"ids\"", "\"is\"")
        descr = {("H","house"):
                    {("d","doorMaps"):
                        {ANY:
                            {ANY: ANY}},
                    ("h","houses"):
                        {ANY:
                            {("n","name"): ANY,
                            ("d","description"): ANY}},
                    ("is","indoorSkills"): [ANY],
                    ("m","roomMaps"):
                        {ANY: ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "interactiveobjects_"):
        descr = {("IO","interactiveobject"):
                    {("d","interactiveobjects"):
                        {ANY:
                            {("n","name"): ANY,
                            ("t","type"): ANY,
                            ("sk","skillIds"): [ANY]}},
                    ("g","gfxIds"):
                        {ANY: ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "items_"):
        descr = {("I","item"):
                    {("ss","superTypePositions"):
                        {ANY:
                            [ANY]},
                    ("st","superTypes"): ANY,
                    ("t","types"):
                        {ANY:
                            {("n","name"): ANY,
                            ("t","superType"): ANY,
                            ("z","zones"): ANY}},
                    ("u","items"):
                        {ANY:
                            {("n","name"): ANY,
                            ("t","type"): ANY,
                            ("d","description"): ANY,
                            ("ep","ep"): ANY,
                            ("g","gfxId"): ANY,
                            ("l","level"): ANY,
                            ("wd","wd"): ANY,
                            ("fm","isForgemageable"): ANY,
                            ("tw","isTwoHands"): ANY,
                            ("et","isEthereal"): ANY,
                            ("h","isHidden"): ANY,
                            ("w","weight"): ANY,
                            ("m","isCursed"): ANY,
                            ("an","animationId"): ANY,
                            ("e","fightEffect"):
                                {(0,"criticalHitBonus"): ANY,
                                (1,"apCost"): ANY,
                                (2,"minRange"): ANY,
                                (3,"maxRange"): ANY,
                                (4,"criticalHitRate"): ANY,
                                (5,"criticalFailureRate"): ANY,
                                (6,"isLineOnly"): ANY,
                                (7,"hasLineOfSight"): ANY},
                            ("c","conditions"): ANY,
                            ("u","canUse"): ANY,
                            ("ut","canTarget"): ANY,
                            ("s","setId"): ANY,
                            ("p","buyPrice"): ANY}},
                    ("us","texts"): ANY}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "itemsets_"):
        descr = {("IS","itemsets"):
                    {ANY:
                        {("n","name"): ANY,
                        ("i","itemIds"): [ANY]}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "itemstats_"):
        descr = {("ISTA","itemstats"):
                    {ANY: ANY}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "jobs_"):
        descr = {("J","jobs"):
                    {ANY:
                        {("n","name"): ANY,
                        ("s","specializationOf"): ANY,
                        ("g","gfxId"): ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "kb_"):
        descr = {("KBA","knownledgeBaseArticles"):
                    {ANY:
                        {("c","categoryId"): ANY,
                        ("n","name"): ANY,
                        ("o","order"): ANY,
                        ("a","text"): ANY,
                        ("k","keywords"): [ANY],
                        ("i","id"): ANY,
                        ("ep","ep"): ANY}},
                ("KBC","knowledgeBaseCategories"):
                    {ANY:
                        {("n","name"): ANY,
                        ("o","order"): ANY,
                        ("i","id"): ANY,
                        ("ep","ep"): ANY}},
                ("KBD","knowledgeBaseTriggers"):
                    {ANY:
                        {("t","type"): ANY,
                        ("v","values"): [ANY],
                        ("d","tipId"): ANY}},
                ("KBT","knwoledgeBaseTips"):
                    {ANY:
                        {("i","id"): ANY,
                        ("c","text"): ANY,
                        ("l","articleId"): ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "lang_"):
        descr = {("ABR","abuseReasons"):
                    {ANY:
                        {("i","id"): ANY,
                        ("t","text"): ANY}},
                ("C","config"): ANY,
                ("CNS","consoleShortcuts"):
                    {ANY:
                        {("k","key"): ANY,
                        ("c","modifier"): ANY}},
                ("COM","communities"):
                    {ANY:
                        {("n","name"): ANY,
                        ("i","id"): ANY,
                        ("d","enabled"): ANY,
                        ("c","countries"): [ANY]}},
                ("CSR","censoredWords"):
                    {ANY:
                        {("l","weight"): ANY,
                        ("c","word"): ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "maps_"):
        descr = {("MA","map"):
                    {("a","areas"):
                        {ANY:
                            {("n","name"): ANY,
                            ("sua","superAreaId"): ANY}},
                    ("m","maps"):
                        {ANY:
                            {("x","x"): ANY,
                            ("y","y"): ANY,
                            ("sa","subAreaId"): ANY,
                            ("p1","fightStartPositions1"): ANY,
                            ("p2","fightStartPositions2"): ANY,
                            ("p","displayedCellObjects"):
                                [{(0,"ids"): [ANY],
                                (1,"cellId"): ANY,
                                (2,"criterion"): ANY}],
                            ("d","dungeonId"): ANY,
                            ("c","maxFightPlayers"): ANY,
                            ("t","maxTeamPlayers"): ANY,
                            ("ep","ep"): ANY}},
                    ("sa","subAreas"):
                        {ANY:
                            {("n","name"): ANY,
                            ("a","areaId"): ANY,
                            ("m","musicIds"): [ANY],
                            ("v","neighborIds"): [ANY]}},
                    ("sua","superAreas"): ANY}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "monsters_"):
        descr = {("MR","monsterRaces"):
                    {ANY:
                        {("n","name"): ANY,
                        ("s","superRaceId"): ANY}},
                ("MSR","monsterSuperRaces"):
                    {ANY:
                        {("n","name"): ANY,
                        ("s","id"): ANY}},
                ("M","monsters"):
                    {ANY:
                        {("n","name"): ANY,
                        ("g","gfxId"): ANY,
                        ("b","raceId"): ANY,
                        ("a","alignmentId"): ANY,
                        ("k","isKickable"): ANY,
                        ("g1","grade1"):
                            {("l","level"): ANY,
                            ("r","resistancePercents"):
                                {(0,"neutral"): ANY,
                                (1,"earth"): ANY,
                                (2,"fire"): ANY,
                                (3,"water"): ANY,
                                (4,"air"): ANY,
                                (5,"dodgeApLoss"): ANY,
                                (6,"dodgeMpLoss"): ANY},
                            ("lp","lp"): ANY,
                            ("ap","ap"): ANY,
                            ("mp","mp"): ANY},
                        ("g2","grade2"):
                            {("l","level"): ANY,
                            ("r","resistancePercents"):
                                {(0,"neutral"): ANY,
                                (1,"earth"): ANY,
                                (2,"fire"): ANY,
                                (3,"water"): ANY,
                                (4,"air"): ANY,
                                (5,"dodgeApLoss"): ANY,
                                (6,"dodgeMpLoss"): ANY},
                            ("lp","lp"): ANY,
                            ("ap","ap"): ANY,
                            ("mp","mp"): ANY},
                        ("g3","grade3"):
                            {("l","level"): ANY,
                            ("r","resistancePercents"):
                                {(0,"neutral"): ANY,
                                (1,"earth"): ANY,
                                (2,"fire"): ANY,
                                (3,"water"): ANY,
                                (4,"air"): ANY,
                                (5,"dodgeApLoss"): ANY,
                                (6,"dodgeMpLoss"): ANY},
                            ("lp","lp"): ANY,
                            ("ap","ap"): ANY,
                            ("mp","mp"): ANY},
                        ("g4","grade4"):
                            {("l","level"): ANY,
                            ("r","resistancePercents"):
                                {(0,"neutral"): ANY,
                                (1,"earth"): ANY,
                                (2,"fire"): ANY,
                                (3,"water"): ANY,
                                (4,"air"): ANY,
                                (5,"dodgeApLoss"): ANY,
                                (6,"dodgeMpLoss"): ANY},
                            ("lp","lp"): ANY,
                            ("ap","ap"): ANY,
                            ("mp","mp"): ANY},
                        ("g5","grade5"):
                            {("l","level"): ANY,
                            ("r","resistancePercents"):
                                {(0,"neutral"): ANY,
                                (1,"earth"): ANY,
                                (2,"fire"): ANY,
                                (3,"water"): ANY,
                                (4,"air"): ANY,
                                (5,"dodgeApLoss"): ANY,
                                (6,"dodgeMpLoss"): ANY},
                            ("lp","lp"): ANY,
                            ("ap","ap"): ANY,
                            ("mp","mp"): ANY},
                        ("g6","grade6"):
                            {("l","level"): ANY,
                            ("r","resistancePercents"):
                                {(0,"neutral"): ANY,
                                (1,"earth"): ANY,
                                (2,"fire"): ANY,
                                (3,"water"): ANY,
                                (4,"air"): ANY,
                                (5,"dodgeApLoss"): ANY,
                                (6,"dodgeMpLoss"): ANY},
                            ("lp","lp"): ANY,
                            ("ap","ap"): ANY,
                            ("mp","mp"): ANY},
                        ("g7","grade7"):
                            {("l","level"): ANY,
                            ("r","resistancePercents"):
                                {(0,"neutral"): ANY,
                                (1,"earth"): ANY,
                                (2,"fire"): ANY,
                                (3,"water"): ANY,
                                (4,"air"): ANY,
                                (5,"dodgeApLoss"): ANY,
                                (6,"dodgeMpLoss"): ANY},
                            ("lp","lp"): ANY,
                            ("ap","ap"): ANY,
                            ("mp","mp"): ANY},
                        ("g8","grade8"):
                            {("l","level"): ANY,
                            ("r","resistancePercents"):
                                {(0,"neutral"): ANY,
                                (1,"earth"): ANY,
                                (2,"fire"): ANY,
                                (3,"water"): ANY,
                                (4,"air"): ANY,
                                (5,"dodgeApLoss"): ANY,
                                (6,"dodgeMpLoss"): ANY},
                            ("lp","lp"): ANY,
                            ("ap","ap"): ANY,
                            ("mp","mp"): ANY},
                        ("g9","grade9"):
                            {("l","level"): ANY,
                            ("r","resistancePercents"):
                                {(0,"neutral"): ANY,
                                (1,"earth"): ANY,
                                (2,"fire"): ANY,
                                (3,"water"): ANY,
                                (4,"air"): ANY,
                                (5,"dodgeApLoss"): ANY,
                                (6,"dodgeMpLoss"): ANY},
                            ("lp","lp"): ANY,
                            ("ap","ap"): ANY,
                            ("mp","mp"): ANY},
                        ("g10","grade10"):
                            {("l","level"): ANY,
                            ("r","resistancePercents"):
                                {(0,"neutral"): ANY,
                                (1,"earth"): ANY,
                                (2,"fire"): ANY,
                                (3,"water"): ANY,
                                (4,"air"): ANY,
                                (5,"dodgeApLoss"): ANY,
                                (6,"dodgeMpLoss"): ANY},
                            ("lp","lp"): ANY,
                            ("ap","ap"): ANY,
                            ("mp","mp"): ANY}}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "names_"):
        descr = {("NF","name"):
                    {("f","firstNames"): ANY,
                    ("n","lastNames"): ANY}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "npc_"):
        descr = {("N","npc"):
                    {("a","actions"):
                        {ANY: ANY},
                    ("d","npcs"):
                        {ANY:
                            {("n","name"): ANY,
                            ("a","actionIds"): [ANY]}}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "pvp_"):
        descr = {("PP","pvp"):
                    {("grds","alignmentRanks"):
                        [[{("nc","shortName"): ANY,
                        ("nl","longName"): ANY}]],
                    ("hp","rankMaxHonor"): [ANY],
                    ("maxdp","maxDisgrace"): ANY}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "quests_"):
        descr = {("Q","quest"):
                    {("o","objectives"):
                        {ANY:
                            {("t","type"): ANY,
                            ("p","parameters"): [ANY]}},
                    ("q","quests"):
                        {ANY: ANY},
                    ("s","steps"):
                        {ANY:
                            {("n","name"): ANY,
                            ("d","description"): ANY,
                            ("r","rewards"):
                                {(0,"xp"): ANY,
                                (1,"money"): ANY,
                                (2,"items"):
                                    [{(0,"modelId"): ANY,
                                    (1,"quantity"): ANY}],
                                (3,"emoteIds"): [ANY],
                                (4,"jobIds"): [ANY],
                                (5,"spellIds"): [ANY]}}},
                    ("t","objectiveTypes"): ANY}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "ranks_"):
        descr = {("R","guildRanks"):
                    {ANY:
                        {("n","name"): ANY,
                        ("o","order"): ANY,
                        ("i","id"): ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "rides_"):
        descr = {("RIA","mountCapacities"):
                    {ANY:
                        {("n","name"): ANY,
                        ("d","description"): ANY,
                        ("e","e"): ANY}},
                ("RI","mounts"):
                    {ANY:
                        {("n","name"): ANY,
                        ("g","gfxId"): ANY,
                        ("c1","color1"): ANY,
                        ("c2","color2"): ANY,
                        ("c3","color3"): ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "scripts_"):
        descr = {("SCR","tutorials"):
                    {ANY: ANY}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "servers_"):
        descr = {("SRC","serverCommunities"):
                    {ANY:
                        {("n","name"): ANY,
                        ("d","isDisplayed"): ANY,
                        ("i","id"): ANY,
                        ("c","countries"): [ANY]}},
                ("SRPW","serverPopulationWeights"):
                    {ANY: ANY},
                ("SRP","serverPopulationTexts"):
                    {ANY: ANY},
                ("SRVC","customServerTexts"):
                    {ANY: ANY},
                ("SRVT","defaultServerTexts"):
                    {ANY:
                        {("l","name"): ANY,
                        ("d","text"): ANY}},
                ("SR","servers"):
                    {ANY:
                        {("n","name"): ANY,
                        ("d","description"): ANY,
                        ("l","language"): ANY,
                        ("p","populationId"): ANY,
                        ("t","type"): ANY,
                        ("c","communityId"): ANY,
                        ("date","date"): ANY,
                        ("rlng","languages"): [ANY]}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "shortcuts_"):
        descr = {("SH","keyboardShortcuts"):
                    {ANY:
                        {("d","description"): ANY,
                        ("c","categoryId"): ANY,
                        ("k","k"): ANY,
                        ("s","s"): ANY}},
                ("SSC","keyboardShortcutCategories"):
                    {ANY:
                        {("d","description"): ANY,
                        ("i","id"): ANY,
                        ("o","order"): ANY}},
                ("SSK","keyboardShortcutSetKeys"):
                    {ANY:
                        {("k","key"): ANY,
                        ("c","modifier"): ANY,
                        ("o","isNoChat"): ANY,
                        ("s","text"): ANY,
                        ("k2","key2"): ANY,
                        ("c2","modifier2"): ANY,
                        ("o2","isNoChat2"): ANY,
                        ("s2","text2"): ANY,
                        ("d","shortcutName"): ANY}},
                ("SST","keyboardShortcutSets"):
                    {ANY:
                        {("d","description"): ANY,
                        ("i","id"): ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "skills_"):
        descr = {("SK","skills"):
                    {ANY:
                        {("d","description"): ANY,
                        ("j","jobId"): ANY,
                        ("io","interactiveObjectId"): ANY,
                        ("c","criterion"): ANY,
                        ("f","forgemageType"): ANY,
                        ("i","harvestModelId"): ANY,
                        ("cl","craftModelIds"): [ANY]}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "speakingitems_"):
        descr = {("SIM","speakingItemMessages"):
                    {ANY:
                        {("m","text"): ANY,
                        ("s","soundId"): ANY,
                        ("r","speakingItemModelId"): ANY,
                        ("l","speakingItemLevel"): ANY,
                        ("p","probability"): ANY}},
                ("SIT","speakingItemTriggers"):
                    {ANY:
                        {("0","leanMoodMessageIds"): ANY,
                        ("1","satisfiedMoodMessageIds"): ANY,
                        ("2","fatMoodMessageIds"): ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "spells_"):
        descr = {("S","spells"):
                    {ANY:
                        {("n","name"): ANY,
                        ("d","description"): ANY,
                        ("l1","level1"):
                            {(0,"normalHit"):
                                [{(0, "effectType"): ANY,
                                (1, "effectParam1"): ANY,
                                (2, "effectParam2"): ANY,
                                (3, "effectParam3"): ANY,
                                (4, "effectRemainingTurn"): ANY,
                                (5, "effectProbability"): ANY,
                                (6, "effectParam4"): ANY}],
                            (1,"criticalHit"):
                                [{(0, "effectType"): ANY,
                                (1, "effectParam1"): ANY,
                                (2, "effectParam2"): ANY,
                                (3, "effectParam3"): ANY,
                                (4, "effectRemainingTurn"): ANY,
                                (5, "effectProbability"): ANY,
                                (6, "effectParam4"): ANY}],
                            (2,"apCost"): ANY,
                            (3,"minRange"): ANY,
                            (4,"maxRange"): ANY,
                            (5,"criticalHitRate"): ANY,
                            (6,"criticalFailureRate"): ANY,
                            (7,"isLineOnly"): ANY,
                            (8,"hasLineOfSight"): ANY,
                            (9,"needsFreeCell"): ANY,
                            (10,"canBoostRange"): ANY,
                            (11,"raceId"): ANY,
                            (12,"maxByTurn"): ANY,
                            (13,"maxByPlayerByTurn"): ANY,
                            (14,"turnsBetween"): ANY,
                            (15,"zones"): ANY,
                            (16,"requiredStates"): [ANY],
                            (17,"forbiddenStates"): [ANY],
                            (18,"minPlayerLevel"): ANY,
                            (19,"criticalFailureEndsTurn"): ANY},
                        ("l2","level2"):
                            {(0,"normalHit"):
                                [{(0, "effectType"): ANY,
                                (1, "effectParam1"): ANY,
                                (2, "effectParam2"): ANY,
                                (3, "effectParam3"): ANY,
                                (4, "effectRemainingTurn"): ANY,
                                (5, "effectProbability"): ANY,
                                (6, "effectParam4"): ANY}],
                            (1,"criticalHit"):
                                [{(0, "effectType"): ANY,
                                (1, "effectParam1"): ANY,
                                (2, "effectParam2"): ANY,
                                (3, "effectParam3"): ANY,
                                (4, "effectRemainingTurn"): ANY,
                                (5, "effectProbability"): ANY,
                                (6, "effectParam4"): ANY}],
                            (2,"apCost"): ANY,
                            (3,"minRange"): ANY,
                            (4,"maxRange"): ANY,
                            (5,"criticalHitRate"): ANY,
                            (6,"criticalFailureRate"): ANY,
                            (7,"isLineOnly"): ANY,
                            (8,"hasLineOfSight"): ANY,
                            (9,"needsFreeCell"): ANY,
                            (10,"canBoostRange"): ANY,
                            (11,"raceId"): ANY,
                            (12,"maxByTurn"): ANY,
                            (13,"maxByPlayerByTurn"): ANY,
                            (14,"turnsBetween"): ANY,
                            (15,"zones"): ANY,
                            (16,"requiredStates"): [ANY],
                            (17,"forbiddenStates"): [ANY],
                            (18,"minPlayerLevel"): ANY,
                            (19,"criticalFailureEndsTurn"): ANY},
                        ("l3","level3"):
                            {(0,"normalHit"):
                                [{(0, "effectType"): ANY,
                                (1, "effectParam1"): ANY,
                                (2, "effectParam2"): ANY,
                                (3, "effectParam3"): ANY,
                                (4, "effectRemainingTurn"): ANY,
                                (5, "effectProbability"): ANY,
                                (6, "effectParam4"): ANY}],
                            (1,"criticalHit"):
                                [{(0, "effectType"): ANY,
                                (1, "effectParam1"): ANY,
                                (2, "effectParam2"): ANY,
                                (3, "effectParam3"): ANY,
                                (4, "effectRemainingTurn"): ANY,
                                (5, "effectProbability"): ANY,
                                (6, "effectParam4"): ANY}],
                            (2,"apCost"): ANY,
                            (3,"minRange"): ANY,
                            (4,"maxRange"): ANY,
                            (5,"criticalHitRate"): ANY,
                            (6,"criticalFailureRate"): ANY,
                            (7,"isLineOnly"): ANY,
                            (8,"hasLineOfSight"): ANY,
                            (9,"needsFreeCell"): ANY,
                            (10,"canBoostRange"): ANY,
                            (11,"raceId"): ANY,
                            (12,"maxByTurn"): ANY,
                            (13,"maxByPlayerByTurn"): ANY,
                            (14,"turnsBetween"): ANY,
                            (15,"zones"): ANY,
                            (16,"requiredStates"): [ANY],
                            (17,"forbiddenStates"): [ANY],
                            (18,"minPlayerLevel"): ANY,
                            (19,"criticalFailureEndsTurn"): ANY},
                        ("l4","level4"):
                            {(0,"normalHit"):
                                [{(0, "effectType"): ANY,
                                (1, "effectParam1"): ANY,
                                (2, "effectParam2"): ANY,
                                (3, "effectParam3"): ANY,
                                (4, "effectRemainingTurn"): ANY,
                                (5, "effectProbability"): ANY,
                                (6, "effectParam4"): ANY}],
                            (1,"criticalHit"):
                                [{(0, "effectType"): ANY,
                                (1, "effectParam1"): ANY,
                                (2, "effectParam2"): ANY,
                                (3, "effectParam3"): ANY,
                                (4, "effectRemainingTurn"): ANY,
                                (5, "effectProbability"): ANY,
                                (6, "effectParam4"): ANY}],
                            (2,"apCost"): ANY,
                            (3,"minRange"): ANY,
                            (4,"maxRange"): ANY,
                            (5,"criticalHitRate"): ANY,
                            (6,"criticalFailureRate"): ANY,
                            (7,"isLineOnly"): ANY,
                            (8,"hasLineOfSight"): ANY,
                            (9,"needsFreeCell"): ANY,
                            (10,"canBoostRange"): ANY,
                            (11,"raceId"): ANY,
                            (12,"maxByTurn"): ANY,
                            (13,"maxByPlayerByTurn"): ANY,
                            (14,"turnsBetween"): ANY,
                            (15,"zones"): ANY,
                            (16,"requiredStates"): [ANY],
                            (17,"forbiddenStates"): [ANY],
                            (18,"minPlayerLevel"): ANY,
                            (19,"criticalFailureEndsTurn"): ANY},
                        ("l5","level5"):
                            {(0,"normalHit"):
                                [{(0, "effectType"): ANY,
                                (1, "effectParam1"): ANY,
                                (2, "effectParam2"): ANY,
                                (3, "effectParam3"): ANY,
                                (4, "effectRemainingTurn"): ANY,
                                (5, "effectProbability"): ANY,
                                (6, "effectParam4"): ANY}],
                            (1,"criticalHit"):
                                [{(0, "effectType"): ANY,
                                (1, "effectParam1"): ANY,
                                (2, "effectParam2"): ANY,
                                (3, "effectParam3"): ANY,
                                (4, "effectRemainingTurn"): ANY,
                                (5, "effectProbability"): ANY,
                                (6, "effectParam4"): ANY}],
                            (2,"apCost"): ANY,
                            (3,"minRange"): ANY,
                            (4,"maxRange"): ANY,
                            (5,"criticalHitRate"): ANY,
                            (6,"criticalFailureRate"): ANY,
                            (7,"isLineOnly"): ANY,
                            (8,"hasLineOfSight"): ANY,
                            (9,"needsFreeCell"): ANY,
                            (10,"canBoostRange"): ANY,
                            (11,"raceId"): ANY,
                            (12,"maxByTurn"): ANY,
                            (13,"maxByPlayerByTurn"): ANY,
                            (14,"turnsBetween"): ANY,
                            (15,"zones"): ANY,
                            (16,"requiredStates"): [ANY],
                            (17,"forbiddenStates"): [ANY],
                            (18,"minPlayerLevel"): ANY,
                            (19,"criticalFailureEndsTurn"): ANY},
                        ("l6","level6"):
                            {(0,"normalHit"):
                                [{(0, "effectType"): ANY,
                                (1, "effectParam1"): ANY,
                                (2, "effectParam2"): ANY,
                                (3, "effectParam3"): ANY,
                                (4, "effectRemainingTurn"): ANY,
                                (5, "effectProbability"): ANY,
                                (6, "effectParam4"): ANY}],
                            (1,"criticalHit"):
                                [{(0, "effectType"): ANY,
                                (1, "effectParam1"): ANY,
                                (2, "effectParam2"): ANY,
                                (3, "effectParam3"): ANY,
                                (4, "effectRemainingTurn"): ANY,
                                (5, "effectProbability"): ANY,
                                (6, "effectParam4"): ANY}],
                            (2,"apCost"): ANY,
                            (3,"minRange"): ANY,
                            (4,"maxRange"): ANY,
                            (5,"criticalHitRate"): ANY,
                            (6,"criticalFailureRate"): ANY,
                            (7,"isLineOnly"): ANY,
                            (8,"hasLineOfSight"): ANY,
                            (9,"needsFreeCell"): ANY,
                            (10,"canBoostRange"): ANY,
                            (11,"raceId"): ANY,
                            (12,"maxByTurn"): ANY,
                            (13,"maxByPlayerByTurn"): ANY,
                            (14,"turnsBetween"): ANY,
                            (15,"zones"): ANY,
                            (16,"requiredStates"): [ANY],
                            (17,"forbiddenStates"): [ANY],
                            (18,"minPlayerLevel"): ANY,
                            (19,"criticalFailureEndsTurn"): ANY}}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "states_"):
        descr = {("ST","states"):
                    {ANY:
                        {("n","name"): ANY,
                        ("p","p"): ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "subtitles_"):
        descr = {("SUB","subtitles"):
                    {ANY:
                        {ANY: ANY}}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "timezones_"):
        descr = {("T","timezone"):
                    {("hpd","hoursPerDay"): ANY,
                    ("m","months"):
                        [{(0,"minYearDay"): ANY,
                        (1,"name"): ANY}],
                    ("mspd","millisecondsPerDay"): ANY,
                    ("tz","lightTimes"):
                        [{(0,"minTime"): ANY,
                        (1,"maxTime"): ANY,
                        (2,"colors"):
                            {("ra","redPercent"): ANY,
                            ("rb","redOffset"): ANY,
                            ("ga","greenPercent"): ANY,
                            ("gb","greenOffset"): ANY,
                            ("ba","bluePercent"): ANY,
                            ("bb","blueOffset"): ANY}}],
                    ("z","yearOffset"): ANY}}
    elif path.startswith("lang" + os.path.sep + "swf" + os.path.sep + "titles_"):
        descr = {("PT","titles"):
                    {ANY:
                        {("t","text"): ANY,
                        ("c","color"): ANY,
                        ("pt","type"): ANY}}}
    elif path.startswith("maps" + os.path.sep):
        descr = {"ambianceId": ANY,
                ("bOutdoor","isOutdoor"): ANY,
                ("backgroundNum","backgroundId"): ANY,
                "capabilities": ANY,
                "height": ANY,
                "id": ANY,
                ("mapData","encryptedData"): ANY,
                "musicId": ANY,
                "width": ANY}
    elif path.startswith("tutorials" + os.path.sep):
        descr = {("actions","blocks"): ANY,
                "canCancel": ANY,
                ("mapID","mapId"): ANY,
                ("rootBlocID","rootBlockId"): ANY,
                ("rootExitBlocID","rootExitBlockId"): ANY}
    if descr is not None:
        data = json.loads(content)
        data = renameData(data, descr)
        content = json.dumps(data, ensure_ascii=False)
    return content

def renameJson():
    for root, dirs, files in os.walk(IN_FOLDER):
        for filename in files:
            if not filename.endswith(".json"):
                continue
            filePath = os.path.join(root, filename)
            relPath = os.path.splitext(os.path.sep.join(filePath.split(os.path.sep)[1:]))[0]
            renamedFilePath = os.path.join(OUT_FOLDER, relPath + ".json")
            renamedDirPath = os.path.dirname(renamedFilePath)
            ensureDirs([renamedDirPath])
            with io.open(filePath, "r", encoding="utf-8") as i:
                content = i.read()
            content = cleanContent(content)
            content = renameContent(content, relPath)
            with io.open(renamedFilePath, "w", encoding="utf-8") as o:
                o.write(content)

cleanPaths([OUT_FOLDER])
ensureDirs([OUT_FOLDER])
renameJson()