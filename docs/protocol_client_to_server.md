# Protocol: Client -> Server

## Index

* [Network message index](#network-message-index)
* [Syntax](#syntax)
* [Common](#common)
* [Network messages](#network-messages)

## Network message index

| Account                                                     | Basic                                                           | Conquest                                                          | Npc                                                 | Exchange                                                            | Friend                                                              | Game                                                          | Info                              | Job                             | Lock                          | Item                                          | Group                                                       | Quest                         | Mount                                                     | Spell                         | Tutorial                          | Transport                                         | Chat                                          | Document                              | Emote                                           | Fight                                                                       | Guild                                                 | House                                             | Enemy                         | Server                          |
|-------------------------------------------------------------|-----------------------------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------|-----------------------------------|---------------------------------|-------------------------------|-----------------------------------------------|-------------------------------------------------------------|-------------------------------|-----------------------------------------------------------|-------------------------------|-----------------------------------|---------------------------------------------------|-----------------------------------------------|---------------------------------------|-------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------|---------------------------------------------------|-------------------------------|---------------------------------|
| [ClientVersion](#clientversion)                             | [AdminCommand](#admincommand)                                   | [GetAlignedConquestAreaModifier](#getalignedconquestareamodifier) | [StartNpcDialog](#startnpcdialog)                   | [AcceptExchange](#acceptexchange)                                   | [AddFriend](#addfriend)                                             | [StartGameAction](#startgameaction)                           | [DisplayArea](#displayarea) | [SetJobOptions](#setjoboptions) | [LockKey](#lockkey)           | [UseItem](#useitem)                           | [AcceptGroupInvitation](#acceptgroupinvitation)             | [GetQuestList](#getquestlist) | [BuyPaddock](#buypaddock)                                 | [UpgradeCharacterSpell](#upgradecharacterspell) | [FinishTutorial](#finishtutorial) | [UsePortalTransport](#useportaltransport)                           | [SubscribeChatChannel](#subscribechatchannel) | [CanCloseDocument](#canclosedocument) | [SetCharacterDirection](#setcharacterdirection) | [GetFightDetails](#getfightdetails)                                         | [UpgradeTaxCollectorStat](#upgradetaxcollectorstat)   | [BuyHouse](#buyhouse)                             | [AddEnemy](#addenemy)         | [Ping](#ping)                   |
| [AccountLogin](#accountlogin)                               | [BasicCheckFileResponse](#basiccheckfileresponse)               | [JoinPrismDefense](#joinprismdefense)                             | [SelectNpcDialogResponse](#selectnpcdialogresponse) | [ExchangeBuy](#exchangebuy)                                         | [RemoveFriend](#removefriend)                                       | [StartGame](#startgame)                                       |                                   |                                 | [CanCloseLock](#cancloselock) | [DropItem](#dropitem)                         | [FollowGroupMember](#followgroupmember)             | [GetQuestStep](#getqueststep) | [SterilizeMount](#sterilizemount)                         | [ForgetSpell](#forgetspell)   |                                   | [CanClosePortalTransport](#cancloseportaltransport)                 |                                               |                                       | [UseEmote](#useemote)                           | [ToggleNeedHelpFightOption](#toggleneedhelpfightoption)                     | [CreateGuild](#createguild)                           | [GetGuildHouseOptions](#getguildhouseoptions)     | [RemoveEnemy](#removeenemy)   | [QuickPing](#quickping)         |
| [ChooseAccountNickname](#chooseaccountnickname)             | [GetBasicDate](#getbasicdate)                                   | [SwapWithPrismDefenseDefender](#swapwithprismdefensedefender)     | [CanCloseNpcDialog](#canclosenpcdialog)             | [AuctionHouseBuy](#auctionhousebuy)                                 | [JoinSpouse](#joinspouse)                                           | [GetMapDetails](#getmapdetails)                               |                                   |                                 |                               | [MoveInventoryItem](#moveinventoryitem)       | [FollowGroupMemberByEveryone](#followgroupmemberbyeveryone) |                               | [GetCertificateMountDetails](#getcertificatemountdetails) | [MoveSpell](#movespell)       |                                   | [UsePrismTransport](#useprismtransport)           |                                               |                                       |                                                 | [GetFightList](#getfightlist)                                               | [RemoveTaxCollector](#removetaxcollector)             | [SetGuildHouseOptions](#setguildhouseoptions)     | [GetEnemyList](#getenemylist) | [RPingResponse](#rpingresponse) |
| [CreateCharacter](#createcharacter)                         | [BasicSanctionMe](#basicsanctionme)                             | [LeavePrismDefense](#leaveprismdefense)                           |                                                     | [GetAuctionHouseItemAveragePrice](#getauctionhouseitemaverageprice) | [FollowSpouse](#followspouse)                                       | [ReleaseCharacterSoul](#releasecharactersoul)                 |                                   |                                 |                               | [DestroyItem](#destroyitem)                   | [InviteInGroup](#inviteingroup)                             |                               | [ReleaseMount](#releasemount)                             |                               |                                   | [UseCityTransport](#usecitytransport)             |                                               |                                       |                                                 | [ToggleCantJoinFightOption](#togglecantjoinfightoption)                     | [AddTaxCollector](#addtaxcollector)                   | [AddGuildHouse](#addguildhouse)                   |                               |                                 |
| [UpgradeCharacterStat](#upgradecharacterstat)               | [ChatMessage](#chatmessage)                                     | [GetPrismDefenseDetails](#getprismdefensedetails)                 |                                                     | [SearchAuctionHouse](#searchauctionhouse)                           | [JoinNoviceFriend](#joinnovicefriend)                               | [GetGameDetails](#getgamedetails)                             |                                   |                                 |                               | [FeedLivingItem](#feedlivingitem)             | [RefuseGroupInvitation](#refusegroupinvitation)             |                               | [RenameMount](#renamemount)                               |                               |                                   | [CanCloseCityTransport](#canclosecitytransport)   |                                               |                                       |                                                 | [ToggleCantJoinIfNotGroupFightOption](#togglecantjoinifnotgroupfightoption) | [GetTaxCollectorStats](#gettaxcollectorstats)     | [RemoveGuildHouse](#removeguildhouse)             |                               |                                 |
| [DeleteCharacter](#deletecharacter)                         | [KickOfflineCharacterFromHouse](#kickofflinecharacterfromhouse) | [ClosePrismDefense](#closeprismdefense)                           |                                                     | [GetAuctionHouseItemList](#getauctionhouseitemlist)                 | [GetFriendList](#getfriendlist)                                     | [StopGameAction](#stopgameaction)                             |                                   |                                 |                               | [SetLivingItemSkin](#setlivingitemskin)       | [KickGroupMember](#kickgroupmember)                                   |                               | [RemovePaddockItem](#removepaddockitem)                   |                               |                                   | [CanClosePrismTransport](#cancloseprismtransport) |                                               |                                       |                                                 | [ToggleCantWatchFightOption](#togglecantwatchfightoption)                   | [GetGuildPaddockList](#getguildpaddocklist)           | [KickCharacterFromHouse](#kickcharacterfromhouse) |                               |                                 |
| [StoreService [RETRO]](#storeservice-[retro])               | [ReportChatMessage](#reportchatmessage)                         | [GetConquestAreaList](#getconquestarealist)                       |                                                     | [GetAuctionHouseEntryList](#getauctionhouseentrylist)               | [SetNotifyFriendConnectionOption](#setnotifyfriendconnectionoption) | [AcknowledgeGameAction](#acknowledgegameaction)               |                                   |                                 |                               | [DissociateLivingItem](#dissociatelivingitem) | [LocateGroup](#locategroup)                                 |                               | [GetPaddockMountDetails](#getpaddockmountdetails)         |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [GetGuildXp](#getguildxp)                             | [SellHouse](#sellhouse)                           |                               |                                 |
| [SearchFriendServer](#searchfriendserver)                   | [UseSmiley](#usesmiley)                                         | [CloseConquestArea](#closeconquestarea)                           |                                                     | [GetJobCraftspersonList](#getjobcraftspersonlist)                   |                                                                     | [GetDisablePvpLostHonor](#getdisablepvplosthonor)             |                                   |                                 |                               |                                               |                                                             |                               | [ToggleRideMount](#toggleridemount)                       |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [GetGuildHouseList](#getguildhouselist)               | [CanCloseBuyHouse](#canclosebuyhouse)             |                               |                                 |
| [AttributeGiftToCharacter](#attributegifttocharacter)       | [BasicWhoIs](#basicwhois)                                       | [GetConquestBalance](#getconquestbalance)                         |                                                     | [ValidateExchange](#validateexchange)                               |                                                                     | [SetPvpState](#setpvpstate)                                   |                                   |                                 |                               |                                               |                                                             |                               | [SellPaddock](#sellpaddock)                               |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [GetGuildMemberList](#getguildmemberlist)             |                                                   |                               |                                 |
| [GetCharacterList](#getcharacterlist)                       | [BasicToggleAway](#basictoggleaway)                             |                                                                   |                                                     | [RedoCraft](#redocraft)                                             |                                                                     | [KickFighter](#kickfighter)                                     |                                   |                                 |                               |                                               |                                                             |                               | [CanCloseBuyPaddock](#canclosebuypaddock)                 |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [GetTaxCollectorList](#gettaxcollectorlist)           |                                                   |                               |                                 |
| [ValidateMigrantCharacter](#validatemigrantcharacter)       | [BasicToggleInvisible](#basictoggleinvisible)                   |                                                                   |                                                     | [SetExchangeMoney](#setexchangemoney)                               |                                                                     | [ValidateFight](#validatefight)                               |                                   |                                 |                               |                                               |                                                             |                               | [SetMountXp](#setmountxp)                                 |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [CloseTaxCollector](#closetaxcollector)               |                                                   |                               |                                 |
| [DeleteMigrantCharacter](#deletemigrantcharacter)           | [AdminTeleport](#adminteleport)                                 |                                                                   |                                                     | [UpdateExchangeItemList](#updateexchangeitemlist)                   |                                                                     | [AcknowledgeFightTurnResponse](#acknowledgefightturnresponse) |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [RefuseGuildInvitation](#refuseguildinvitation)       |                                                   |                               |                                 |
| [CanValidateMigrantCharacter](#canvalidatemigrantcharacter) | [BasicAveragePing](#basicaverageping)                           |                                                                   |                                                     | [StartCraftLoop](#startcraftloop)                                   |                                                                     | [FlagFightChallengeTarget](#flagfightchallengetarget)         |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [AcceptGuildInvitation](#acceptguildinvitation)       |                                                   |                               |                                 |
| [GetRandomCharacterName](#getrandomcharactername)           |                                                                 |                                                                   |                                                     | [StopCraftLoop](#stopcraftloop)                                     |                                                                     | [FlagFightCell](#flagfightcell)                               |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [InviteInGuild](#inviteinguild)                       |                                                   |                               |                                 |
| [ResetCharacter](#resetcharacter)                           |                                                                 |                                                                   |                                                     | [UpdatePaymentContentList](#updatepaymentcontentlist)                             |                                                                     | [SetFightStartPosition](#setfightstartposition)               |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [KickGuildMember](#kickguildmember)                   |                                                   |                               |                                 |
| [SelectCharacter](#selectcharacter)                         |                                                                 |                                                                   |                                                     | [SwitchToOfflineCharacterShop](#switchtoofflinecharactershop)       |                                                                     | [FinishFightTurn](#finishfightturn)                           |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [SetGuildMemberOptions](#setguildmemberoptions)         |                                                   |                               |                                 |
| [ClientTicket](#clientticket)                               |                                                                 |                                                                   |                                                     | [RequestExchange](#requestexchange)                                 |                                                                     |                                                               |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [JoinTaxCollectorDefense](#jointaxcollectordefense)   |                                                   |                               |                                 |
| [GetRegionalVersion](#getregionalversion)                   |                                                                 |                                                                   |                                                     | [NpcExchangeSell](#npcexchangesell)                                 |                                                                     |                                                               |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [LeaveTaxCollectorDefense](#leavetaxcollectordefense) |                                                   |                               |                                 |
| [SelectServer](#selectserver)                               |                                                                 |                                                                   |                                                     | [CanLeaveExchange](#canleaveexchange)                               |                                                                     |                                                               |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [CanCloseCreateGuild](#canclosecreateguild)           |                                                   |                               |                                 |
| [GetQueuePosition](#getqueueposition)                       |                                                                 |                                                                   |                                                     | [SetCraftPublicModeOption](#setcraftpublicmodeoption)               |                                                                     |                                                               |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [UpgradeTaxCollectorSpell](#upgradetaxcollectorspell) |                                                   |                               |                                 |
| [GetGiftList](#getgiftlist)                                 |                                                                 |                                                                   |                                                     | [MovePaddockMountToStable](#movepaddockmounttostable)               |                                                                     |                                                               |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [TeleportToGuildPaddock](#teleporttoguildpaddock)     |                                                   |                               |                                 |
| [ClientId](#clientid)                                       |                                                                 |                                                                   |                                                     | [MoveStableMountToPaddock](#movestablemounttopaddock)               |                                                                     |                                                               |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             | [TeleportToGuildHouse](#teleporttoguildhouse)         |                                                   |                               |                                 |
| [UseClientKey](#useclientkey)                               |                                                                 |                                                                   |                                                     | [GetOfflineCharacterShopTax](#getofflinecharactershoptax)           |                                                                     |                                                               |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             |                                                       |                                                   |                               |                                 |
| [RescueCharacter](#rescuecharacter)                         |                                                                 |                                                                   |                                                     | [MoveCertificateMountToStable](#movecertificatemounttostable)       |                                                                     |                                                               |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             |                                                       |                                                   |                               |                                 |
| [GetOwnServerList](#getownserverlist)                       |                                                                 |                                                                   |                                                     | [MoveStableMountToCertificate](#movestablemounttocertificate)       |                                                                     |                                                               |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             |                                                       |                                                   |                               |                                 |
|                                                             |                                                                 |                                                                   |                                                     | [MoveStableMountToEquipped](#movestablemounttoequipped)             |                                                                     |                                                               |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             |                                                       |                                                   |                               |                                 |
|                                                             |                                                                 |                                                                   |                                                     | [MoveEquippedMountToStable](#moveequippedmounttostable)             |                                                                     |                                                               |                                   |                                 |                               |                                               |                                                             |                               |                                                           |                               |                                   |                                                   |                                               |                                       |                                                 |                                                                             |                                                       |                                                   |                               |                                 |

## Syntax

```js
"a" = a IS TEXT
```

```js
a = a IS VARIABLE
```

```js
a b = JOIN a AND b
```

```js
(a | b) = a OR b
```

```js
(a -> b) = a OR ... OR b
```

```js
{a} = a IS OPTIONAL
```

```js
[a, b] = JOIN a ELEMENTS WITH b
```

```js
<a> = a IS AN OPERATION
```

```js
<a, b> = CONVERT a TO BASE b
```

```js
a(b) = a IS FUNCTION
```

## Common

#### Footer

```js
"\n" "\0"
```

#### Parameters

```js
directionId = (DIRECTION_EAST | DIRECTION_SOUTH_EAST | DIRECTION_SOUTH | DIRECTION_SOUTH_WEST | DIRECTION_WEST | DIRECTION_NORTH_WEST | DIRECTION_NORTH | DIRECTION_NORTH_EAST)
```

```js
livingItem.position = (ITEM_POSITION_AMULET | ITEM_POSITION_RINGS | ITEM_POSITION_HAT | ITEM_POSITION_CLOAK)
```

#### Constants

```js
EMPTY = ""
```

```js
(ADD | ENABLE) = "+"
(REMOVE | DISABLE) = "-"
```

```js
DIRECTION_EAST = 0
DIRECTION_SOUTH_EAST = 1
DIRECTION_SOUTH = 2
DIRECTION_SOUTH_WEST = 3
DIRECTION_WEST = 4
DIRECTION_NORTH_WEST = 5
DIRECTION_NORTH = 6
DIRECTION_NORTH_EAST = 7
```

```js
EXCHANGE_NPC_SHOP = 0
EXCHANGE_CHARACTER_EXCHANGE = 1
EXCHANGE_NPC_EXCHANGE = 2
EXCHANGE_OFFLINE_CHARACTER_SHOP_BUY = 4
EXCHANGE_OFFLINE_CHARACTER_SHOP_SELL = 6
EXCHANGE_TAX_COLLECTOR_STORAGE = 8
EXCHANGE_NPC_EXCHANGE_PET = 9
EXCHANGE_AUCTION_HOUSE_SELL = 10
EXCHANGE_AUCTION_HOUSE_BUY = 11
EXCHANGE_MULTI_CRAFT_INVITE = 12
EXCHANGE_MULTI_CRAFT_ASK = 13
EXCHANGE_MOUNT_STORAGE = 15
EXCHANGE_NPC_RESURRECT_PET = 17
EXCHANGE_NPC_EXCHANGE_MOUNT = 18
```

```js
CHANNEL_PUBLIC = "*"
CHANNEL_TEAM = "#"
CHANNEL_PARTY = "$"
CHANNEL_GUILD = "%"
CHANNEL_ALIGNMENT = "!"
CHANNEL_RECRUITMENT = "?"
CHANNEL_TRADING = ":"
CHANNEL_NOVICE = "^"
CHANNEL_ADMIN = "@"
```

```js
ITEM_POSITION_AMULET = 0
ITEM_POSITION_RINGS = (2 | 4)
ITEM_POSITION_HAT = 6
ITEM_POSITION_CLOAK = 7
```

## Network messages

### ClientVersion

#### Header

```js
EMPTY
```

#### Body

```js
version.major "." version.minor "." version.patch {"." version.beta}
```

---

### AccountLogin

#### Header

```js
EMPTY
```

#### Body

```js
account.login "\n" "#1" ENCRYPT_PASSWORD(account.password, connectionKey)
```

```js
account.login "\n" "#2" MD5(MD5(account.password) connectionKey)
```

#### Functions

```js
function ENCRYPT_PASSWORD(pwd, key) {
    var pwdByteDivi = 16;
    var array = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_";
    var pwdEncrypted = "";
    for (var pwdIndex = 0; pwdIndex < pwd.length; pwdIndex++) {
        var pwdByte = pwd.charCodeAt(pwdIndex);
        var keyByte = key.charCodeAt(pwdIndex);
        var pwdByteQuot = Math.floor(pwdByte / pwdByteDivi);
        var pwdByteRest = pwdByte % pwdByteDivi;
        pwdEncrypted += array[(pwdByteQuot + keyByte) % array.length] + array[(pwdByteRest + keyByte) % array.length];
    }
    return pwdEncrypted;
}
```

---

### ChooseAccountNickname

#### Header

```js
EMPTY
```

#### Body

```js
account.nickname
```

---

### CreateCharacter

#### Header

```js
"AA"
```

#### Body

```js
character.name "|" character.raceId "|" character.isFemale "|" (-1 | character.color1) "|" (-1 | character.color2) "|" (-1 | character.color3)
```

---

### UpgradeCharacterStat

#### Header

```js
"AB"
```

#### Body

```js
(CHARACTER_STAT_STRENGTH | CHARACTER_STAT_VITALITY | CHARACTER_STAT_WISDOM | CHARACTER_STAT_CHANCE | CHARACTER_STAT_AGILITY | CHARACTER_STAT_INTELLIGENCE)
```

#### Constants

```js
CHARACTER_STAT_LIFE_POINTS = 0
CHARACTER_STAT_ACTION_POINTS = 1
CHARACTER_STAT_MONEY = 2
CHARACTER_STAT_STAT_POINTS = 3
CHARACTER_STAT_SPELL_POINTS = 4
CHARACTER_STAT_LEVEL = 5
CHARACTER_STAT_STRENGTH = 10
CHARACTER_STAT_VITALITY = 11
CHARACTER_STAT_WISDOM = 12
CHARACTER_STAT_CHANCE = 13
CHARACTER_STAT_AGILITY = 14
CHARACTER_STAT_INTELLIGENCE = 15
CHARACTER_STAT_DAMAGE_BONUS = 16
CHARACTER_STAT_DAMAGE_FACTOR_BONUS = 17
CHARACTER_STAT_CRITICAL_HIT_BONUS = 18
CHARACTER_STAT_RANGE = 19
CHARACTER_STAT_MAGICAL_RESISTANCE = 20
CHARACTER_STAT_PHYSICAL_RESISTANCE = 21
CHARACTER_STAT_EXPERIENCE = 22
CHARACTER_STAT_MOVEMENT_POINTS = 23
CHARACTER_STAT_INVISIBILITY = 24
CHARACTER_STAT_DAMAGE_PERCENT_BONUS = 25
CHARACTER_STAT_MAX_SUMMONED_COUNT = 26
CHARACTER_STAT_DODGE_AP_LOSS = 27
CHARACTER_STAT_DODGE_MP_LOSS = 28
CHARACTER_STAT_ENERGY_POINTS = 29
CHARACTER_STAT_ALIGNMENT = 30
CHARACTER_STAT_WEAPON_DAMAGE_PERCENT_BONUS = 31
CHARACTER_STAT_PHYSICAL_DAMAGE_BONUS = 32
CHARACTER_STAT_EARTH_RESISTANCE_PERCENT = 33
CHARACTER_STAT_FIRE_RESISTANCE_PERCENT = 34
CHARACTER_STAT_WATER_RESISTANCE_PERCENT = 35
CHARACTER_STAT_AIR_RESISTANCE_PERCENT = 36
CHARACTER_STAT_NEUTRAL_RESISTANCE_PERCENT = 37
CHARACTER_STAT_GFX = 38
CHARACTER_STAT_CRITICAL_FAILURE_BONUS = 39
CHARACTER_STAT_INITIATIVE = 44
CHARACTER_STAT_PROSPECTING = 48
CHARACTER_STAT_STATE = 71
```

---

### DeleteCharacter

#### Header

```js
"AD"
```

#### Body

```js
character.id "|" ESCAPE(account.secretAnswer)
```

---

### StoreService [RETRO]

#### Header

```js
"AE"
```

#### Body

```js
EDIT_CHARACTER_COLORS (-1 | character.color1) "|" (-1 | character.color2) "|" (-1 | character.color3)
```

```
MIMIBIOTE ((DESTROY "|" item.id) | (ASSOCIATE "|" statItem.id "|" skinItem.id))
```

```js
EDIT_CHARACTER_NAME character.name
```

#### Constants

```js
EDIT_CHARACTER_COLORS = "c"
MIMIBIOTE = "i"
EDIT_CHARACTER_NAME = "n"
```

```js
DESTROY = 0
ASSOCIATE = 1
```

---

### SearchFriendServer

#### Header

```js
"AF"
```

#### Body

```js
account.nickname
```

---

### AttributeGiftToCharacter

#### Header

```js
"AG"
```

#### Body

```js
gift.id "|" character.id
```

---

### GetCharacterList

#### Header

```js
"AL"
```

#### Body

```js
{FORCE}
```

#### Constants

```js
FORCE = "f"
```

---

### ValidateMigrantCharacter

#### Header

```js
"AM"
```

#### Body

```js
character.id ";" character.name
```

---

### DeleteMigrantCharacter

#### Header

```js
"AM-"
```

#### Body

```js
character.id
```

---

### CanValidateMigrantCharacter

#### Header

```js
"AM?"
```

#### Body

```js
character.id ";" character.name
```

---

### GetRandomCharacterName

#### Header

```js
"AP"
```

#### Body

```js
EMPTY
```

---

### ResetCharacter

#### Header

```js
"AR"
```

#### Body

```js
character.id
```

---

### SelectCharacter

#### Header

```js
"AS"
```

#### Body

```js
character.id
```

---

### ClientTicket

#### Header

```js
"AT"
```

#### Body

```js
ticket
```

---

### GetRegionalVersion

#### Header

```js
"AV"
```

#### Body

```js
EMPTY
```

---

### SelectServer

#### Header

```js
"AX"
```

#### Body

```js
server.id
```

---

### GetQueuePosition

#### Header

```js
"Af"
```

#### Body

```js
EMPTY
```

---

### GetGiftList

#### Header

```js
"Ag"
```

#### Body

```js
language
```

---

### ClientId

#### Header

```js
"Ai"
```

#### Body

```js
clientId
```

---

### UseClientKey

#### Header

```js
"Ak"
```

#### Body

```js
<keyId, 16>
```

#### Parameters

```js
keyId = (0 -> 15)
```

---

### RescueCharacter

#### Header

```js
"Ar"
```

#### Body

```js
ticket {"|" (IN_NOT_VALIDATED_FIGHT | IN_VALIDATED_FIGHT)}
```

#### Constants

```js
IN_NOT_VALIDATED_FIGHT = 0
IN_VALIDATED_FIGHT = 1
```

---

### GetOwnServerList

#### Header

```js
"Ax"
```

#### Body

```js
EMPTY
```

---

### AdminCommand

#### Header

```js
"BA"
```

#### Body

```js
{"!"} "getitem" " " item.id " " item.quantity
```

```js
"join" " " character.name
```

```js
command
```

---

### BasicCheckFileResponse

#### Header

```js
"BC"
```

#### Body

```js
checkId ";" (FAILED | fileSizeInBytes)
```

#### Constants

```js
FAILED = -1
```

---

### GetBasicDate

#### Header

```js
"BD"
```

#### Body

```js
EMPTY
```

---

### BasicSanctionMe

#### Header

```js
"BK"
```

#### Body

```js
censoredWord.weight "|" censoredWord.id
```

---

### ChatMessage

#### Header

```js
"BM"
```

#### Body

```js
(CHANNEL_PUBLIC | CHANNEL_TEAM | CHANNEL_GUILD | CHANNEL_PARTY | CHANNEL_ALIGNMENT | CHANNEL_RECRUITMENT | CHANNEL_TRADING | CHANNEL_NOVICE | CHANNEL_ADMIN | CHANNEL_MEETING | character.name) "|" chatText "|" [item.modelId "!" ("." | item.effects), "!"]
```

#### Parameters

```js
chatText = [(text | ("°" itemIndex)), EMPTY]
```

```js
item.effects = [<effect.typeId, 16> "#" (0 | <effect.param1, 16>) "#" (0 | <effect.param2, 16>) "#" (0 | <effect.param3, 16>) "#" effect.param4, ","]
```

#### Constants

```js
CHANNEL_MEETING = "¤"
```

---

### KickOfflineCharacterFromHouse

#### Header

```js
"BQ"
```

#### Body

```js
offlineCharacter.cellId
```

---

### ReportChatMessage

#### Header

```js
"BR"
```

#### Body

```js
character.name "|" message.id "|" message.text "|" reasonId
```

---

### UseSmiley

#### Header

```js
"BS"
```

#### Body

```js
smiley.id
```

#### Parameters

```js
smiley.id = (1 -> 15)
```

---

### BasicWhoIs

#### Header

```js
"BW"
```

#### Body

```js
{(character.name | "*" account.nickname)}
```

---

### BasicToggleAway

#### Header

```js
"BYA"
```

#### Body

```js
EMPTY
```

---

### BasicToggleInvisible

#### Header

```js
"BYI"
```

#### Body

```js
EMPTY
```

---

### AdminTeleport

#### Header

```js
"BaM"
```

#### Body

```js
map.x "," map.y
```

---

### BasicAveragePing

#### Header

```js
"Bp"
```

#### Body

```js
averagePingInMilliseconds "|" pingCount "|" maxPingCount
```

---

### GetAlignedConquestAreaModifier

#### Header

```js
"CB"
```

#### Body

```js
EMPTY
```

---

### JoinPrismDefense

#### Header

```js
"CFJ"
```

#### Body

```js
EMPTY
```

---

### SwapWithPrismDefenseDefender

#### Header

```js
"CFS"
```

#### Body

```js
defender.id
```

---

### LeavePrismDefense

#### Header

```js
"CFV"
```

#### Body

```js
EMPTY
```

---

### GetPrismDefenseDetails

#### Header

```js
"CIJ"
```

#### Body

```js
EMPTY
```

---

### ClosePrismDefense

#### Header

```js
"CIV"
```

#### Body

```js
EMPTY
```

---

### GetConquestAreaList

#### Header

```js
"CWJ"
```

#### Body

```js
EMPTY
```

---

### CloseConquestArea

#### Header

```js
"CWV"
```

#### Body

```js
EMPTY
```

---

### GetConquestBalance

#### Header

```js
"Cb"
```

#### Body

```js
EMPTY
```

---

### StartNpcDialog

#### Header

```js
"DC"
```

#### Body

```js
npc.id
```

---

### SelectNpcDialogResponse

#### Header

```js
"DR"
```

#### Body

```js
question.id "|" response.id
```

---

### CanCloseNpcDialog

#### Header

```js
"DV"
```

#### Body

```js
EMPTY
```

---

### AcceptExchange

#### Header

```js
"EA"
```

#### Body

```js
EMPTY
```

---

### ExchangeBuy

#### Header

```js
"EB"
```

#### Body

EXCHANGE_NPC_SHOP:

```js
item.modelId "|" item.quantity
```

EXCHANGE_OFFLINE_CHARACTER_SHOP_BUY:

```js
item.id "|" item.quantity
```

---

### AuctionHouseBuy

#### Header

```js
"EHB"
```

#### Body

```js
entry.id "|" (LOT_1 | LOT_2 | LOT_3) "|" lotPrice
```

#### Constants

```js
LOT_1 = 1
LOT_2 = 2
LOT_3 = 3
```

---

### GetAuctionHouseItemAveragePrice

#### Header

```js
"EHP"
```

#### Body

```js
item.modelId
```

---

### SearchAuctionHouse

#### Header

```js
"EHS"
```

#### Body

```js
item.typeId "|" item.modelId
```

---

### GetAuctionHouseItemList

#### Header

```js
"EHT"
```

#### Body

```js
item.typeId
```

---

### GetAuctionHouseEntryList

#### Header

```js
"EHl"
```

#### Body

```js
item.modelId
```

---

### GetJobCraftspersonList

#### Header

```js
"EJF"
```

#### Body

```js
job.id
```

---

### ValidateExchange

#### Header

```js
"EK"
```

#### Body

```js
EMPTY
```

---

### RedoCraft

#### Header

```js
"EL"
```

#### Body

```js
EMPTY
```

---

### SetExchangeMoney

#### Header

```js
"EMG"
```

#### Body

```js
moneyAmount
```

---

### UpdateExchangeItemList

#### Header

```js
"EMO"
```

#### Body

```js
[(ADD | REMOVE) item.id "|" item.quantity {"|" item.price}, EMPTY]
```

---

### StartCraftLoop

#### Header

```js
"EMR"
```

#### Body

```js
itemCount
```

---

### StopCraftLoop

#### Header

```js
"EMr"
```

#### Body

```js
EMPTY
```

---

### UpdatePaymentContentList

#### Header

```js
"EP"
```

#### Body

```js
(PAYMENT_BASE | PAYMENT_SUCCESS_BONUS) EXCHANGE_ITEM (ADD | REMOVE) item.id "|" item.quantity {"|" item.price}
```

```js
(PAYMENT_BASE | PAYMENT_SUCCESS_BONUS) EXCHANGE_MONEY moneyAmount
```

#### Constants

```js
PAYMENT_BASE = 1
PAYMENT_SUCCESS_BONUS = 2
```

```js
EXCHANGE_ITEM = "O"
EXCHANGE_MONEY = "G"
```

---

### SwitchToOfflineCharacterShop

#### Header

```js
"EQ"
```

#### Body

```js
EMPTY
```

---

### RequestExchange

#### Header

```js
"ER"
```

#### Body

```js
(EXCHANGE_NPC_SHOP | EXCHANGE_NPC_EXCHANGE | EXCHANGE_NPC_EXCHANGE_PET | EXCHANGE_AUCTION_HOUSE_SELL | EXCHANGE_AUCTION_HOUSE_BUY | EXCHANGE_NPC_RESURRECT_PET | EXCHANGE_NPC_EXCHANGE_MOUNT) "|" npc.id
```

```js
EXCHANGE_CHARACTER_EXCHANGE "|" character.id
```

```js
EXCHANGE_OFFLINE_CHARACTER_SHOP_BUY "|" character.id "|" character.cellId
```

```js
EXCHANGE_OFFLINE_CHARACTER_SHOP_SELL
```

```js
EXCHANGE_TAX_COLLECTOR_STORAGE "|" taxCollector.id
```

```js
(EXCHANGE_MULTI_CRAFT_INVITE | EXCHANGE_MULTI_CRAFT_ASK) "|" character.id "|" skill.id
```

```js
EXCHANGE_MOUNT_STORAGE
```

---

### NpcExchangeSell

#### Header

```js
"ES"
```

#### Body

```js
item.id "|" item.quantity
```

---

### CanLeaveExchange

#### Header

```js
"EV"
```

#### Body

```js
EMPTY
```

---

### SetCraftPublicModeOption

#### Header

```js
"EW"
```

#### Body

```js
(ENABLE | DISABLE)
```

---

### MovePaddockMountToStable

#### Header

```js
"Efg"
```

#### Body

```js
mount.id
```

---

### MoveStableMountToPaddock

#### Header

```js
"Efp"
```

#### Body

```js
mount.id
```

---

### GetOfflineCharacterShopTax

#### Header

```js
"Eq"
```

#### Body

```js
EMPTY
```

---

### MoveCertificateMountToStable

#### Header

```js
"ErC"
```

#### Body

```js
certificate.id
```

---

### MoveStableMountToCertificate

#### Header

```js
"Erc"
```

#### Body

```js
mount.id
```

---

### MoveStableMountToEquipped

#### Header

```js
"Erg"
```

#### Body

```js
mount.id
```

---

### MoveEquippedMountToStable

#### Header

```js
"Erp"
```

#### Body

```js
mount.id
```

---

### AddFriend

#### Header

```js
"FA"
```

#### Body

```js
{FROM_FRIENDS} (character.name | "*" account.nickname)
```

#### Constants

```js
FROM_FRIENDS = "%"
```

---

### RemoveFriend

#### Header

```js
"FD"
```

#### Body

```js
(character.name | "*" account.nickname)
```

---

### JoinSpouse

#### Header

```js
"FJS"
```

---

### FollowSpouse

#### Header

```js
"FJC"
```

#### Body

```js
(ENABLE | DISABLE)
```

---

### JoinNoviceFriend

#### Header

```js
"FJF"
```

#### Body

```js
character.name
```

---

### GetFriendList

#### Header

```js
"FL"
```

#### Body

```js
EMPTY
```

---

### SetNotifyFriendConnectionOption

#### Header

```js
"FO"
```

#### Body

```js
(ENABLE | DISABLE)
```

---

### StartGameAction

#### Header

```js
"GA"
```

#### Body

```js
ACTION_MOVE ENCODE_PATH(path)
```

```js
ACTION_USE_SPELL spell.id ";" cell.id
```

```js
ACTION_USE_WEAPON cell.id
```

```js
ACTION_USE_RESOURCE cell.id ";" skill.id
```

```js
ACTION_USE_SKILL skill.id
```

```js
(ACTION_USE_PRISM | ACTION_ATTACK_CHARACTER | ACTION_ATTACK_TAX_COLLECTOR | ACTION_ATTACK_MUTANT | ACTION_ATTACK_PRISM) entity.id
```

```js
(ACTION_WEDDING_ACCEPT | ACTION_WEDDING_REFUSE) entity.id
```

```js
(ACTION_DEFIANCE_REQUEST | ACTION_DEFIANCE_ACCEPT | ACTION_DEFIANCE_REFUSE) asker.id
```

```js
ACTION_JOIN_FIGHT fight.id {";" team.id}
```

#### Constants

```js
ACTION_MOVE = 001
ACTION_USE_SPELL = 300
ACTION_USE_WEAPON = 303
ACTION_USE_RESOURCE = 500
ACTION_USE_SKILL = 507
ACTION_USE_PRISM = 512
ACTION_WEDDING_ACCEPT = 618
ACTION_WEDDING_REFUSE = 619
ACTION_DEFIANCE_REQUEST = 900
ACTION_DEFIANCE_ACCEPT = 901
ACTION_DEFIANCE_REFUSE = 902
ACTION_JOIN_FIGHT = 903
ACTION_ATTACK_CHARACTER = 906
ACTION_ATTACK_TAX_COLLECTOR = 909
ACTION_ATTACK_MUTANT = 910
ACTION_ATTACK_PRISM = 912
```

#### Functions

```js
function ENCODE_64(value) {
    var array = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_";
    var encodedValue = array.charAt(value);
    return encodedValue;
}
```

```js
function DECODE_64(encodedValue) {
    var array = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_";
    var value = array.indexOf(encodedValue);
    return value;
}
```

```js
function MAKE_SHORT_PATH(fullPath) {
    var previousDirectionId = null;
    var shortPath = [];
    for (var i = fullpath.length - 1; i >= 0; i--) {
        var directionId = fullPath[i].directionId;
        if (directionId != previousDirectionId) {
            shortPath.unshift(fullPath[i]);
            previousDirectionId = directionId;
        }
    }
    return shortPath;
}

function ENCODE_PATH(path) {
    var shortPath = MAKE_SHORT_PATH(path);
    var encodedPath = "";
    for (var i = 0; i < shortPath.length; i++) {
        var cellId = shortPath[i].cellId;
        var directionId = shortPath[i].directionId;
        var e0 = directionId & ((1 << 2) | (1 << 1) | 1);
        var e1 = (cellId & ((1 << 11) | (1 << 10) | (1 << 9) | (1 << 8) | (1 << 7) | (1 << 6))) >> 6;
        var e2 = cellId & ((1 << 5) | (1 << 4) | (1 << 3) | (1 << 2) | (1 << 1) | 1);
        encodedPath += ENCODE_64(e0) + ENCODE_64(e1) + ENCODE_64(e2);
    }
    return encodedPath;
}
```

```js
function MAKE_FULL_PATH(shortPath, mapWidth) {
    var widthPathLength = (mapWidth * 2) - 1;
    var nextCellIdIncrements = [1, mapWidth, (mapWidth * 2) - 1, mapWidth - 1, -1, -mapWidth, -((mapWidth * 2) - 1), -(mapWidth - 1)];
    var fullPath = [];
    var i = 0;
    fullPath.push({"cellId": shortPath[i].cellId});
    for (i = 1; i < shortPath.length; i++) {
        var cellId = shortPath[i].cellId;
        var directionId = shortPath[i].directionId;
        var potentialPathLength = widthPathLength;
        while (fullPath[fullPath.length - 1].cellId != cellId) {
            fullPath.push({"cellId": fullPath[fullPath.length - 1].cellId + nextCellIdIncrements[directionId]});
            if (--potentialPathLength < 0) {
                return null;
            }
        }
    }
    return fullPath;
}

function DECODE_PATH(encodedPath) {
    var path = [];
    for (var i = 0; i < encodedPath.length; i += 3) {
        var e0 = DECODE_64(encodedPath.charAt(i));
        var e1 = DECODE_64(encodedPath.charAt(i + 1));
        var e2 = DECODE_64(encodedPath.charAt(i + 2));
        var cellId = ((e1 << 6) & ((1 << 9) | (1 << 8) | (1 << 7) | (1 << 6))) | e2;
        var directionId = e0;
        path.push({"cellId": cellId, "directionId": directionId});
    }
    return MAKE_FULL_PATH(path);
}
```

---

### StartGame

#### Header

```js
"GC"
```

#### Body

```js
STATE_NOT_IN_FIGHT
```

#### Constants

```js
STATE_NOT_IN_FIGHT = 1
```

---

### GetMapDetails

#### Header

```js
"GD"
```

#### Body

```js
{map.id}
```

---

### ReleaseCharacterSoul

#### Header

```js
"GF"
```

#### Body

```js
EMPTY
```

---

### GetGameDetails

#### Header

```js
"G"
```

#### Body

```js
"I"
```

RETRO:

```js
"І"
```

---

### StopGameAction

#### Header

```js
"GKE"
```

#### Body

```js
action.id "|" character.cellId
```

---

### AcknowledgeGameAction

#### Header

```js
"GKK"
```

#### Body

```js
action.id
```

---

### GetDisablePvpLostHonor

#### Header

```js
"GP"
```

#### Body

```js
ASK_DISABLE
```

#### Constants

```js
ASK_DISABLE = "*"
```

---

### SetPvpState

#### Header

```js
"GP"
```

#### Body

```js
(ENABLE | DISABLE)
```

---

### KickFighter

#### Header

```js
"GQ"
```

#### Body

```js
{kicked.id}
```

---

### ValidateFight

#### Header

```js
"GR"
```

#### Body

```js
isReady
```

---

### AcknowledgeFightTurnResponse

#### Header

```js
"GT"
```

#### Body

```js
EMPTY
```

---

### FlagFightChallengeTarget

#### Header

```js
"Gdi"
```

#### Body

```js
challenge.id
```

---

### FlagFightCell

#### Header

```js
"Gf"
```

#### Body

```js
cell.id
```

---

### SetFightStartPosition

#### Header

```js
"Gp"
```

#### Body

```js
cell.id
```

---

### FinishFightTurn

#### Header

```js
"Gt"
```

#### Body

```js
EMPTY
```

---

### DisplayArea

#### Header

```js
"Ir"
```

#### Body

```js
displayArea.width ";" displayArea.height ";" (STATE_NORMAL | STATE_FULLSCREEN | STATE_OTHER)
```

#### Constants

```js
STATE_NORMAL = 0
STATE_FULLSCREEN = 1
STATE_OTHER = 2
```

---

### SetJobOptions

#### Header

```js
"JO"
```

#### Body

```js
job.id "|" ENCODE_JOB_OPTIONS(job.options) "|" job.minSlotCount
```

#### Functions

```js
function NEW_JOB_OPTIONS() {
    var jobOptions = {};
    jobOptions.noResourceProvided = false;
    jobOptions.freeOnFailure = false;
    jobOptions.paid = false;
    return jobOptions;
}
```

```js
function ENCODE_JOB_OPTIONS(jobOptions) {
    var encodedJobOptions = 0;
    encodedJobOptions |= jobOptions.noResourceProvided << 2;
    encodedJobOptions |= jobOptions.freeOnFailure << 1;
    encodedJobOptions |= jobOptions.paid;
    return encodedJobOptions;
}
```

```js
function DECODE_JOB_OPTIONS(encodedJobOptions) {
    var jobOptions = {};
    jobOptions.noResourceProvided = (encodedJobOptions >> 2) & 1;
    jobOptions.freeOnFailure = (encodedJobOptions >> 1) & 1;
    jobOptions.paid = encodedJobOptions & 1;
    return jobOptions;
}
```

---

### LockKey

#### Header

```js
"KK"
```

#### Body

```js
(LOCK_UNLOCK | LOCK_CHANGE) "|" (EMPTY_CODE | keyCode)
```

#### Constants

```js
LOCK_UNLOCK = 0
LOCK_CHANGE = 1
```

```js
EMPTY_CODE = "-"
```

---

### CanCloseLock

#### Header

```js
"KV"
```

#### Body

```js
EMPTY
```

---

### UseItem

#### Header

```js
"O"
```

#### Body

```js
(NOT_VALIDATED | VALIDATED) item.id "|" {{sprite.id} "|" cell.id}
```

#### Constants

```js
NOT_VALIDATED = "U"
VALIDATED = "u"
```

---

### DropItem

#### Header

```js
"OD"
```

#### Body

```js
item.id "|" item.quantity
```

---

### MoveInventoryItem

#### Header

```js
"OM"
```

#### Body

```js
item.id "|" item.position {"|" item.quantity}
```

#### Parameters

```js
item.position = (ITEM_POSITION_INVENTORY | ITEM_POSITION_AMULET | ITEM_POSITION_WEAPON | ITEM_POSITION_RINGS | ITEM_POSITION_BELT | ITEM_POSITION_BOOTS | ITEM_POSITION_HAT | ITEM_POSITION_CLOAK | ITEM_POSITION_PET | ITEM_POSITION_DOFUS | ITEM_POSITION_SHIELD | ITEM_POSITION_MOUNT | ITEM_POSITION_SHORTCUTS)
```

#### Constants

```js
ITEM_POSITION_INVENTORY = -1
ITEM_POSITION_WEAPON = 1
ITEM_POSITION_BELT = 3
ITEM_POSITION_BOOTS = 5
ITEM_POSITION_PET = 8
ITEM_POSITION_DOFUS = (9 -> 14)
ITEM_POSITION_SHIELD = 15
ITEM_POSITION_MOUNT = 16
ITEM_POSITION_SHORTCUTS = (35 -> 57)
```

---

### DestroyItem

#### Header

```js
"Od"
```

#### Body

```js
item.id "|" item.quantity
```

---

### FeedLivingItem

#### Header

```js
"Of"
```

#### Body

```js
livingItem.id "|" livingItem.position "|" foodItem.id
```

---

### SetLivingItemSkin

#### Header

```js
"Os"
```

#### Body

```js
livingItem.id "|" livingItem.position "|" livingItem.skinId
```

#### Parameters

```js
livingItem.skinId = (1 -> 20)
```

---

### DissociateLivingItem

#### Header

```js
"Ox"
```

#### Body

```js
livingItem.id "|" livingItem.position
```

---

### AcceptGroupInvitation

#### Header

```js
"PA"
```

#### Body

```js
EMPTY
```

---

### FollowGroupMember

#### Header

```js
"PF"
```

#### Body

```js
(ENABLE | DISABLE) character.id
```

---

### FollowGroupMemberByEveryone

#### Header

```js
"PG"
```

#### Body

```js
(ENABLE | DISABLE) character.id
```

---

### InviteInGroup

#### Header

```js
"PI"
```

#### Body

```js
character.name
```

---

### RefuseGroupInvitation

#### Header

```js
"PR"
```

#### Body

```js
EMPTY
```

---

### KickGroupMember

#### Header

```js
"PV"
```

#### Body

```js
{kicked.id}
```

---

### LocateGroup

#### Header

```js
"PW"
```

#### Body

```js
EMPTY
```

---

### GetQuestList

#### Header

```js
"QL"
```

#### Body

```js
EMPTY
```

---

### GetQuestStep

#### Header

```js
"QS"
```

#### Body

```js
quest.id
```

---

### BuyPaddock

#### Header

```js
"Rb"
```

#### Body

```js
paddock.price
```

---

### SterilizeMount

#### Header

```js
"Rc"
```

#### Body

```js
EMPTY
```

---

### GetCertificateMountDetails

#### Header

```js
"Rd"
```

#### Body

```js
id "|" mount.validityTimestamp
```

---

### ReleaseMount

#### Header

```js
"Rf"
```

#### Body

```js
EMPTY
```

---

### RenameMount

#### Header

```js
"Rn"
```

#### Body

```js
mount.name
```

---

### RemovePaddockItem

#### Header

```js
"Ro"
```

#### Body

```js
item.cellId
```

---

### GetPaddockMountDetails

#### Header

```js
"Rp"
```

#### Body

```js
mount.id
```

---

### ToggleRideMount

#### Header

```js
"Rr"
```

#### Body

```js
EMPTY
```

---

### SellPaddock

#### Header

```js
"Rs"
```

#### Body

```js
(CANCEL_SALE | paddock.price)
```

#### Constants

```
CANCEL_SALE = 0
```

---

### CanCloseBuyPaddock

#### Header

```js
"Rv"
```

#### Body

```js
EMPTY
```

---

### SetMountXp

#### Header

```js
"Rx"
```

#### Body

```js
mount.xpPercent
```

---

### UpgradeCharacterSpell

#### Header

```js
"SB"
```

#### Body

```js
spell.id
```

---

### ForgetSpell

#### Header

```js
"SF"
```

#### Body

```js
(-1 | spell.id)
```

---

### MoveSpell

#### Header

```js
"SM"
```

#### Body

```js
spell.id "|" spell.position
```

#### Parameters

```js
spell.position = SPELL_POSITION_SHORTCUTS
```

#### Constants

```js
SPELL_POSITION_SHORTCUTS = (1 -> 23)
```

---

### FinishTutorial

#### Header

```js
"TV"
```

#### Body

```js
endId {"|" cell.id "|" directionId}
```

---

### UsePortalTransport

#### Header

```js
"WU"
```

#### Body

```js
destination.mapId
```

---

### CanClosePortalTransport

#### Header

```js
"WV"
```

#### Body

```js
EMPTY
```

---

### UsePrismTransport

#### Header

```js
"Wp"
```

#### Body

```js
destination.mapId
```

---

### UseCityTransport

#### Header

```js
"Wu"
```

#### Body

```js
destination.mapId
```

---

### CanCloseCityTransport

#### Header

```js
"Wv"
```

#### Body

```js
EMPTY
```

---

### CanClosePrismTransport

#### Header

```js
"Ww"
```

#### Body

```js
EMPTY
```

---

### SubscribeChatChannel

#### Header

```js
"cC"
```

#### Body

```js
(ENABLE | DISABLE) [(CHANNEL_INFORMATION | CHANNEL_PUBLIC | CHANNEL_TEAM | CHANNEL_PARTY | CHANNEL_PRIVATE | CHANNEL_GUILD | CHANNEL_ALIGNMENT | CHANNEL_RECRUITMENT | CHANNEL_TRADING | CHANNEL_NOVICE | CHANNEL_ADMIN), EMPTY]
```

RETRO:

```js
(ENABLE | DISABLE) [(CHANNEL_INFORMATION | CHANNEL_PUBLIC | CHANNEL_TEAM | CHANNEL_PARTY | CHANNEL_PRIVATE | CHANNEL_GUILD | CHANNEL_ALIGNMENT | CHANNEL_RECRUITMENT | CHANNEL_TRADING | CHANNEL_NOVICE | CHANNEL_ADMIN | CHANNEL_EVENT), EMPTY]
```

#### Constants

```js
CHANNEL_INFORMATION = "i"
CHANNEL_PRIVATE = "p"
CHANNEL_EVENT = "e"
```

---

### CanCloseDocument

#### Header

```js
"dV"
```

#### Body

```js
EMPTY
```

---

### SetCharacterDirection

#### Header

```js
"eD"
```

#### Body

```js
character.directionId
```

---

### UseEmote

#### Header

```js
"eU"
```

#### Body

```js
emoteId
```

---

### GetFightDetails

#### Header

```js
"fD"
```

#### Body

```js
fight.id
```

---

### ToggleNeedHelpFightOption

#### Header

```js
"fH"
```

#### Body

```js
EMPTY
```

---

### GetFightList

#### Header

```js
"fL"
```

#### Body

```js
EMPTY
```

---

### ToggleCantJoinFightOption

#### Header

```js
"fN"
```

#### Body

```js
EMPTY
```

---

### ToggleCantJoinIfNotGroupFightOption

#### Header

```js
"fP"
```

#### Body

```js
EMPTY
```

---

### ToggleCantWatchFightOption

#### Header

```js
"fS"
```

#### Body

```js
EMPTY
```

---

### UpgradeTaxCollectorStat

#### Header

```js
"gB"
```

#### Body

```js
(TAX_COLLECTOR_STAT_POPULATION | TAX_COLLECTOR_STAT_PODS | TAX_COLLECTOR_STAT_PROSPECTING | TAX_COLLECTOR_STAT_WISDOM)
```

#### Constants

```js
TAX_COLLECTOR_STAT_POPULATION = "k"
TAX_COLLECTOR_STAT_PODS = "o"
TAX_COLLECTOR_STAT_PROSPECTING = "p"
TAX_COLLECTOR_STAT_WISDOM = "x"
```

---

### CreateGuild

#### Header

```js
"gC"
```

#### Body

```js
guildEmblem.backId "|" guildEmblem.backColor "|" guildEmblem.symbolId "|" guildEmblem.symbolColor "|" guild.name
```

---

### RemoveTaxCollector

#### Header

```js
"gF"
```

#### Body

```js
taxCollector.id
```

---

### AddTaxCollector

#### Header

```js
"gH"
```

#### Body

```js
EMPTY
```

---

### GetTaxCollectorStats

#### Header

```js
"gIB"
```

#### Body

```js
EMPTY
```

---

### GetGuildPaddockList

#### Header

```js
"gIF"
```

#### Body

```js
EMPTY
```

---

### GetGuildXp

#### Header

```js
"gIG"
```

#### Body

```js
EMPTY
```

---

### GetGuildHouseList

#### Header

```js
"gIH"
```

#### Body

```js
EMPTY
```

---

### GetGuildMemberList

#### Header

```js
"gIM"
```

#### Body

```js
EMPTY
```

---

### GetTaxCollectorList

#### Header

```js
"gIT"
```

#### Body

```js
EMPTY
```

---

### CloseTaxCollector

#### Header

```js
"gITV"
```

#### Body

```js
EMPTY
```

---

### RefuseGuildInvitation

#### Header

```js
"gJE"
```

#### Body

```js
asker.id
```

---

### AcceptGuildInvitation

#### Header

```js
"gJK"
```

#### Body

```js
asker.id
```

---

### InviteInGuild

#### Header

```js
"gJR"
```

#### Body

```js
character.name
```

---

### KickGuildMember

#### Header

```js
"gK"
```

#### Body

```js
character.name
```

---

### SetGuildMemberOptions

#### Header

```js
"gP"
```

#### Body

```js
member.id "|" member.rankId "|" member.xpPercent "|" ENCODE_GUILD_RIGHTS(member.rights)
```

#### Functions

```js
function NEW_GUILD_RIGHTS() {
    var guildRights = {};
    guildRights.canManageOtherMount = false;
    guildRights.canManagePaddock = false;
    guildRights.canUsePaddock = false;
    guildRights.canCollectTaxCollector = false;
    guildRights.canManageOwnXPPercent = false;
    guildRights.canAddTaxCollector = false;
    guildRights.canManageRanks = false;
    guildRights.canManageXPPercent = false;
    guildRights.canKick = false;
    guildRights.canInvite = false;
    guildRights.canManageRights = false;
    guildRights.canManageUpgrades = false;
    guildRights.isLeader = false;
    return guildRights;
}
```

```js
function ENCODE_GUILD_RIGHTS(guildRights) {
    var encodedGuildRights = 0;
    encodedGuildRights |= guildRights.canManageOtherMount << 14;
    encodedGuildRights |= guildRights.canManagePaddock << 13;
    encodedGuildRights |= guildRights.canUsePaddock << 12;
    encodedGuildRights |= guildRights.canCollectTaxCollector << 9;
    encodedGuildRights |= guildRights.canManageOwnXPPercent << 8;
    encodedGuildRights |= guildRights.canAddTaxCollector << 7;
    encodedGuildRights |= guildRights.canManageRanks << 6;
    encodedGuildRights |= guildRights.canManageXPPercent << 5;
    encodedGuildRights |= guildRights.canKick << 4;
    encodedGuildRights |= guildRights.canInvite << 3;
    encodedGuildRights |= guildRights.canManageRights << 2;
    encodedGuildRights |= guildRights.canManageUpgrades << 1;
    encodedGuildRights |= guildRights.isLeader;
    return encodedGuildRights;
}
```

```js
function DECODE_GUILD_RIGHTS(encodedGuildRights) {
    var guildRights = {};
    guildRights.canManageOtherMount = (encodedGuildRights >> 14) & 1;
    guildRights.canManagePaddock = (encodedGuildRights >> 13) & 1;
    guildRights.canUsePaddock = (encodedGuildRights >> 12) & 1;
    guildRights.canCollectTaxCollector = (encodedGuildRights >> 9) & 1;
    guildRights.canManageOwnXPPercent = (encodedGuildRights >> 8) & 1;
    guildRights.canAddTaxCollector = (encodedGuildRights >> 7) & 1;
    guildRights.canManageRanks = (encodedGuildRights >> 6) & 1;
    guildRights.canManageXPPercent = (encodedGuildRights >> 5) & 1;
    guildRights.canKick = (encodedGuildRights >> 4) & 1;
    guildRights.canInvite = (encodedGuildRights >> 3) & 1;
    guildRights.canManageRights = (encodedGuildRights >> 2) & 1;
    guildRights.canManageUpgrades = (encodedGuildRights >> 1) & 1;
    guildRights.isLeader = encodedGuildRights & 1;
    return guildRights;
}
```

---

### JoinTaxCollectorDefense

#### Header

```js
"gTJ"
```

#### Body

```js
taxCollector.id
```

---

### LeaveTaxCollectorDefense

#### Header

```js
"gTV"
```

#### Body

```js
taxCollector.id
```

---

### CanCloseCreateGuild

#### Header

```js
"gV"
```

#### Body

```js
EMPTY
```

---

### UpgradeTaxCollectorSpell

#### Header

```js
"gb"
```

#### Body

```js
spell.id
```

---

### TeleportToGuildPaddock

#### Header

```js
"gf"
```

#### Body

```js
paddock.mapId
```

---

### TeleportToGuildHouse

#### Header

```js
"gh"
```

#### Body

```js
house.id
```

---

### BuyHouse

#### Header

```js
"hB"
```

#### Body

```js
house.price
```

---

### GetGuildHouseOptions

#### Header

```js
"hG"
```

#### Body

```js
EMPTY
```

---

### SetGuildHouseOptions

#### Header

```js
"hG"
```

#### Body

```js
ENCODE_GUILD_HOUSE_OPTIONS(house.guildOptions)
```

#### Functions

```js
function NEW_GUILD_HOUSE_OPTIONS() {
    var guildHouseOptions = {};
    guildHouseOptions.restForGuild = false;
    guildHouseOptions.teleportForGuild = false;
    guildHouseOptions.chestAccessDenyForOthers = false;
    guildHouseOptions.chestAccessAllowKeylessForGuild = false;
    guildHouseOptions.houseAccessDenyForOthers = false;
    guildHouseOptions.houseAccessAllowKeylessForGuild = false;
    guildHouseOptions.showDoorEmblemForOthers = false;
    guildHouseOptions.showDoorEmblemForGuild = false;
    return guildHouseOptions;
}
```

```js
function ENCODE_GUILD_HOUSE_OPTIONS(guildHouseOptions) {
    var encodedGuildHouseOptions = 0;
    encodedGuildHouseOptions |= guildHouseOptions.restForGuild << 8;
    encodedGuildHouseOptions |= guildHouseOptions.teleportForGuild << 7;
    encodedGuildHouseOptions |= guildHouseOptions.chestAccessDenyForOthers << 6;
    encodedGuildHouseOptions |= guildHouseOptions.chestAccessAllowKeylessForGuild << 5;
    encodedGuildHouseOptions |= guildHouseOptions.houseAccessDenyForOthers << 4;
    encodedGuildHouseOptions |= guildHouseOptions.houseAccessAllowKeylessForGuild << 3;
    encodedGuildHouseOptions |= guildHouseOptions.showDoorEmblemForOthers << 2;
    encodedGuildHouseOptions |= guildHouseOptions.showDoorEmblemForGuild << 1;
    return encodedGuildHouseOptions;
}
```

```js
function DECODE_GUILD_HOUSE_OPTIONS(encodedGuildHouseOptions) {
    var guildHouseOptions = {};
    guildHouseOptions.restForGuild = (encodedGuildHouseOptions >> 8) & 1;
    guildHouseOptions.teleportForGuild = (encodedGuildHouseOptions >> 7) & 1;
    guildHouseOptions.chestAccessDenyForOthers = (encodedGuildHouseOptions >> 6) & 1;
    guildHouseOptions.chestAccessAllowKeylessForGuild = (encodedGuildHouseOptions >> 5) & 1;
    guildHouseOptions.houseAccessDenyForOthers = (encodedGuildHouseOptions >> 4) & 1;
    guildHouseOptions.houseAccessAllowKeylessForGuild = (encodedGuildHouseOptions >> 3) & 1;
    guildHouseOptions.showDoorEmblemForOthers = (encodedGuildHouseOptions >> 2) & 1;
    guildHouseOptions.showDoorEmblemForGuild = (encodedGuildHouseOptions >> 1) & 1;
    return guildHouseOptions;
}
```

---

### AddGuildHouse

#### Header

```js
"hG+"
```

#### Body

```js
EMPTY
```

---

### RemoveGuildHouse

#### Header

```js
"hG-"
```

#### Body

```js
EMPTY
```

---

### KickCharacterFromHouse

#### Header

```js
"hQ"
```

#### Body

```js
character.id
```

---

### SellHouse

#### Header

```js
"hS"
```

#### Body

```js
(CANCEL_SALE | house.price)
```

#### Constants

```
CANCEL_SALE = 0
```

---

### CanCloseBuyHouse

#### Header

```js
"hV"
```

#### Body

```js
EMPTY
```

---

### AddEnemy

#### Header

```js
"iA"
```

#### Body

```js
{FROM_ENEMIES} (character.name | "*" account.nickname)
```

#### Constants

```js
FROM_ENEMIES = "%"
```

---

### RemoveEnemy

#### Header

```js
"iD"
```

#### Body

```js
(character.name | "*" account.nickname)
```

---

### GetEnemyList

#### Header

```js
"iL"
```

#### Body

```js
EMPTY
```

---

### Ping

#### Header

```js
"ping"
```

#### Body

```js
EMPTY
```

---

### QuickPing

#### Header

```js
"qping"
```

#### Body

```js
EMPTY
```

---

### RPingResponse?

#### Header

```js
"rpong"
```

#### Body

```js
payload?
```