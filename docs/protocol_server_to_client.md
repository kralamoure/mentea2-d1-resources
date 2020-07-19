# Protocol: Server -> Client

## Index

* [Network message index](#network-message-index)
* [Syntax](#syntax)
* [Common](#common)
* [Network messages](#network-messages)

## Network message index

| Account                                                                   | Basic                                                   | Conquest                                                          | Npc                                             | Exchange                                                                  | Friend                                                        | Game                                                                      | Info                                          | Job                           | Lock                            | Item                                            | Group                                               | Quest                   | Mount                                       | Spell                                     | Tutorial                            | Transport                                   | Specialization                                                  | Area                                                                | Chat                                                    | Document                        | Emote                                     | Fight                         | Guild                                                                           | House                                         | Enemy                                   | Storage                                           | Server                                                      |
|---------------------------------------------------------------------------|---------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------|-------------------------------|---------------------------------|-------------------------------------------------|-----------------------------------------------------|-------------------------|---------------------------------------------|-------------------------------------------|-------------------------------------|---------------------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------|---------------------------------|-------------------------------------------|-------------------------------|---------------------------------------------------------------------------------|-----------------------------------------------|-----------------------------------------|---------------------------------------------------|-------------------------------------------------------------|
| [CreateCharacterResult](#createcharacterresult)                           | [ClearAdminConsole](#clearadminconsole)                 | [PrismAttackedInfo](#prismattackedinfo)                           | [StartNpcDialogSuccess](#startnpcdialogsuccess) | [CraftLoopInfo](#craftloopinfo)                                           | [AddFriendResult](#addfriendresult)                           | [GameAction](#gameaction)                                                 | [CompassCoordinates](#compasscoordinates)       | [JobLevelUp](#joblevelup)     | [StartLock](#startlock)         | [AddInventoryItem](#addinventoryitem)           | [AcceptGroupInvitation](#acceptgroupinvitation)     | [QuestList](#questlist) | [StartBuySellPaddock](#startbuysellpaddock) | [SpellModifier](#spellmodifier)           | [WelcomeTutorial](#welcometutorial) | [StartPortalTransport](#startportaltransport)                 | [ChangeAlignmentSpecialization](#changealignmentspecialization) | [ChangeConquestAreaAlignmentInfo](#changeconquestareaalignmentinfo) | [SubscribeChatChannelState](#subscribechatchannelstate) | [StartDocument](#startdocument) | [AddEmoteInfo](#addemoteinfo)             | [FightCount](#fightcount)     | [TaxCollectorAttackedInfo](#taxcollectorattackedinfo)                           | [BuyHouseResult](#buyhouseresult)             | [AddEnemyResult](#addenemyresult)       | [UpdateOwnedStorageList](#updateownedstoragelist) | [LoginServerHello](#loginserverhello)                       |
| [DeleteCharacterFailure](#deletecharacterfailure)                         | [RemoveAdminRights](#removeadminrights)                 | [AlignedConquestAreaModifier](#alignedconquestareamodifier)       | [PauseNpcDialog](#pausenpcdialog)               | [ExchangeBuyResult](#exchangebuyresult)                                   | [RemoveFriendResult](#removefriendresult)                     | [FinishFightAction](#finishfightaction)                                   | [MarkedCoordinateList](#markedcoordinatelist) | [JobOptions](#joboptions)     | [LockKeyResult](#lockkeyresult) | [InventoryItemList](#inventoryitemlist)         | [StartGroup](#startgroup)                           | [QuestStep](#queststep) | [MountDetails](#mountdetails)               | [StartForgetSpell](#startforgetspell)     | [StartTutorial](#starttutorial)     | [UsePortalTransportFailure](#useportaltransportfailure)       | [AlignmentSpecialization](#alignmentspecialization)             | [SubAreaList](#subarealist)                                         | [ChatMessage](#chatmessage)                             | [CloseDocument](#closedocument) | [CharacterDirection](#characterdirection) | [FightDetails](#fightdetails) | [CreateGuildResult](#createguildresult)                                         | [StartBuySellHouse](#startbuysellhouse)       | [RemoveEnemyResult](#removeenemyresult) | [StorageLockState](#storagelockstate)             | [GameServerHello](#gameserverhello)                         |
| [StartStoreService [RETRO]](#startstoreservice-[retro])                   | [GiveAdminRights](#giveadminrights)                     | [PrismDeadInfo](#prismdeadinfo)                                   | [NpcDialogQuestion](#npcdialogquestion)         | [StartExchange](#startexchange)                                           | [FriendList](#friendlist)                                     | [StartFightAction](#startfightaction)                                     | [FinishRestoreLife](#finishrestorelife)       | [RemoveJob](#removejob)       | [CloseLock](#closelock)         | [DropItemFailure](#dropitemfailure)             | [FollowGroupMemberResult](#followgroupmemberresult) |                         | [UpdateEquippedMount](#updateequippedmount) | [SpellList](#spelllist)                   | [TutorialTip](#tutorialtip)         | [ClosePortalTransport](#closeportaltransport)                 |                                                                 | [ChangeSubAreaAlignment](#changesubareaalignment)                   | [UseSmiley](#usesmiley)                                 |                                 | [EmoteList](#emotelist)                   | [FightList](#fightlist)       | [AddTaxCollectorFailure](#addtaxcollectorfailure)                               | [GuildHouseOptions](#guildhouseoptions)       | [EnemyList](#enemylist)                 |                                                   | [ServerMessage](#servermessage)                             |
| [FriendServerList](#friendserverlist)                                     | [UpdateAdminConsoleMessage](#updateadminconsolemessage) | [PrismDefenseDetails](#prismdefensedetails)                       | [CloseNpcDialog](#closenpcdialog)               | [AuctionHouseItemList](#auctionhouseitemlist)                             | [NotifyFriendConnectionOption](#notifyfriendconnectionoption) | [StartGameResult](#startgameresult)                                       | [StartRestoreLife](#startrestorelife)         | [JobSkillList](#jobskilllist) |                                 | [ItemFoundOverhead](#itemfoundoverhead)         | [InviteInGroupResult](#inviteingroupresult)         |                         | [MountName](#mountname)                     | [CanShowAllSpellOption](#canshowallspelloption)               |                                     | [StartCityTransport](#startcitytransport)   |                                                                 |                                                                     | [ChatServerMessage](#chatservermessage)                 |                                 | [RemoveEmoteInfo](#removeemoteinfo)       |                               | [TaxCollectorStats](#taxcollectorstats)                                     | [UpdateOwnedHouseList](#updateownedhouselist) |                                         |                                                   | [UpcomingServerDisconnection](#upcomingserverdisconnection) |
| [GiftStored](#giftstored)                                                 | [AdminConsolePrompt](#adminconsoleprompt)               | [ClosePrismDefense](#closeprismdefense)                           |                                                 | [UpdateAuctionHouseItemList](#updateauctionhouseitemlist)                 | [SpouseDetails](#spousedetails)                               | [CellDetails](#celldetails)                                               | [ItemOverhead](#itemoverhead)                 | [JobXp](#jobxp)               |                                 | [ValidateUseItem](#validateuseitem)             | [GroupLeader](#groupleader)                         |                         | [PaddockDetails](#paddockdetails)           | [UpgradeCharacterSpellResult](#upgradecharacterspellresult) |                                     | [StartPrismTransport](#startprismtransport) |                                                                 |                                                                     |                                                         |                                 | [UseEmote](#useemote)                     |                               | [GuildPaddockList](#guildpaddocklist)                                           | [HouseDoorDetails](#housedoordetails)                 |                                         |                                                   | [PingResponse](#pingresponse)                               |
| [AllServerList](#allserverlist)                                           | [AdminConsoleMessage](#adminconsolemessage)             | [UpdatePrismDefenseDefenderList](#updateprismdefensedefenderlist) |                                                 | [AuctionHouseItemAveragePrice](#auctionhouseitemaverageprice)             |                                                               | [CellExternalObjectFrame](#cellexternalobjectframe)                       | [QuantityOverhead](#quantityoverhead)         |                               |                                 | [MoveInventoryItem](#moveinventoryitem)         | [UpdateGroupMemberList](#updategroupmemberlist)     |                         | [RideMountState](#ridemountstate)           |                                           |                                     | [UseTransportFailure](#usetransportfailure) |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [GuildXp](#guildxp)                                                             | [SellHouseResult](#sellhouseresult)           |                                         |                                                   | [QuickPingResponse](#quickpingresponse)                     |
| [ClientKey](#clientkey)                                                   | [BasicCheckFile](#basiccheckfile)                       | [PrismSurvivedInfo](#prismsurvivedinfo)                           |                                                 | [SearchAuctionHouseResult](#searchauctionhouseresult)                     |                                                               | [CellObject2Frame](#cellobject2frame)                                     | [InfoMessage](#infomessage)                   |                               |                                 | [InventoryItemQuantity](#inventoryitemquantity) | [RefuseGroupInvitation](#refusegroupinvitation)     |                         | [CloseBuySellPaddock](#closebuysellpaddock) |                                           |                                     | [CloseCityTransport](#closecitytransport)   |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [GuildHouseList](#guildhouselist)                                               | [CloseBuySellHouse](#closebuysellhouse)       |                                         |                                                   | [RPing](#rping)                                             |
| [CharacterList](#characterlist)                                           | [BasicDate](#basicdate)                                 | [ConquestAreaList](#conquestarealist)                             |                                                 | [AuctionHouseEntryList](#auctionhouseentrylist)                           |                                                               | [MapLoaded](#maploaded)                                                   |                                               |                               |                                 | [RemoveInventoryItem](#removeinventoryitem)     | [RemoteKickGroupMember](#remotekickgroupmember)                           |                         | [MountXp](#mountxp)                         |                                           |                                     | [ClosePrismTransport](#closeprismtransport) |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [UpdateGuildMemberList](#updateguildmemberlist)                                 | [HouseLockState](#houselockstate)             |                                         |                                                   |                                                             |
| [MigrantCharacterList](#migrantcharacterlist)                             | [BasicPopupMessage [RETRO]](#basicpopupmessage-[retro]) | [ConquestBalance](#conquestbalance)                               |                                                 | [UpdateAuctionHouseEntryList](#updateauctionhouseentrylist)               |                                                               | [MapDetails](#mapdetails)                                                 |                                               |                               |                                 | [UpdateEquippedItemSet](#updateequippeditemset) |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [UpdateTaxCollectorList](#updatetaxcollectorlist)                               |                                               |                                         |                                                   |                                                             |
| [CanValidateMigrantCharacterSuccess](#canvalidatemigrantcharactersuccess) | [BasicNoResponse](#basicnoresponse)                     | [UpdatePrismDefenseAttackerList](#updateprismdefenseattackerlist) |                                                 | [UpdateJobCraftspersonList](#updatejobcraftspersonlist)                   |                                                               | [UpdateCellExternalObject](#updatecellexternalobject)                     |                                               |                               |                                 | [EquippedJobTool](#equippedjobtool)             |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [UpdateTaxCollectorDefenseDefenderList](#updatetaxcollectordefensedefenderlist) |                                               |                                         |                                                   |                                                             |
| [CharacterLevelUp](#characterlevelup)                                     | [BasicSubscriberZone](#basicsubscriberzone)             |                                                                   |                                                 | [ValidateExchangeState](#validateexchangestate)                           |                                                               | [UpdateZone](#updatezone)                                                 |                                               |                               |                                 | [EntityAccessories](#entityaccessories)         |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [UpdateTaxCollectorDefenseAttackerList](#updatetaxcollectordefenseattackerlist) |                                               |                                         |                                                   |                                                             |
| [RandomCharacterName](#randomcharactername)                               | [BasicReferenceTime](#basicreferencetime)               |                                                                   |                                                 | [ExchangeContentList](#exchangecontentlist)                                             |                                                               | [FinishFight](#finishfight)                                               |                                               |                               |                                 | [InventoryWeight](#inventoryweight)             |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [RemoteGuildInvitationSuccess](#remoteguildinvitationsuccess)                   |                                               |                                         |                                                   |                                                             |
| [AccountSecretQuestion](#accountsecretquestion)                           | [BasicWhoIsResult](#basicwhoisresult)                   |                                                                   |                                                 | [UpdateLocalExchangeContentList](#updatelocalexchangecontentlist)                       |                                                               | [FighterPosition](#fighterposition)                                       |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [GuildInvitationFailure](#guildinvitationfailure)                               |                                               |                                         |                                                   |                                                             |
| [CharacterRestrictions](#characterrestrictions)                           | [GetBasicAveragePing](#getbasicaverageping)             |                                                                   |                                                 | [RequestExchangeResult](#requestexchangeresult)                           |                                                               | [AddFighterEffect](#addfightereffect)                                     |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [GuildInvitationSuccess](#guildinvitationsuccess)                               |                                               |                                         |                                                   |                                                             |
| [SelectCharacterResult](#selectcharacterresult)                           |                                                         |                                                                   |                                                 | [ExchangeSellResult](#exchangesellresult)                                 |                                                               | [DisablePvpLostHonor](#disablepvplosthonor)                               |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [LocalGuildInvitation](#localguildinvitation)                                   |                                               |                                         |                                                   |                                                             |
| [ClientTicketResult](#clientticketresult)                                 |                                                         |                                                                   |                                                 | [LeaveExchange](#leaveexchange)                                           |                                                               | [ClearFighterEffects](#clearfightereffects)                               |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [RemoteGuildInvitation](#remoteguildinvitation)                                 |                                               |                                         |                                                   |                                                             |
| [RegionalVersion](#regionalversion)                                       |                                                         |                                                                   |                                                 | [CraftPublicModeOption](#craftpublicmodeoption)                           |                                                               | [JoinFight](#joinfight)                                                   |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [KickGuildMemberResult](#kickguildmemberresult)                                 |                                               |                                         |                                                   |                                                             |
| [SelectServerResult](#selectserverresult)                                 |                                                         |                                                                   |                                                 | [FinishCraftLoop](#finishcraftloop)                                       |                                                               | [UpdateEntityList](#updateentitylist)                                     |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [GuildDetails](#guilddetails)                                                   |                                               |                                         |                                                   |                                                             |
| [PlainSelectServerResult](#plainselectserverresult)                       |                                                         |                                                                   |                                                 | [CraftResult](#craftresult)                                               |                                                               | [GameOver](#gameover)                                                     |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [TaxCollectorInfo](#taxcollectorinfo)                                           |                                               |                                         |                                                   |                                                             |
| [AccountCommunity](#accountcommunity)                                     |                                                         |                                                                   |                                                 | [UpdateStableMountList](#updatestablemountlist)                           |                                                               | [FightStartPositionList](#fightstartpositionlist)                         |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [StartGuild](#startguild)                                                       |                                               |                                         |                                                   |                                                             |
| [AccountNickname](#accountnickname)                                       |                                                         |                                                                   |                                                 | [UpdatePaddockMountList](#updatepaddockmountlist)                         |                                                               | [ValidateFightState](#validatefightstate)                                 |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [CloseCreateGuild](#closecreateguild)                                           |                                               |                                         |                                                   |                                                             |
| [QueueDetails](#queuedetails)                                             |                                                         |                                                                   |                                                 | [UpdateOfflineCharacterShopItemList](#updateofflinecharactershopitemlist) |                                                               | [StartFight](#startfight)                                                 |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               | [StartCreateGuild](#startcreateguild)                                           |                                               |                                         |                                                   |                                                             |
| [GiftList](#giftlist)                                                     |                                                         |                                                                   |                                                 | [CraftReferenceInfo](#craftreferenceinfo)                   |                                                               | [FinishFightTurn](#finishfightturn)                                       |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               |                                                                                 |                                               |                                         |                                                   |                                                             |
| [AccountLoginResult](#accountloginresult)                                 |                                                         |                                                                   |                                                 | [UpdateRemoteExchangeContentList](#updateremoteexchangecontentlist)                     |                                                               | [FightTurnOrder](#fightturnorder)                                         |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               |                                                                                 |                                               |                                         |                                                   |                                                             |
| [FirstConnectionInfo](#firstconnectioninfo)                               |                                                         |                                                                   |                                                 | [UpdatePaymentContentList](#updatepaymentcontentlist)                                   |                                                               | [FighterStatList](#fighterstatlist)                                               |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               |                                                                                 |                                               |                                         |                                                   |                                                             |
| [QueuePosition](#queueposition)                                           |                                                         |                                                                   |                                                 | [OfflineCharacterShopTax](#offlinecharactershoptax)                       |                                                               | [AcknowledgeFightTurn](#acknowledgefightturn)                             |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               |                                                                                 |                                               |                                         |                                                   |                                                             |
| [RescueCharacterResult](#rescuecharacterresult)                           |                                                         |                                                                   |                                                 | [UpdateMultiCraftContentList](#updatemulticraftcontentlist)                             |                                                               | [StartFightTurn](#startfightturn)                                         |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               |                                                                                 |                                               |                                         |                                                   |                                                             |
| [CharacterStats](#characterstats)                                           |                                                         |                                                                   |                                                 | [UpdateStorageContentList](#updatestoragecontentlist)                                   |                                                               | [RemoteKickFighter](#remotekickfighter)                                                 |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               |                                                                                 |                                               |                                         |                                                   |                                                             |
| [OwnServerList](#ownserverlist)                                           |                                                         |                                                                   |                                                 | [MountInventoryWeight](#mountinventoryweight)                             |                                                               | [UpdateEntityExtra](#updateentityextra)                           |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               |                                                                                 |                                               |                                         |                                                   |                                                             |
|                                                                           |                                                         |                                                                   |                                                 |                                                                           |                                                               | [UpdateNotValidatedFightList](#updatenotvalidatedfightlist)               |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               |                                                                                 |                                               |                                         |                                                   |                                                             |
|                                                                           |                                                         |                                                                   |                                                 |                                                                           |                                                               | [FightChallenge](#fightchallenge)                                         |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               |                                                                                 |                                               |                                         |                                                   |                                                             |
|                                                                           |                                                         |                                                                   |                                                 |                                                                           |                                                               | [FightChallengeResult](#fightchallengeresult)                             |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               |                                                                                 |                                               |                                         |                                                   |                                                             |
|                                                                           |                                                         |                                                                   |                                                 |                                                                           |                                                               | [FlagFightCell](#flagfightcell)                                           |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               |                                                                                 |                                               |                                         |                                                   |                                                             |
|                                                                           |                                                         |                                                                   |                                                 |                                                                           |                                                               | [UpdateFightOption](#updatefightoption)                                   |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               |                                                                                 |                                               |                                         |                                                   |                                                             |
|                                                                           |                                                         |                                                                   |                                                 |                                                                           |                                                               | [UpdateNotValidatedFightFighterList](#updatenotvalidatedfightfighterlist) |                                               |                               |                                 |                                                 |                                                     |                         |                                             |                                           |                                     |                                             |                                                                 |                                                                     |                                                         |                                 |                                           |                               |                                                                                 |                                               |                                         |                                                   |                                                             |

## Syntax

```js
"a" = a IS TEXT
```

```js
'a' = a IS REGEX
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
"\0"
```

#### Parameters

```js
accessories = weaponAccessory "," hatAccessory "," cloakAccessory "," petAccessory "," shieldAccessory

accessory = <item.modelId, 16> {"~" item.typeId "~" <item.frame + 1>}
```

```js
item = <id, 16> "~" <modelId, 16> "~" <quantity, 16> "~" {<position, 16>} "~" effects
```

```js
item.position = (ITEM_POSITION_INVENTORY | ITEM_POSITION_AMULET | ITEM_POSITION_WEAPON | ITEM_POSITION_RINGS | ITEM_POSITION_BELT | ITEM_POSITION_BOOTS | ITEM_POSITION_HAT | ITEM_POSITION_CLOAK | ITEM_POSITION_PET | ITEM_POSITION_DOFUS | ITEM_POSITION_SHIELD | ITEM_POSITION_MOUNT | ITEM_POSITION_BUFF | ITEM_POSITION_SHORTCUTS)
```

```js
effects = [<effect.typeId, 16> "#" (0 | <effect.param1, 16>) "#" (0 | <effect.param2, 16>) "#" (0 | <effect.param3, 16>) "#" effect.param4, ","]
```

```js
adminConsoleText = [(text | html | ("<a href='asfunction:onHref," (("ShowPlayerPopupMenu" "," character.name) | ("ExecCmd" "," command "," isExecuted)) "'>" text "</a>")), EMPTY]
```

```js
mount = id ":" modelId ":" [ancestor.modelId, ","] ":" [mountCapacity.id, ","] ":" {name} ":" isFemale ":" totalXp "," levelXp "," nextLevelXp ":" level ":" isMountable ":" maxPods ":" isWild ":" stamina "," maxStamina ":" maturity "," maxMaturity ":" energy "," maxEnergy ":" serenity "," minSerenity "," maxSerenity ":" love "," maxLove ":" hoursSinceFecundation ":" isFecundable ":" effects ":" tired "," maxTired ":" reproduction "," maxReproduction
```

```js
friend = enemy = account.nickname {";" (FRIEND_IN_VILLAGE | FRIEND_IN_FIGHT | FRIEND_IN_UNKNOWN) ";" character.name ";" character.level ";" character.alignmentId ";" character.raceId ";" character.isFemale ";" character.gfxId}
```

```js
directionId = (DIRECTION_EAST | DIRECTION_SOUTH_EAST | DIRECTION_SOUTH | DIRECTION_SOUTH_WEST | DIRECTION_WEST | DIRECTION_NORTH_WEST | DIRECTION_NORTH | DIRECTION_NORTH_EAST)
```

```js
entityListUpdate = [(((ADD | ADD_TRANSITION) (summoned | monster | monsterGroup | npc | offlineCharacter | taxCollector | mutant | mutantCharacter | paddockMount | prism | character)) | (REMOVE entity.id)), "|"]

summoned = cell.id ";" directionId ";" {0} ";" id ";" monster.modelId ";" ENTITY_SUMMONED {"," title.id "*" title.param} ";" gfxId {"^" (scale | (scaleX "x" scaleY))} {MONSTER_NO_FLIP} ";" powerLevel ";" (-1 | <color1, 16>) ";" (-1 | <color2, 16>) ";" (-1 | <color3, 16>) ";" accessories {";" lp ";" ap ";" mp {";" neutralResistancePercent ";" earthResistancePercent ";" fireResistancePercent ";" waterResistancePercent ";" airResistancePercent ";" dodgeApPercent ";" dodgeMpPercent} ";" teamIndex}

monster = cell.id ";" directionId ";" {0} ";" id ";" monster.modelId ";" ENTITY_MONSTER {"," title.id "*" title.param} ";" gfxId {"^" (scale | (scaleX "x" scaleY))} {MONSTER_NO_FLIP} ";" powerLevel ";" (-1 | <color1, 16>) ";" (-1 | <color2, 16>) ";" (-1 | <color3, 16>) ";" accessories {";" lp ";" ap ";" mp {";" neutralResistancePercent ";" earthResistancePercent ";" fireResistancePercent ";" waterResistancePercent ";" airResistancePercent ";" dodgeApPercent ";" dodgeMpPercent} ";" teamIndex}

monsterGroup = cell.id ";" directionId ";" (-1 | bonusPercent) ";" id ";" [monster.modelId, ","] ";" ENTITY_MONSTER_GROUP {"," title.id "*" title.param} ";" [monster.gfxId {"^" monster.scaleX {"x" monster.scaleY}}, (SHAPE_CIRCLE | SHAPE_LINE)] {MONSTER_NO_FLIP} ";" [monster.level, ","] ";" [(-1 | <monster.color1, 16>) "," (-1 | <monster.color2, 16>) "," (-1 | <monster.color3, 16>) ";" monster.accessories, ";"] {";"}

npc = cell.id ";" directionId ";" {0} ";" id ";" npc.modelId ";" ENTITY_NPC {"," title.id "*" title.param} ";" gfxId {"^" (scale | (scaleX "x" scaleY))} ";" isFemale ";" (-1 | <color1, 16>) ";" (-1 | <color2, 16>) ";" (-1 | <color3, 16>) ";" accessories ";" {extraId} ";" (0 | artworkId)

offlineCharacter = cell.id ";" directionId ";" {0} ";" id ";" name ";" ENTITY_OFFLINE_CHARACTER {"," title.id "*" title.param} ";" gfxId {"^" (scale | (scaleX "x" scaleY))} ";" (-1 | <color1, 16>) ";" (-1 | <color2, 16>) ";" (-1 | <color3, 16>) ";" accessories ";" {guild.name} ";" {guild.emblem} ";" extraId

taxCollector = cell.id ";" directionId ";" {0} ";" id ";" taxCollector.name ";" ENTITY_TAX_COLLECTOR {"," title.id "*" title.param} ";" gfxId {"^" (scale | (scaleX "x" scaleY))} ";" level ";" ((guild.name ";" guild.emblem) | (lp ";" ap ";" mp ";" neutralResistancePercent ";" earthResistancePercent ";" fireResistancePercent ";" waterResistancePercent ";" airResistancePercent ";" dodgeApPercent ";" dodgeMpPercent ";" teamIndex))

mutant = cell.id ";" directionId ";" {?} ";" id ";" monster.modelId ";" ENTITY_MUTANT {"," title.id "*" title.param} ";" gfxId {"^" (scale | (scaleX "x" scaleY))} ";" isFemale ";" monster.powerLevel ";" accessories ";" (({emoteId} ";" {emoteDurationInMilliseconds} ";" <ENCODE_REMOTE_RESTRICTIONS(restrictions), 36>) | (lp ";" ap ";" mp ";" {neutralResistancePercent} ";" {earthResistancePercent} ";" {fireResistancePercent} ";" {waterResistancePercent} ";" {airResistancePercent} ";" {dodgeApPercent} ";" {dodgeMpPercent} ";" teamIndex))

mutantCharacter = cell.id ";" directionId ";" {?} ";" id ";" monster.modelId "~" character.name ";" ENTITY_MUTANT_CHARACTER {"," title.id "*" title.param} ";" gfxId {"^" (scale | (scaleX "x" scaleY))} ";" isFemale ";" monster.powerLevel ";" accessories ";" (({emoteId} ";" {emoteDurationInMilliseconds} ";" <ENCODE_REMOTE_RESTRICTIONS(restrictions), 36>) | (lp ";" ap ";" mp ";" {neutralResistancePercent} ";" {earthResistancePercent} ";" {fireResistancePercent} ";" {waterResistancePercent} ";" {airResistancePercent} ";" {dodgeApPercent} ";" {dodgeMpPercent} ";" teamIndex))

paddockMount = cell.id ";" directionId ";" {-1} ";" id ";" name ";" ENTITY_PADDOCK_MOUNT {"," title.id "*" title.param} ";" gfxId {"^" (scale | (scaleX "x" scaleY))} ";" owner.name ";" level ";" mount.modelId {";" scale?}

prism = cell.id ";" directionId ";" {0} ";" id ";" monster.modelId ";" ENTITY_PRISM {"," title.id "*" title.param} ";" gfxId {"^" (scale | (scaleX "x" scaleY))} ";" level ";" alignment.level ";" alignment.id

character = cell.id ";" directionId ";" {0} ";" id ";" name ";" raceId {"," title.id "*" title.param} ";" {CHARACTER_NO_TRANSPARENCY} [entity.gfxId {"^" (entity.scale | (entity.scaleX "x" entity.scaleY))}, (SHAPE_CIRCLE | SHAPE_LINE)] ";" isFemale ";" ((alignment.id "," alignment.level "," alignment.rank {"," <level + id> {"," alignment.isDisgraced}} ";" (-1 | <color1, 16>) ";" (-1 | <color2, 16>) ";" (-1 | <color3, 16>) ";" accessories ";" (0 | auraId) ";" {emoteId} ";" {emoteDurationInMilliseconds} ";" {guild.name} ";" {guild.emblem} ";" <ENCODE_REMOTE_RESTRICTIONS(restrictions), 36> ";" {mount.modelId {"," (-1 | <mount.customColor1, 16>) "," (-1 | <mount.customColor2, 16>) "," (-1 | <mount.customColor3, 16>)}} {";"}) | (level ";" alignment.id "," alignment.level "," alignment.rank {"," <level + id> {"," alignment.isDisgraced}} ";" (-1 | <color1, 16>) ";" (-1 | <color2, 16>) ";" (-1 | <color3, 16>) ";" accessories ";" lp ";" ap ";" mp ";" neutralResistancePercent ";" earthResistancePercent ";" fireResistancePercent ";" waterResistancePercent ";" airResistancePercent ";" dodgeApPercent ";" dodgeMpPercent ";" teamIndex {";" mount.modelId {"," (-1 | <mount.customColor1, 16>) "," (-1 | <mount.customColor2, 16>) "," (-1 | <mount.customColor3, 16>)}}))
```

```js
taxCollector.name = <firstNameId, 36> "," <lastNameId, 36>
```

```js
guild.emblem = <backId, 36> "," <backColor, 36> "," <symbolId, 36> "," <symbolColor, 36>
```

```js
teamIndex = (0 | 1)
```

```js
genericName = (taxCollector.name | character.name | monster.modelId)
```

```js
fight.typeId = (FIGHT_DEFIANCE | FIGHT_PVP | FIGHT_PVMA | FIGHT_MXVM | FIGHT_PVM | FIGHT_PVTC | FIGHT_PVMU)
```

```js
team.typeId = (TEAM_CHARACTER | TEAM_MONSTER | TEAM_DEFIANCE_CHARACTER | TEAM_TAX_COLLECTORE)
```

```js
spell = id "~" level "~" ENCODE_64(position)

position = SPELL_POSITION_SHORTCUTS
```

```js
chatText = [(text | html | ("<a href='asfunction:onHref," ("OpenGuildTaxCollectors" | "OpenPayZoneDetails" | ("ShowPlayerPopupMenu" "," character.name {"," id}) | ("ShowItemViewer" "," totalItemIndex) | ("updateCompass" "," map.x "," map.y) | ("ShowLinkWarning" "," langId)) "'>" text "</a>")), EMPTY]
```

#### Constants

```js
EMPTY = ""
```

```js
FAILURE = "E"
SUCCESS = "K"
```

```js
(ADD | ADD_UPDATE | ENABLE) = "+"
(REMOVE | DISABLE) = "-"
ADD_TRANSITION = "~"
```

```js
ITEM_POSITION_INVENTORY = -1
ITEM_POSITION_AMULET = 0
ITEM_POSITION_WEAPON = 1
ITEM_POSITION_RINGS = (2 | 4)
ITEM_POSITION_BELT = 3
ITEM_POSITION_BOOTS = 5
ITEM_POSITION_HAT = 6
ITEM_POSITION_CLOAK = 7
ITEM_POSITION_PET = 8
ITEM_POSITION_DOFUS = (9 -> 14)
ITEM_POSITION_SHIELD = 15
ITEM_POSITION_MOUNT = 16
ITEM_POSITION_BUFF = (20 -> 27)
ITEM_POSITION_SHORTCUTS = (35 -> 57)
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
EXCHANGE_MONEY = "G"
EXCHANGE_ITEM = "O"
```

```js
(MONSTER_NO_FLIP | CHARACTER_NO_TRANSPARENCY) = "*"
```

```js
SHAPE_CIRCLE = ","
SHAPE_LINE = ":"
```

```js
FRIEND_IN_VILLAGE = 1
FRIEND_IN_FIGHT = 2
FRIEND_IN_UNKNOWN = "?"
```

```js
ENTITY_SUMMONED = -1
ENTITY_MONSTER = -2
ENTITY_MONSTER_GROUP = -3
ENTITY_NPC = -4
ENTITY_OFFLINE_CHARACTER = -5
ENTITY_TAX_COLLECTOR = -6
ENTITY_MUTANT = -7
ENTITY_MUTANT_CHARACTER = -8
ENTITY_PADDOCK_MOUNT = -9
ENTITY_PRISM = -10
```

```js
FIGHT_DEFIANCE = 0
FIGHT_PVP = 1
FIGHT_PVMA = 2
FIGHT_MXVM = 3
FIGHT_PVM = 4
FIGHT_PVTC = 5
FIGHT_PVMU = 6
```

```js
TEAM_CHARACTER = 0
TEAM_MONSTER = 1
TEAM_DEFIANCE_CHARACTER = 2
TEAM_TAX_COLLECTOR = 3
```

```js
ADMIN_CONSOLE_LOG = 0
ADMIN_CONSOLE_ERROR = 1
ADMIN_CONSOLE_INFO = 2
```

```js
EXCHANGE_NPC_SHOP = 0
EXCHANGE_CHARACTER_EXCHANGE = 1
EXCHANGE_NPC_EXCHANGE = 2
EXCHANGE_CRAFT = 3
EXCHANGE_OFFLINE_CHARACTER_SHOP_BUY = 4
EXCHANGE_STORAGE = 5
EXCHANGE_OFFLINE_CHARACTER_SHOP_SELL = 6
EXCHANGE_TAX_COLLECTOR_STORAGE = 8
EXCHANGE_NPC_EXCHANGE_PET = 9
EXCHANGE_AUCTION_HOUSE_SELL = 10
EXCHANGE_AUCTION_HOUSE_BUY = 11
EXCHANGE_MULTI_CRAFT_INVITE = 12
EXCHANGE_MULTI_CRAFT_ASK = 13
EXCHANGE_CRAFTSPERSON_LIST = 14
EXCHANGE_MOUNT_STORAGE = 15
EXCHANGE_MOUNT_MANAGEMENT = 16
EXCHANGE_NPC_RESURRECT_PET = 17
EXCHANGE_NPC_EXCHANGE_MOUNT = 18
```

```js
SPELL_POSITION_SHORTCUTS = (1 -> 23)
```

```js
CHANNEL_TEAM = "#"
CHANNEL_PARTY = "$"
CHANNEL_GUILD = "%"
CHANNEL_ALIGNMENT = "!"
CHANNEL_RECRUITMENT = "?"
CHANNEL_TRADING = ":"
CHANNEL_NOVICE = "^"
CHANNEL_ADMIN = "@"
CHANNEL_EVENT = "e"
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
function NEW_REMOTE_RESTRICTIONS() {
    var remoteRestrictions = {};
    remoteRestrictions.isTomb = false;
    remoteRestrictions.cantSwitchInCreatureMode = false;
    remoteRestrictions.isSlow = false;
    remoteRestrictions.forceWalk = false;
    remoteRestrictions.cantBeAttacked = false;
    remoteRestrictions.cantExchange = false;
    remoteRestrictions.cantBeChallenged = false;
    remoteRestrictions.cantBeAssaulted = false;
    return remoteRestrictions;
}
```

```js
function ENCODE_REMOTE_RESTRICTIONS(remoteRestrictions) {
    var encodedRemoteRestrictions = 0;
    encodedRemoteRestrictions |= remoteRestrictions.isTomb << 7;
    encodedRemoteRestrictions |= remoteRestrictions.cantSwitchInCreatureMode << 6;
    encodedRemoteRestrictions |= remoteRestrictions.isSlow << 5;
    encodedRemoteRestrictions |= remoteRestrictions.forceWalk << 4;
    encodedRemoteRestrictions |= remoteRestrictions.cantBeAttacked << 3;
    encodedRemoteRestrictions |= remoteRestrictions.cantExchange << 2;
    encodedRemoteRestrictions |= remoteRestrictions.cantBeChallenged << 1;
    encodedRemoteRestrictions |= remoteRestrictions.cantBeAssaulted;
    return encodedRemoteRestrictions;
}
```

```js
function DECODE_REMOTE_RESTRICTIONS(encodedRemoteRestrictions) {
    var remoteRestrictions = {};
    remoteRestrictions.isTomb = (encodedRemoteRestrictions >> 7) & 1;
    remoteRestrictions.cantSwitchInCreatureMode = (encodedRemoteRestrictions >> 6) & 1;
    remoteRestrictions.isSlow = (encodedRemoteRestrictions >> 5) & 1;
    remoteRestrictions.forceWalk = (encodedRemoteRestrictions >> 4) & 1;
    remoteRestrictions.cantBeAttacked = (encodedRemoteRestrictions >> 3) & 1;
    remoteRestrictions.cantExchange = (encodedRemoteRestrictions >> 2) & 1;
    remoteRestrictions.cantBeChallenged = (encodedRemoteRestrictions >> 1) & 1;
    remoteRestrictions.cantBeAssaulted = encodedRemoteRestrictions & 1;
    return remoteRestrictions;
}
```

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

## Network messages

### CreateCharacterResult

#### Header

```js
"AA"
```

#### Body

```js
FAILURE (ERROR_NAME_USED | ERROR_FULL | ERROR_INVALID_NAME | ERROR_SUBSCRIPTION | ERROR_OTHER)
```

```js
SUCCESS
```

#### Constants

```js
ERROR_NAME_USED = "a"
ERROR_FULL = "f"
ERROR_INVALID_NAME = "n"
ERROR_SUBSCRIPTION = "s"
ERROR_OTHER = EMPTY
```

---

### DeleteCharacterFailure

#### Header

```js
"AD"
```

#### Body

```js
FAILURE
```

---

### StartStoreService [RETRO]

#### Header

```js
"AE"
```

#### Body

```js
(EDIT_CHARACTER_COLORS | EDIT_CHARACTER_NAME) {FORCE}
```

```
MAKE_MIMIBIOTE
```

#### Constants

```js
EDIT_CHARACTER_COLORS = "c"
MAKE_MIMIBIOTE = "i"
EDIT_CHARACTER_NAME = "n"
```

```js
FORCE = "f"
```

---

### FriendServerList

#### Header

```js
"AF"
```

#### Body

```js
[server.id "," server.friendCharacterCount, ";"]
```

---

### GiftStored

#### Header

```js
"AG"
```

#### Body

```js
EMPTY
```

---

### AllServerList

#### Header

```js
"AH"
```

#### Body

```js
[server.id ";" (SERVER_OFFLINE | SERVER_ONLINE | SERVER_STARTING) ";" server.completionLevel ";" server.isSelectable, "|"]
```

#### Constants

```js
SERVER_OFFLINE = 0
SERVER_ONLINE = 1
SERVER_STARTING = 2
```

---

### ClientKey

#### Header

```js
"AK"
```

#### Body

```js
<keyId, 16> key
```

#### Parameters

```js
keyId = (0 -> 15)
```

---

### CharacterList

#### Header

```js
"AL"
```

#### Body

```js
SUCCESS remainingSubscriptionTimeInMilliseconds "|" characterCount {"|" [character.id ";" character.name ";" character.level ";" character.gfxId ";" (-1 | <character.color1, 16>) ";" (-1 | <character.color2, 16>) ";" (-1 | <character.color3, 16>) ";" character.accessories ";" character.hasShop ";" character.serverId ";" {character.isDead} ";" {character.deathCount} ";" {character.maxLevel}, "|"]}
```

---

### MigrantCharacterList

#### Header

```js
"AM"
```

#### Body

```js
SUCCESS remainingSubscriptionTimeInMilliseconds "|" characterCount {"|" [character.id ";" character.name ";" character.level ";" character.gfxId ";" (-1 | <character.color1, 16>) ";" (-1 | <character.color2, 16>) ";" (-1 | <character.color3, 16>) ";" character.accessories ";" character.hasShop ";" character.serverId ";" character.isDead ";" character.deathCount ";" character.maxLevel, "|"]}
```

---

### CanValidateMigrantCharacterSuccess

#### Header

```js
"AM?"
```

#### Body

```js
character.id ";" character.name
```

---

### CharacterLevelUp

#### Header

```js
"AN"
```

#### Body

```js
character.level
```

---

### RandomCharacterName

#### Header

```js
"AP"
```

#### Body

```js
FAILURE ERROR_CANT_GENERATE
```

```js
SUCCESS character.name
```

#### Constants

```js
ERROR_CANT_GENERATE = 2
```

---

### AccountSecretQuestion

#### Header

```js
"AQ"
```

#### Body

```js
ESCAPE(account.secretQuestion)
```

---

### CharacterRestrictions

#### Header

```js
"AR"
```

#### Body

```js
<ENCODE_LOCAL_RESTRICTIONS(character.restrictions), 36>
```

#### Functions

```js
function NEW_LOCAL_RESTRICTIONS() {
    var localRestrictions = {};
    localRestrictions.cantInteractWithPrism = false;
    localRestrictions.canAttackMonstersAnywhereWhenMutant = false;
    localRestrictions.canMoveInAllDirections = false;
    localRestrictions.canAttackDungeonMonstersWhenMutant = false;
    localRestrictions.cantInteractWithNpc = false;
    localRestrictions.cantUseInteractiveObjects = false;
    localRestrictions.cantInteractWithTaxCollector = false;
    localRestrictions.cantUseObject = false;
    localRestrictions.cantBeMerchant = false;
    localRestrictions.cantChatToAll = false;
    localRestrictions.canAttack = false;
    localRestrictions.cantExchange = false;
    localRestrictions.cantChallenge = false;
    localRestrictions.cantAssault = false;
    return localRestrictions;
}
```

```js
function ENCODE_LOCAL_RESTRICTIONS(localRestrictions) {
    var encodedLocalRestrictions = 0;
    encodedLocalRestrictions |= localRestrictions.cantInteractWithPrism << 15;
    encodedLocalRestrictions |= localRestrictions.canAttackMonstersAnywhereWhenMutant << 14;
    encodedLocalRestrictions |= localRestrictions.canMoveInAllDirections << 13;
    encodedLocalRestrictions |= localRestrictions.canAttackDungeonMonstersWhenMutant << 12;
    encodedLocalRestrictions |= localRestrictions.cantInteractWithNpc << 9;
    encodedLocalRestrictions |= localRestrictions.cantUseInteractiveObjects << 8;
    encodedLocalRestrictions |= localRestrictions.cantInteractWithTaxCollector << 7;
    encodedLocalRestrictions |= localRestrictions.cantUseObject << 6;
    encodedLocalRestrictions |= localRestrictions.cantBeMerchant << 5;
    encodedLocalRestrictions |= localRestrictions.cantChatToAll << 4;
    encodedLocalRestrictions |= localRestrictions.canAttack << 3;
    encodedLocalRestrictions |= localRestrictions.cantExchange << 2;
    encodedLocalRestrictions |= localRestrictions.cantChallenge << 1;
    encodedLocalRestrictions |= localRestrictions.cantAssault;
    return encodedLocalRestrictions;
}
```

```js
function DECODE_LOCAL_RESTRICTIONS(encodedLocalRestrictions) {
    var localRestrictions = {};
    localRestrictions.cantInteractWithPrism = (encodedLocalRestrictions >> 15) & 1;
    localRestrictions.canAttackMonstersAnywhereWhenMutant = (encodedLocalRestrictions >> 14) & 1;
    localRestrictions.canMoveInAllDirections = (encodedLocalRestrictions >> 13) & 1;
    localRestrictions.canAttackDungeonMonstersWhenMutant = (encodedLocalRestrictions >> 12) & 1;
    localRestrictions.cantInteractWithNpc = (encodedLocalRestrictions >> 9) & 1;
    localRestrictions.cantUseInteractiveObjects = (encodedLocalRestrictions >> 8) & 1;
    localRestrictions.cantInteractWithTaxCollector = (encodedLocalRestrictions >> 7) & 1;
    localRestrictions.cantUseObject = (encodedLocalRestrictions >> 6) & 1;
    localRestrictions.cantBeMerchant = (encodedLocalRestrictions >> 5) & 1;
    localRestrictions.cantChatToAll = (encodedLocalRestrictions >> 4) & 1;
    localRestrictions.canAttack = (encodedLocalRestrictions >> 3) & 1;
    localRestrictions.cantExchange = (encodedLocalRestrictions >> 2) & 1;
    localRestrictions.cantChallenge = (encodedLocalRestrictions >> 1) & 1;
    localRestrictions.cantAssault = encodedLocalRestrictions & 1;
    return localRestrictions;
}
```

---

### SelectCharacterResult

#### Header

```js
"AS"
```

#### Body

```js
FAILURE
```

```js
SUCCESS "|" character.id "|" character.name "|" character.level "|" character.raceId "|" character.isFemale "|" character.gfxId "|" (-1 | <character.color1, 16>) "|" (-1 | <character.color2, 16>) "|" (-1 | <character.color3, 16>) "|" [{character.item}, ";"] {";"}
```

---

### ClientTicketResult

#### Header

```js
"AT"
```

#### Body

```js
FAILURE
```

```js
SUCCESS <keyId, 16> {key}
```

#### Parameters

```js
keyId = (0 -> 15)
```

---

### RegionalVersion

#### Header

```js
"AV"
```

#### Body

```js
regionalVersion
```

---

### SelectServerResult

#### Header

```js
"AX"
```

#### Body

```js
FAILURE (ERROR_FULL_HEROIC | ERROR_DOWN | ERROR_CANT_SELECT)
```

```js
FAILURE ERROR_FULL [server.id, "|"]
```

```js
FAILURE ERROR_CANT_SELECT_CHARACTER server.id
```

```js
SUCCESS ENCODE_IP(server.ip) ENCODE_PORT(server.port) ticket
```

#### Constants

```js
ERROR_FULL_HEROIC = "F"
ERROR_DOWN = "d"
ERROR_FULL = "f"
ERROR_CANT_SELECT = "r"
ERROR_CANT_SELECT_CHARACTER = "s"
```

#### Functions

```js
function ENCODE_IP(ip) {
    var parts = ip.split(".");
    var encodedIp = "";
    for (var i = 0; i < 4; i++) {
        var e0 = (parts[i] & ((1 << 7) | (1 << 6) | (1 << 5) | (1 << 4))) >> 4;
        var e1 = parts[i] & ((1 << 3) | (1 << 2) | (1 << 1) | 1);
        encodedIp += fromCharCode(e0 + 48) + fromCharCode(e1 + 48);
    }
    return encodedIp;
}
```

```js
function DECODE_IP(encodedIp) {
    var parts = [];
    for (var i = 0; i < 8; i += 2) {
        var e0 = encodedIp.charCodeAt(i) - 48;
        var e1 = encodedIp.charCodeAt(i + 1) - 48;
        var part = (e0 << 4) & ((1 << 7) | (1 << 6) | (1 << 5) | (1 << 4));
        part |= e1 & ((1 << 3) | (1 << 2) | (1 << 1) | 1);
        parts.push(part);
    }
    var ip = parts.join(".");
    return ip;
}
```

```js
function ENCODE_PORT(port) {
    var e0 = (port & ((1 << 17) | (1 << 16) | (1 << 15) | (1 << 14) | (1 << 13) | (1 << 12))) >> 12;
    var e1 = (port & ((1 << 11) | (1 << 10) | (1 << 9) | (1 << 8) | (1 << 7) | (1 << 6))) >> 6;
    var e2 = port & ((1 << 5) | (1 << 4) | (1 << 3) | (1 << 2) | (1 << 1) | 1);
    var encodedPort = ENCODE_64(e0) + ENCODE_64(e1) + ENCODE_64(e2);
    return encodedPort;
}
```

```js
function DECODE_PORT(encodedPort) {
    var e0 = DECODE_64(encodedPort.charAt(0));
    var e1 = DECODE_64(encodedPort.charAt(1));
    var e2 = DECODE_64(encodedPort.charAt(2));
    var port = ((e0 << 12) & ((1 << 17) | (1 << 16) | (1 << 15) | (1 << 14) | (1 << 13) | (1 << 12)));
    port |= ((e1 << 6) & ((1 << 11) | (1 << 10) | (1 << 9) | (1 << 8) | (1 << 7) | (1 << 6)));
    port |= (e2 & ((1 << 5) | (1 << 4) | (1 << 3) | (1 << 2) | (1 << 1) | 1));
    return port;
}
```

---

### PlainSelectServerResult

#### Header

```js
"AY"
```

#### Body

```js
FAILURE (ERROR_FULL_HEROIC | ERROR_DOWN | ERROR_CANT_SELECT)
```

```js
FAILURE ERROR_FULL [server.id, "|"]
```

```js
FAILURE ERROR_CANT_SELECT_CHARACTER server.id
```

```js
SUCCESS server.ip ":" server.port ";" ticket
```

#### Parameters

```js
ticket = '[a-z\d]{6}'
```

#### Constants

```js
ERROR_FULL_HEROIC = "F"
ERROR_DOWN = "d"
ERROR_FULL = "f"
ERROR_CANT_SELECT = "r"
ERROR_CANT_SELECT_CHARACTER = "s"
```

---

### AccountCommunity

#### Header

```js
"Ac"
```

#### Body

```js
account.communityId
```

---

### AccountNickname

#### Header

```js
"Ad"
```

#### Body

```js
account.nickname
```

---

### QueueDetails

#### Header

```js
"Af"
```

#### Body

```js
position "|" queue.totalSubscribers "|" queue.totalNonSubscribers "|" {isSubscriber} "|" queue.id
```

---

### GiftList

#### Header

```js
"Ag"
```

#### Body

```js
GIFT_TYPE "|" gift.id "|" gift.title "|" gift.description "|" gift.gfxUrl "|" [gift.item, ";"]
```

#### Constants

```js
GIFT_TYPE = 1
```

---

### AccountLoginResult

#### Header

```js
"Al"
```

#### Body

```js
FAILURE (ERROR_LOGGED | ERROR_BANNED | ERROR_LOGGED_GAME | ERROR_DISCONNECTED | ERROR_ACCOUNT_IN_MAINTENANCE | ERROR_INCOMPLETE | ERROR_INVALID_LOGIN | ERROR_CHOOSE_NICKNAME | ERROR_NICKNAME_USED | ERROR_SERVER_FULL | ERROR_WRONG_LOGIN)
```

```js
FAILURE ERROR_TEMPORARY_BANNED invalidTime.days "|" invalidTime.hours "|" invalidTime.minutes
```

```js
FAILURE ERROR_INVALID_VERSION requiredVersion
```

```js
SUCCESS account.isAdmin
```

#### Constants

```js
ERROR_LOGGED = "a"
ERROR_BANNED = "b"
ERROR_LOGGED_GAME = "c"
ERROR_DISCONNECTED = "d"
ERROR_TEMPORARY_BANNED = "k"
ERROR_ACCOUNT_IN_MAINTENANCE = "m"
ERROR_INCOMPLETE = "n"
ERROR_INVALID_LOGIN = "p"
ERROR_CHOOSE_NICKNAME = "r"
ERROR_NICKNAME_USED = "s"
ERROR_INVALID_VERSION = "v"
ERROR_SERVER_FULL = "w"
ERROR_WRONG_LOGIN = EMPTY
```

---

### FirstConnectionInfo

#### Header

```js
"Am"
```

#### Body

```js
EMPTY
```

---

### QueuePosition

#### Header

```js
"Aq"
```

#### Body

```js
position
```

---

### RescueCharacterResult

#### Header

```js
"Ar"
```

#### Body

```js
FAILURE
```

```js
SUCCESS
```

---

### CharacterStats

#### Header

```js
"As"
```

#### Body

```js
character.totalXp "," character.levelXp "," character.nextLevelXp
"|" character.moneyAmount
"|" character.statPoints
"|" character.spellPoints
"|" character.alignmentId {"~" character.fakeAlignmentId} "," character.alignmentLevel "," character.alignmentRank "," character.alignmentHonor "," character.alignmentDisgrace "," character.isAlignmentEnabled
"|" character.lp "," character.maxLp
"|" character.energy "," character.maxEnergy
"|" character.initiative
"|" character.prospecting
"|" character.apBase "," character.apStuff "," character.apGift "," character.apBoost
"|" character.mpBase "," character.mpStuff "," character.mpGift "," character.mpBoost
"|" character.strengthBase "," character.strengthStuff "," character.strengthGift "," character.strengthBoost
"|" character.vitalityBase "," character.vitalityStuff "," character.vitalityGift "," character.vitalityBoost
"|" character.wisdomBase "," character.wisdomStuff "," character.wisdomGift "," character.wisdomBoost
"|" character.chanceBase "," character.chanceStuff "," character.chanceGift "," character.chanceBoost
"|" character.agilityBase "," character.agilityStuff "," character.agilityGift "," character.agilityBoost
"|" character.intelligenceBase "," character.intelligenceStuff "," character.intelligenceGift "," character.intelligenceBoost
"|" character.rangeBase "," character.rangeStuff "," character.rangeGift "," character.rangeBoost
"|" character.maxSummonedCountBase "," character.maxSummonedCountStuff "," character.maxSummonedCountGift "," character.maxSummonedCountBoost
"|" character.damageBonusBase "," character.damageBonusStuff "," character.damageBonusGift "," character.damageBonusBoost
"|" character.physicalDamageBonusBase "," character.physicalDamageBonusStuff "," character.physicalDamageBonusGift "," character.physicalDamageBonusBoost
"|" character.weaponDamagePercentBonusBase "," character.weaponDamagePercentBonusStuff "," character.weaponDamagePercentBonusGift "," character.weaponDamagePercentBonusBoost
"|" character.damagePercentBonusBase "," character.damagePercentBonusStuff "," character.damagePercentBonusGift "," character.damagePercentBonusBoost
"|" character.healBonusBase "," character.healBonusStuff "," character.healBonusGift "," character.healBonusBoost
"|" character.trapBonusBase "," character.trapBonusStuff "," character.trapBonusGift "," character.trapBonusBoost
"|" character.trapPercentBonusBase "," character.trapPercentBonusStuff "," character.trapPercentBonusGift "," character.trapPercentBonusBoost
"|" character.returnedDamageBase "," character.returnedDamageStuff "," character.returnedDamageGift "," character.returnedDamageBoost
"|" character.criticalHitBonusBase "," character.criticalHitBonusStuff "," character.criticalHitBonusGift "," character.criticalHitBonusBoost
"|" character.criticalFailureBonusBase "," character.criticalFailureBonusStuff "," character.criticalFailureBonusGift "," character.criticalFailureBonusBoost
"|" character.dodgeApLossBase "," character.dodgeApLossStuff "," character.dodgeApLossGift "," character.dodgeApLossBoost
"|" character.dodgeMpLossBase "," character.dodgeMpLossStuff "," character.dodgeMpLossGift "," character.dodgeMpLossBoost
"|" character.neutralResistanceBase "," character.neutralResistanceStuff "," character.neutralResistanceGift "," character.neutralResistanceBoost
"|" character.neutralResistancePercentBase "," character.neutralResistancePercentStuff "," character.neutralResistancePercentGift "," character.neutralResistancePercentBoost
"|" character.pvpNeutralResistanceBase "," character.pvpNeutralResistanceStuff "," character.pvpNeutralResistanceGift "," character.pvpNeutralResistanceBoost
"|" character.pvpNeutralResistancePercentBase "," character.pvpNeutralResistancePercentStuff "," character.pvpNeutralResistancePercentGift "," character.pvpNeutralResistancePercentBoost
"|" character.earthResistanceBase "," character.earthResistanceStuff "," character.earthResistanceGift "," character.earthResistanceBoost
"|" character.earthResistancePercentBase "," character.earthResistancePercentStuff "," character.earthResistancePercentGift "," character.earthResistancePercentBoost
"|" character.pvpEarthResistanceBase "," character.pvpEarthResistanceStuff "," character.pvpEarthResistanceGift "," character.pvpEarthResistanceBoost
"|" character.pvpEarthResistancePercentBase "," character.pvpEarthResistancePercentStuff "," character.pvpEarthResistancePercentGift "," character.pvpEarthResistancePercentBoost
"|" character.waterResistanceBase "," character.waterResistanceStuff "," character.waterResistanceGift "," character.waterResistanceBoost
"|" character.waterResistancePercentBase "," character.waterResistancePercentStuff "," character.waterResistancePercentGift "," character.waterResistancePercentBoost
"|" character.pvpWaterResistanceBase "," character.pvpWaterResistanceStuff "," character.pvpWaterResistanceGift "," character.pvpWaterResistanceBoost
"|" character.pvpWaterResistancePercentBase "," character.pvpWaterResistancePercentStuff "," character.pvpWaterResistancePercentGift "," character.pvpWaterResistancePercentBoost
"|" character.airResistanceBase "," character.airResistanceStuff "," character.airResistanceGift "," character.airResistanceBoost
"|" character.airResistancePercentBase "," character.airResistancePercentStuff "," character.airResistancePercentGift "," character.airResistancePercentBoost
"|" character.pvpAirResistanceBase "," character.pvpAirResistanceStuff "," character.pvpAirResistanceGift "," character.pvpAirResistanceBoost
"|" character.pvpAirResistancePercentBase "," character.pvpAirResistancePercentStuff "," character.pvpAirResistancePercentGift "," character.pvpAirResistancePercentBoost
"|" character.fireResistanceBase "," character.fireResistanceStuff "," character.fireResistanceGift "," character.fireResistanceBoost
"|" character.fireResistancePercentBase "," character.fireResistancePercentStuff "," character.fireResistancePercentGift "," character.fireResistancePercentBoost
"|" character.pvpFireResistanceBase "," character.pvpFireResistanceStuff "," character.pvpFireResistanceGift "," character.pvpFireResistanceBoost
"|" character.pvpFireResistancePercentBase "," character.pvpFireResistancePercentStuff "," character.pvpFireResistancePercentGift "," character.pvpFireResistancePercentBoost
{"|" ?}
```

---

### OwnServerList

#### Header

```js
"Ax"
```

#### Body

```js
SUCCESS remainingSubscriptionTimeInMilliseconds "|" [server.id "," server.characterCount, "|"]
```

---

### ClearAdminConsole

#### Header

```js
"BAC"
```

#### Body

```js
EMPTY
```

---

### RemoveAdminRights

#### Header

```js
"BAIC"
```

#### Body

```js
remover.name
```

---

### GiveAdminRights

#### Header

```js
"BAIO"
```

#### Body

```js
giver.name
```

---

### UpdateAdminConsoleMessage

#### Header

```js
"BAL"
```

#### Body

```js
reversedIndex "|" (ADMIN_CONSOLE_LOG | ADMIN_CONSOLE_ERROR | ADMIN_CONSOLE_INFO) "|" adminConsoleText
```

---

### AdminConsolePrompt

#### Header

```js
"BAP"
```

#### Body

```js
prompt
```

---

### AdminConsoleMessage

#### Header

```js
"BAT"
```

#### Body

```js
(ADMIN_CONSOLE_LOG | ADMIN_CONSOLE_ERROR | ADMIN_CONSOLE_INFO) adminConsoleText
```

RETRO:

```js
(ADMIN_CONSOLE_LOG | ADMIN_CONSOLE_ERROR | ADMIN_CONSOLE_INFO) "|" "|" "|" adminConsoleText
```

---

### BasicCheckFile

#### Header

```js
"BC"
```

#### Body

```js
checkId ";" CELL_COLOR (REMOVE_ALL | (REMOVE [cell.id, "."]) | ([cell.id, "."] "/" <color, 16>))
```

```js
checkId ";" filePath
```

#### Constants

```js
CELL_COLOR = "bright.swf"
```

```js
REMOVE_ALL = 0
```

---

### BasicDate

#### Header

```js
"BD"
```

#### Body

```js
<date.year - 1370> "|" <date.month - 1> "|" date.day
```

---

### BasicPopupMessage [RETRO]

#### Header

```js
"BM"
```

#### Body

```js
text
```

---

### BasicNoResponse

#### Header

```js
"BN"
```

#### Body

```js
EMPTY
```

---

### BasicSubscriberZone

#### Header

```js
"BP"
```

#### Body

```js
ENABLE {SUBSCRIPTION_LOCK}
```

```js
DISABLE
```

---

### Constants

```js
SUBSCRIPTION_LOCK = 10
```

---

### BasicReferenceTime

#### Header

```js
"BT"
```

#### Body

```js
referenceTimestamp
```

---

### BasicWhoIsResult

#### Header

```js
"BW"
```

#### Body

```js
FAILURE (character.name | account.nickname)
```

```js
SUCCESS (localAccount.login | remoteAccount.nickname) "|" (STATE_NOT_IN_FIGHT | STATE_IN_FIGHT) "|" character.name "|" character.areaId
```

#### Constants

```js
STATE_NOT_IN_FIGHT = 1
STATE_IN_FIGHT = 2
```

---

### GetBasicAveragePing

#### Header

```js
"Bp"
```

#### Body

```js
EMPTY
```

---

### PrismAttackedInfo

#### Header

```js
"CA"
```

#### Body

```js
prism.mapId "|" prism.mapX "|" prism.mapY
```

---

### AlignedConquestAreaModifier

#### Header

```js
"CB"
```

#### Body

```js
bonus.xpPercent "," bonus.dropPercent "," bonus.harvestPercent ";" bonus.xpRankMultiplicator "," bonus.dropRankMultiplicator "," bonus.harvestRankMultiplicator ";" malus.xpPercent "," malus.dropPercent "," malus.harvestPercent
```

---

### PrismDeadInfo

#### Header

```js
"CD"
```

#### Body

```js
prism.mapId "|" prism.mapX "|" prism.mapY
```

---

### PrismDefenseDetails

#### Header

```js
"CIJ"
```

#### Body

```js
JOIN_CAN ";" remainingTimerInMilliseconds ";" totalTimerInMilliseconds ";" maxTeamSlotCount
```

```js
(JOIN_CANT_NO_FIGHT | JOIN_CANT_IN_FIGHT | JOIN_CANT_NO_PRISM)
```

#### Constants

```js
JOIN_CAN = 0
JOIN_CANT_NO_FIGHT = -1
JOIN_CANT_IN_FIGHT = -2
JOIN_CANT_NO_PRISM = -3
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

### UpdatePrismDefenseDefenderList

#### Header

```js
"CP"
```

#### Body

```js
ADD "|" [<defender.id, 36> ";" defender.name ";" defender.gfxId ";" defender.level ";" (-1 | <defender.color1, 36>) ";" (-1 | <defender.color2, 36>) ";" (-1 | <defender.color3, 36>) ";" defender.isReservist, "|"]
```

```js
REMOVE "|" [<defender.id, 36>, "|"]
```

---

### PrismSurvivedInfo

#### Header

```js
"CS"
```

#### Body

```js
prism.mapId "|" prism.mapX "|" prism.mapY
```

---

### ConquestAreaList

#### Header

```js
"CW"
```

#### Body

```js
world.ownedAreas "|" world.totalAreas "|" world.possibleAreas "|" [{area.id "," area.alignmentId "," area.isFighting "," area.prismMapId "," area.isAttackable}, ";"] "|" world.ownedVillages "|" world.totalVillages "|" [village.id "," village.alignmentId "," village.isDoorOpen "," village.isPrismDoorOpen, ";"]
```

---

### ConquestBalance

#### Header

```js
"Cb"
```

#### Body

```js
world.balancePercent ";" area.balancePercent
```

---

### UpdatePrismDefenseAttackerList

#### Header

```js
"Cp"
```

#### Body

```js
ADD "|" [<attacker.id, 36> ";" attacker.name ";" attacker.level, "|"]
```

```js
REMOVE "|" [<attacker.id, 36>, "|"]
```

---

### StartNpcDialogSuccess

#### Header

```js
"DC"
```

#### Body

```js
SUCCESS npc.id
```

---

### PauseNpcDialog

#### Header

```js
"DP"
```

#### Body

```js
EMPTY
```

---

### NpcDialogQuestion

#### Header

```js
"DQ"
```

#### Body

```js
question.id ";" [question.param, ","] "|" [response.id, ";"]
```

---

### CloseNpcDialog

#### Header

```js
"DV"
```

#### Body

```js
EMPTY
```

---

### CraftLoopInfo

#### Header

```js
"EA"
```

#### Body

```js
remainingItemCount
```

---

### ExchangeBuyResult

#### Header

```js
"EB"
```

#### Body

```js
FAILURE
```

```js
SUCCESS
```

---

### StartExchange

#### Header

```js
"EC"
```

#### Body

```js
SUCCESS (EXCHANGE_NPC_SHOP | EXCHANGE_OFFLINE_CHARACTER_SHOP_BUY) "|" entity.id
```

```js
SUCCESS EXCHANGE_CHARACTER_EXCHANGE
```

```js
SUCCESS (EXCHANGE_NPC_EXCHANGE | EXCHANGE_NPC_EXCHANGE_PET | EXCHANGE_NPC_RESURRECT_PET | EXCHANGE_NPC_EXCHANGE_MOUNT) "|" npc.id
```

```js
SUCCESS EXCHANGE_CRAFT "|" maxSlotCount ";" skill.id
```

```js
SUCCESS EXCHANGE_STORAGE
```

```js
SUCCESS EXCHANGE_OFFLINE_CHARACTER_SHOP_SELL
```

```js
SUCCESS EXCHANGE_TAX_COLLECTOR_STORAGE "|" taxCollector.id
```

```js
SUCCESS (EXCHANGE_AUCTION_HOUSE_SELL | EXCHANGE_AUCTION_HOUSE_BUY) "|" auctionHouse.lot1Quantity "," auctionHouse.lot2Quantity "," auctionHouse.lot3Quantity ";" [auctionHouse.itemTypeId, ","] ";" auctionHouse.taxPercent ";" auctionHouse.maxItemLevel ";" auctionHouse.maxItemCount ";" auctionHouse.npcId ";" auctionHouse.maxSellTimeInHours
```

```js
SUCCESS (EXCHANGE_MULTI_CRAFT_INVITE | EXCHANGE_MULTI_CRAFT_ASK) "|" maxSlotCount ";" skill.id
```

```js
SUCCESS EXCHANGE_CRAFTSPERSON_LIST "|" [job.id, ";"]
```

```js
SUCCESS EXCHANGE_MOUNT_STORAGE
```

```js
SUCCESS EXCHANGE_MOUNT_MANAGEMENT "|" [stable.mount, ";"] "~" [paddock.mount, ";"]
```

---

### AuctionHouseItemList

#### Header

```js
"EHL"
```

#### Body

```js
item.typeId "|" [item.modelId, ";"]
```

---

### UpdateAuctionHouseItemList

#### Header

```js
"EHM"
```

#### Body

```js
(ADD | REMOVE) item.modelId
```

---

### AuctionHouseItemAveragePrice

#### Header

```js
"EHP"
```

#### Body

```js
item.modelId "|" price
```

---

### SearchAuctionHouseResult

#### Header

```js
"EHS"
```

#### Body

```js
FAILURE
```

```js
SUCCESS
```

---

### AuctionHouseEntryList

#### Header

```js
"EHl"
```

#### Body

```js
entry.itemModelId {"|" [entry.id ";" entry.itemEffects ";" entry.lot1Price ";" entry.lot2Price ";" entry.lot3Price, "|"]}
```

---

### UpdateAuctionHouseEntryList

#### Header

```js
"EHm"
```

#### Body

```js
(ADD | REMOVE) entry.id "|" entry.itemModelId "|" entry.itemEffects "|" entry.lot1Price "|" entry.lot2Price "|" entry.lot3Price
```

---

### UpdateJobCraftspersonList

#### Header

```js
"EJ"
```

#### Body

```js
ADD_UPDATE job.id ";" craftsperson.id ";" craftsperson.name ";" craftsperson.jobLevel ";" craftsperson.mapId ";" craftsperson.isInWorkshop ";" craftsperson.raceId ";" craftsperson.isFemale ";" (-1 | craftsperson.color1) "," (-1 | craftsperson.color2) "," (-1 | craftsperson.color3) ";" {craftsperson.accessories} ";" craftsperson.jobOptions "," craftsperson.jobMinSlotCount
```

```js
REMOVE craftsperson.jobId ";" craftsperson.id
```

---

### ValidateExchangeState

#### Header

```js
"EK"
```

#### Body

```js
isReady entity.id
```

---

### ExchangeContentList

#### Header

```js
"EL"
```

#### Body

EXCHANGE_NPC_SHOP:

```js
[item.modelId ";" item.effects, "|"]
```

EXCHANGE_OFFLINE_CHARACTER_SHOP_BUY:

EXCHANGE_OFFLINE_CHARACTER_SHOP_SELL:

```js
[item.id ";" item.quantity ";" item.modelId ";" item.effects ";" item.price, "|"]
```

EXCHANGE_STORAGE:

EXCHANGE_TAX_COLLECTOR_STORAGE:

EXCHANGE_MOUNT_STORAGE:

```js
[((EXCHANGE_MONEY moneyAmount) | (EXCHANGE_ITEM item)), ";"]
```

EXCHANGE_AUCTION_HOUSE_SELL:

```js
[item.id ";" item.quantity ";" item.modelId ";" item.effects ";" item.price ";" item.remainingHours, "|"]
```

---

### UpdateLocalExchangeContentList

#### Header

```js
"EM"
```

#### Body

```js
SUCCESS EXCHANGE_MONEY moneyAmount
```

```js
SUCCESS EXCHANGE_ITEM ADD_UPDATE item.id "|" item.quantity
```

```js
SUCCESS EXCHANGE_ITEM REMOVE item.id
```

---

### RequestExchangeResult

#### Header

```js
"ER"
```

#### Body

```js
FAILURE (ERROR_UNABLE | ERROR_EQUIPPED_TOOL | ERROR_ALREADY | ERROR_SUBSCRIPTION | ERROR_NOT_NEAR_CRAFT_TABLE | ERROR_OVERLOAD)
```

```js
SUCCESS asker.id "|" asked.id "|" (WAIT_EXCHANGE | WANT_EXCHANGE | WAIT_CRAFT_CLIENT | WANT_CRAFT_ARTISAN | WAIT_CRAFT_ARTISAN | WANT_CRAFT_CLIENT)
```

#### Constants

```js
(WAIT_EXCHANGE | WANT_EXCHANGE) = 1
(WAIT_CRAFT_CLIENT | WANT_CRAFT_ARTISAN) = 12
(WAIT_CRAFT_ARTISAN | WANT_CRAFT_CLIENT) = 13
```

```js
ERROR_UNABLE = "I"
ERROR_EQUIPPED_TOOL = "J"
ERROR_ALREADY = "O"
ERROR_SUBSCRIPTION = "S"
ERROR_NOT_NEAR_CRAFT_TABLE = "T"
ERROR_OVERLOAD = "o"
```

---

### ExchangeSellResult

#### Header

```js
"ES"
```

#### Body

```js
FAILURE
```

```js
SUCCESS
```

---

### LeaveExchange

#### Header

```js
"EV"
```

#### Body

```js
(EXCHANGE_DONE | EXCHANGE_CANCELED)
```

#### Constants

```js
EXCHANGE_DONE = "a"
EXCHANGE_CANCELED = EMPTY
```

---

### CraftPublicModeOption

#### Header

```js
"EW"
```

#### Body

```js
(ENABLE | DISABLE)
```

```js
ENABLE craftsperson.id "|" [craftsperson.skillId, ";"]
```

```js
DISABLE craftsperson.id
```

---

### FinishCraftLoop

#### Header

```js
"Ea"
```

#### Body

```js
(RESULT_OK | RESULT_INTERRUPT | RESULT_FAIL | RESULT_INVALID)
```

#### Constants

```js
RESULT_OK = 1
RESULT_INTERRUPT = 2
RESULT_FAIL = 3
RESULT_INVALID = 4
```

---

### CraftResult

#### Header

```js
"Ec"
```

#### Body

```js
FAILURE (ERROR_FAILED | ERROR_NO_RESULT)
```

```js
SUCCESS ";" item.modelId {";" (REMOTE_FOR_LOCAL | LOCAL_FOR_REMOTE) remote.name ";" item.effects}
```

#### Constants

```js
ERROR_FAILED = "F"
ERROR_NO_RESULT = "I"
```

```js
REMOTE_FOR_LOCAL = "B"
LOCAL_FOR_REMOTE = "T"
```

---

### UpdateStableMountList

#### Header

```js
"Ee"
```

#### Body

```js
(ADD | ADD_NEW_BORN) mount
```

```js
REMOVE mount.id
```

#### Constants

```js
ADD_NEW_BORN = "~"
```

---

### UpdatePaddockMountList

#### Header

```js
"Ef"
```

#### Body

```js
ADD mount
```

```js
REMOVE mount.id
```

---

### UpdateOfflineCharacterShopItemList

#### Header

```js
"Ei"
```

#### Body

```js
SUCCESS ADD_UPDATE item.id "|" item.quantity "|" item.modelId "|" item.effects "|" item.price
```

```js
SUCCESS REMOVE item.id
```

---

### CraftReferenceInfo

#### Header

```js
"Ej"
```

#### Body

```js
(ADD | REMOVE) job.id
```

---

### UpdateRemoteExchangeContentList

#### Header

```js
"Em"
```

#### Body

EXCHANGE_CHARACTER_EXCHANGE:

EXCHANGE_NPC_EXCHANGE:

EXCHANGE_CRAFT:

EXCHANGE_NPC_EXCHANGE_PET:

EXCHANGE_MULTI_CRAFT_INVITE:

EXCHANGE_MULTI_CRAFT_ASK:

```js
SUCCESS EXCHANGE_MONEY moneyAmount
```

```js
SUCCESS EXCHANGE_ITEM ADD_UPDATE item.id "|" item.quantity "|" item.modelId "|" item.effects
```

```js
SUCCESS EXCHANGE_ITEM REMOVE item.id
```

EXCHANGE_AUCTION_HOUSE_SELL:

```js
SUCCESS ADD_UPDATE item.id "|" item.quantity "|" item.modelId "|" item.effects "|" item.price "|" item.remainingHours
```

```js
SUCCESS REMOVE item.id
```

---

### UpdatePaymentContentList

#### Header

```js
"Ep"
```

#### Body

EXCHANGE_MULTI_CRAFT_INVITE:

```js
(PAYMENT_BASE | PAYMENT_SUCCESS_BONUS) "|" EXCHANGE_MONEY moneyAmount
```

```js
(PAYMENT_BASE | PAYMENT_SUCCESS_BONUS) "|" EXCHANGE_ITEM ADD_UPDATE item.id "|" item.quantity "|" item.modelId "|" item.effects
```

```js
(PAYMENT_BASE | PAYMENT_SUCCESS_BONUS) "|" EXCHANGE_ITEM REMOVE item.id
```

EXCHANGE_MULTI_CRAFT_ASK:

```js
(PAYMENT_BASE | PAYMENT_SUCCESS_BONUS) "|" EXCHANGE_MONEY moneyAmount
```

```js
(PAYMENT_BASE | PAYMENT_SUCCESS_BONUS) "|" EXCHANGE_ITEM ADD_UPDATE item.id "|" item.quantity
```

```js
(PAYMENT_BASE | PAYMENT_SUCCESS_BONUS) "|" EXCHANGE_ITEM REMOVE item.id
```

#### Constants

```js
PAYMENT_BASE = 1
PAYMENT_SUCCESS_BONUS = 2
```

---

### OfflineCharacterShopTax

#### Header

```js
"Eq"
```

#### Body

```js
{itemTotalPrice} "|" <taxPercent * 10> "|" taxCost
```

---

### UpdateMultiCraftContentList

#### Header

```js
"Er"
```

#### Body

EXCHANGE_MULTI_CRAFT_INVITE:

EXCHANGE_MULTI_CRAFT_ASK:

```js
SUCCESS EXCHANGE_MONEY moneyAmount
```

```js
SUCCESS EXCHANGE_ITEM ADD_UPDATE item.id "|" item.quantity "|" item.modelId "|" item.effects
```

```js
SUCCESS EXCHANGE_ITEM REMOVE item.id
```

---

### UpdateStorageContentList

#### Header

```js
"Es"
```

#### Body

```js
SUCCESS EXCHANGE_MONEY moneyAmount
```

```js
SUCCESS EXCHANGE_ITEM ADD_UPDATE item.id "|" item.quantity "|" item.modelId "|" item.effects
```

```js
SUCCESS EXCHANGE_ITEM REMOVE item.id
```

---

### MountInventoryWeight

#### Header

```js
"Ew"
```

#### Body

```js
mount.pods ";" mount.maxPods
```

---

### AddFriendResult

#### Header

```js
"FA"
```

#### Body

```js
FAILURE (ERROR_ALREADY | ERROR_NOT_FOUND | ERROR_FULL | ERROR_YOURSELF)
```

```js
SUCCESS friend
```

#### Constants

```js
ERROR_ALREADY = "a"
ERROR_NOT_FOUND = "f"
ERROR_FULL = "m"
ERROR_YOURSELF = "y"
```

---

### RemoveFriendResult

#### Header

```js
"FD"
```

#### Body

```js
FAILURE ERROR_NOT_FOUND
```

```js
SUCCESS
```

#### Constants

```js
ERROR_NOT_FOUND = "f"
```

---

### FriendList

#### Header

```js
"FL"
```

#### Body

```js
"|" [friend, "|"]
```

---

### NotifyFriendConnectionOption

#### Header

```js
"FO"
```

#### Body

```js
(ENABLE | DISABLE)
```

---

### SpouseDetails

#### Header

```js
"FS"
```

#### Body

```js
spouse.name "|" spouse.gfxId "|" (-1 | spouse.color1) "|" (-1 | spouse.color2) "|" (-1 | spouse.color3) "|" spouse.mapId "|" spouse.level "|" spouse.isInFight "|" spouse.isFollowed
```

---

### GameAction

#### Header

```js
"GA"
```

#### Body

```js
";" ACTION_NO
```

```js
{action.id} ";" ACTION_SPRITE_MOVE ";" sprite.id ";" ENCODE_PATH(path)
```

```js
{action.id} ";" ACTION_SHOW_LOADING_MAP_OR_CINEMATIC ";" {entity.id} {";" cinematic.id}
```

```js
{action.id} ";" ACTION_SPRITE_SET_POSITION ";" {entity.id} ";" sprite.id "," sprite.cellId
```

```js
{action.id} ";" ACTION_SPRITE_SLIDE_STRAIGHT ";" {entity.id} ";" sprite.id "," sprite.cellId
```

```js
{action.id} ";" ACTION_SPRITE_SET_DIRECTION ";" {entity.id} ";" sprite.id "," sprite.directionId
```

```js
{action.id} ";" ACTION_SPRITE_CARRY_START ";" carrier.id ";" carried.id
```

```js
{action.id} ";" ACTION_SPRITE_CARRY_LAUNCH ";" carrier.id ";" carried.cellId
```

```js
{action.id} ";" ACTION_SPRITE_CARRY_STOP ";" {entity.id} ";" carried.id "," carried.cellId
```

```js
{action.id} ";" (ACTION_SPRITE_UPDATE_MP | ACTION_SPRITE_UPDATE_MP_USED) ";" {entity.id} ";" sprite.id "," mpDifference
```

```js
{action.id} ";" ACTION_SPRITE_UPDATE_LP ";" {entity.id} ";" sprite.id "," lpDifference
```

```js
{action.id} ";" (ACTION_SPRITE_UPDATE_AP | ACTION_SPRITE_UPDATE_AP_USED) ";" {entity.id} ";" sprite.id "," apDifference
```

```js
{action.id} ";" ACTION_SPRITE_DIE ";" killer.id ";" killed.id
```

```js
{action.id} ";" ACTION_SPRITE_CANT_MOVE ";" sprite.id
```

```js
{action.id} ";" (ACTION_FIGHT_REDUCE_DAMAGE | ACTION_FIGHT_REDUCE_DAMAGE_PERCENT) ";" {entity.id} ";" reducer.id "," reducedDamage
```

```js
{action.id} ";" ACTION_FIGHT_RETURN_SPELL ";" {entity.id} ";" returner.id "," spell.isReturned
```

```js
{action.id} ";" ACTION_FIGHT_RETURN_DAMAGE ";" {entity.id} ";" returner.id "," returnedDamage
```

```js
{action.id} ";" (ACTION_SPRITE_ADD_EFFECT_DAMAGE_BONUS | ACTION_SPRITE_ADD_EFFECT_DAMAGE_MULTIPLICATOR | ACTION_SPRITE_ADD_EFFECT_CRITICAL_HIT_BONUS | ACTION_SPRITE_ADD_EFFECT_RANGE_MALUS | ACTION_SPRITE_ADD_EFFECT_RANGE_BONUS | ACTION_SPRITE_ADD_EFFECT_STRENGTH_BONUS | ACTION_SPRITE_ADD_EFFECT_AGILITY_BONUS | ACTION_SPRITE_ADD_EFFECT_CRITICAL_FAILURE_BONUS | ACTION_SPRITE_ADD_EFFECT_CHANCE_BONUS | ACTION_SPRITE_ADD_EFFECT_WISDOM_BONUS | ACTION_SPRITE_ADD_EFFECT_VITALITY_BONUS | ACTION_SPRITE_ADD_EFFECT_INTELLIGENCE_BONUS | ACTION_SPRITE_ADD_EFFECT_DAMAGE_PERCENT_BONUS | ACTION_SPRITE_ADD_EFFECT_PHYSICAL_DAMAGE_BONUS | ACTION_SPRITE_ADD_EFFECT_DAMAGE_MALUS | ACTION_SPRITE_ADD_EFFECT_CHANCE_MALUS | ACTION_SPRITE_ADD_EFFECT_VITALITY_MALUS | ACTION_SPRITE_ADD_EFFECT_AGILITY_MALUS | ACTION_SPRITE_ADD_EFFECT_INTELLIGENCE_MALUS | ACTION_SPRITE_ADD_EFFECT_WISDOM_MALUS | ACTION_SPRITE_ADD_EFFECT_STRENGTH_MALUS | ACTION_SPRITE_ADD_EFFECT_DODGE_AP_LOSS_PERCENT_BONUS | ACTION_SPRITE_ADD_EFFECT_DODGE_MP_LOSS_PERCENT_BONUS | ACTION_SPRITE_ADD_EFFECT_DODGE_AP_LOSS_PERCENT_MALUS | ACTION_SPRITE_ADD_EFFECT_DODGE_MP_LOSS_PERCENT_MALUS | ACTION_SPRITE_ADD_EFFECT_MAX_SUMMONED_COUNT_BONUS | ACTION_SPRITE_ADD_EFFECT_WISDOM_BONUS | ACTION_SPRITE_ADD_EFFECT_STRENGTH_BONUS | ACTION_SPRITE_ADD_EFFECT_CHANCE_BONUS | ACTION_SPRITE_ADD_EFFECT_AGILITY_BONUS | ACTION_SPRITE_ADD_EFFECT_VITALITY_BONUS | ACTION_SPRITE_ADD_EFFECT_INTELLIGENCE_BONUS) ";" {entity.id} ";" sprite.id "," value "," remainingTurnCount
```

```js
{action.id} ";" ACTION_FIGHT_STEAL_MONEY ";" stealer.id ";" moneyAmount
```

```js
{action.id} ";" ACTION_SPRITE_CLEAR_EFFECTS ";" clearer.id ";" cleared.id
```

```js
{action.id} ";" ACTION_FIGHT_PASS_NEXT_TURN ";" {entity.id} ";" sprite.id
```

```js
{action.id} ";" ACTION_FIGHT_REVIVE ";" {entity.id} ";" entityListUpdate
```

```js
{action.id} ";" ACTION_SPRITE_ADD_EFFECT_APPEARANCE_CHANGE ";" {entity.id} ";" sprite.id "," sprite.gfxId "," temporaryGfxId "," remainingTurnCount
```

```js
{action.id} ";" ACTION_SPRITE_SET_EFFECT_INVISIBILITY ";" {entity.id} ";" sprite.id "," remainingTurnCount
```

```js
{action.id} ";" ACTION_FIGHT_CANT_INVISIBLE_OBSTACLE ";" launcher.id {";" spell.id}
```

```js
{action.id} ";" ACTION_FIGHT_RETURN_AP_LOSS ";" returner.id ";" "," returnedApLoss
```

```js
{action.id} ";" ACTION_FIGHT_SUMMON ";" summoner.id ";" entityListUpdate
```

```js
{action.id} ";" ACTION_UPDATE_ENTITY_LIST ";" {entity.id} ";" entityListUpdate
```

```js
{action.id} ";" ACTION_SET_CELL_OBJECT2_FRAME ";" {entity.id} ";" cell.id "," object2.frame
```

```js
{action.id} ";" ACTION_SPRITE_LAUNCH_VISUAL_EFFECT_TRY_BYPASS_CONTAINER_COLOR ";" sprite.id ";" cell.id "," visualEffect.gfxId "," visualEffect.displayTypeId "," sprite.animation {"," visualEffect.level}
```

```js
{action.id} ";" ACTION_SPRITE_LAUNCH_VISUAL_EFFECT ";" sprite.id ";" cell.id "," visualEffect.gfxId "," visualEffect.displayTypeId "," sprite.animation {"," visualEffect.level}
```

```js
{action.id} ";" ACTION_SPRITE_SPELL_USE ";" sprite.id ";" spell.id "," cell.id "," visualEffect.gfxId "," visualEffect.level "," visualEffect.displayTypeId "," sprite.animation "," visualEffect.isInFrontOfSprite
```

```js
{action.id} ";" ACTION_SPRITE_SPELL_CRITICAL_HIT ";" sprite.id
```

```js
{action.id} ";" ACTION_SPRITE_SPELL_CRITICAL_FAILURE ";" sprite.id ";" spell.id
```

```js
{action.id} ";" ACTION_SPRITE_WEAPON_USE ";" sprite.id ";" cell.id {"," visualEffect.gfxId "," visualEffect.displayTypeId "," visualEffect.isInFrontOfSprite}
```

```js
{action.id} ";" ACTION_SPRITE_WEAPON_CRITICAL_HIT ";" sprite.id
```

```js
{action.id} ";" ACTION_SPRITE_WEAPON_CRITICAL_FAILURE ";" sprite.id
```

```js
{action.id} ";" ACTION_SPRITE_ACTIVATE_TRAP ";" activator.id ";" spell.id "," cell.id "," visualEffect.gfxId "," visualEffect.level "," visualEffect.isInFrontOfSprite "," owner.id
```

```js
{action.id} ";" ACTION_FIGHT_ACTIVATE_GLYPH ";" activator.id ";" spell.id "," "," "," spell.level "," "," owner.id
```

```js
{action.id} ";" ACTION_FIGHT_DODGE_AP_LOSS ";" {entity.id} ";" dodger.id "," dodgedApLoss
```

```js
{action.id} ";" ACTION_FIGHT_DODGE_MP_LOSS ";" {entity.id} ";" dodger.id "," dodgedMpLoss
```

```js
{action.id} ";" ACTION_SPRITE_HARVEST ";" sprite.id ";" cell.id "," durationInMilliseconds {"," sprite.animationId}
```

```js
{action.id} ";" ACTION_SPRITE_WEDDING_REQUESTED ";" entity.id ";" asked.id "," engaged.id "," priest.id
```

```js
{action.id} ";" (ACTION_SPRITE_WEDDING_ACCEPTED | ACTION_SPRITE_WEDDING_REFUSED) ";" entity.id ";" engaged0.id "," engaged1.id "," priest.id
```

```js
{action.id} ";" ACTION_FIGHT_SUMMONED_STATE ";" summoner.id ";" ";" ";" ";" summoned.id
```

```js
{action.id} ";" ACTION_DEFIANCE_REQUESTED ";" asker.id ";" asked.id
```

```js
{action.id} ";" ACTION_DEFIANCE_ACCEPTED ";" {entity.id} ";" sprite.id
```

```js
{action.id} ";" ACTION_DEFIANCE_REFUSED ";" {entity.id}
```

```js
{action.id} ";" ACTION_JOIN_FIGHT_FAILURE ";" {entity.id} ";" (ERROR_TEAM_ALIGNMENT | ERROR_OPPONENT_SUBSCRIPTION | ERROR_FIGHT_FULL | ERROR_DEAD | ERROR_TEAM_CLOSED | ERROR_GUILD | ERROR_MULTI_ACCOUNT | ERROR_RIGHTS | ERROR_TOO_LATE | ERROR_MUTANT | ERROR_SUBSCRIPTION | ERROR_OCCUPIED | ERROR_MAP | ERROR_OPPONENT_NOT_READY | ERROR_SUBSCRIPTION_EXPIRED | ERROR_TEAM_FULL | ERROR_OPPONENT_OCCUPIED)
```

```js
{action.id} ";" ACTION_SHOW_ENTERED_FIGHT ";" {entity.id}
```

```js
{action.id} ";" ACTION_CHARACTER_ATTACKED ";" attacker.id ";" attacked.id
```

```js
{action.id} ";" ACTION_TAX_COLLECTOR_ATTACKED ";" attacker.id ";" attacked.id
```

```js
{action.id} ";" ACTION_SPRITE_SET_STATE ";" {entity.id} ";" sprite.id "," state.id "," state.isEnabled
```

```js
{action.id} ";" ACTION_PROCESS_NETWORK_MESSAGE ";" {entity.id} ";" message
```

#### Parameters

```js
sprite.animation = (animation.id | (movementAnimation.name "~" postMovementAnimation.name "~" returnMovementAnimation.name {"~" postReturnMovementAnimation.name}))
```

```js
visualEffect.displayTypeId = (DISPLAY_DO_NOT_SHOW | DISPLAY_SHOW_ASYNC | DISPLAY_SHOW_SYNC)
```

#### Constants

```js
ACTION_NO = 0
ACTION_SPRITE_MOVE = 1
ACTION_SHOW_LOADING_MAP_OR_CINEMATIC = 2
ACTION_SPRITE_SET_POSITION = 4
ACTION_SPRITE_SLIDE_STRAIGHT = 5
ACTION_SPRITE_SET_DIRECTION = 11
ACTION_SPRITE_CARRY_START = 50
ACTION_SPRITE_CARRY_LAUNCH = 51
ACTION_SPRITE_CARRY_STOP = 52
ACTION_SPRITE_UPDATE_MP = (78 | 127 | 128 | 169)
ACTION_SPRITE_UPDATE_MP_USED = 129
ACTION_SPRITE_UPDATE_LP = (100 | 108 | 110)
ACTION_SPRITE_UPDATE_AP = (101 | 111 | 120 | 168)
ACTION_SPRITE_UPDATE_AP_USED = 102
ACTION_SPRITE_DIE = 103
ACTION_SPRITE_CANT_MOVE = 104
ACTION_FIGHT_REDUCE_DAMAGE = 105
ACTION_FIGHT_REDUCE_DAMAGE_PERCENT = 164
ACTION_FIGHT_RETURN_SPELL = 106
ACTION_FIGHT_RETURN_DAMAGE = 107
ACTION_SPRITE_ADD_EFFECT_DAMAGE_BONUS = 112
ACTION_SPRITE_ADD_EFFECT_DAMAGE_MULTIPLICATOR = 114
ACTION_SPRITE_ADD_EFFECT_CRITICAL_HIT_BONUS = 115
ACTION_SPRITE_ADD_EFFECT_RANGE_MALUS = 116
ACTION_SPRITE_ADD_EFFECT_RANGE_BONUS = 117
ACTION_SPRITE_ADD_EFFECT_STRENGTH_BONUS = 118
ACTION_SPRITE_ADD_EFFECT_AGILITY_BONUS = 119
ACTION_SPRITE_ADD_EFFECT_CRITICAL_FAILURE_BONUS = 122
ACTION_SPRITE_ADD_EFFECT_CHANCE_BONUS = 123
ACTION_SPRITE_ADD_EFFECT_WISDOM_BONUS = 124
ACTION_SPRITE_ADD_EFFECT_VITALITY_BONUS = 125
ACTION_SPRITE_ADD_EFFECT_INTELLIGENCE_BONUS = 126
ACTION_SPRITE_ADD_EFFECT_DAMAGE_PERCENT_BONUS = 138
ACTION_SPRITE_ADD_EFFECT_PHYSICAL_DAMAGE_BONUS = 142
ACTION_SPRITE_ADD_EFFECT_DAMAGE_MALUS = 145
ACTION_SPRITE_ADD_EFFECT_CHANCE_MALUS = 152
ACTION_SPRITE_ADD_EFFECT_VITALITY_MALUS = 153
ACTION_SPRITE_ADD_EFFECT_AGILITY_MALUS = 154
ACTION_SPRITE_ADD_EFFECT_INTELLIGENCE_MALUS = 155
ACTION_SPRITE_ADD_EFFECT_WISDOM_MALUS = 156
ACTION_SPRITE_ADD_EFFECT_STRENGTH_MALUS = 157
ACTION_SPRITE_ADD_EFFECT_DODGE_AP_LOSS_PERCENT_BONUS = 160
ACTION_SPRITE_ADD_EFFECT_DODGE_MP_LOSS_PERCENT_BONUS = 161
ACTION_SPRITE_ADD_EFFECT_DODGE_AP_LOSS_PERCENT_MALUS = 162
ACTION_SPRITE_ADD_EFFECT_DODGE_MP_LOSS_PERCENT_MALUS = 163
ACTION_SPRITE_ADD_EFFECT_MAX_SUMMONED_COUNT_BONUS = 182
ACTION_SPRITE_ADD_EFFECT_WISDOM_BONUS = 606
ACTION_SPRITE_ADD_EFFECT_STRENGTH_BONUS = 607
ACTION_SPRITE_ADD_EFFECT_CHANCE_BONUS = 608
ACTION_SPRITE_ADD_EFFECT_AGILITY_BONUS = 609
ACTION_SPRITE_ADD_EFFECT_VITALITY_BONUS = 610
ACTION_SPRITE_ADD_EFFECT_INTELLIGENCE_BONUS = 611
ACTION_FIGHT_STEAL_MONEY = 130
ACTION_SPRITE_CLEAR_EFFECTS = 132
ACTION_FIGHT_PASS_NEXT_TURN = 140
ACTION_FIGHT_REVIVE = 147
ACTION_SPRITE_ADD_EFFECT_APPEARANCE_CHANGE = 149
ACTION_SPRITE_SET_EFFECT_INVISIBILITY = 150
ACTION_FIGHT_CANT_INVISIBLE_OBSTACLE = 151
ACTION_FIGHT_RETURN_AP_LOSS = 166
ACTION_FIGHT_SUMMON = (180 | 181)
ACTION_UPDATE_ENTITY_LIST = 185
ACTION_SET_CELL_OBJECT2_FRAME = 200
ACTION_SPRITE_LAUNCH_VISUAL_EFFECT_TRY_BYPASS_CONTAINER_COLOR = 208
ACTION_SPRITE_LAUNCH_VISUAL_EFFECT = 228
ACTION_SPRITE_SPELL_USE = 300
ACTION_SPRITE_SPELL_CRITICAL_HIT = 301
ACTION_SPRITE_SPELL_CRITICAL_FAILURE = 302
ACTION_SPRITE_WEAPON_USE = 303
ACTION_SPRITE_WEAPON_CRITICAL_HIT = 304
ACTION_SPRITE_WEAPON_CRITICAL_FAILURE = 305
ACTION_SPRITE_ACTIVATE_TRAP = 306
ACTION_FIGHT_ACTIVATE_GLYPH = 307
ACTION_FIGHT_DODGE_AP_LOSS = 308
ACTION_FIGHT_DODGE_MP_LOSS = 309
ACTION_SPRITE_HARVEST = 501
ACTION_SPRITE_WEDDING_REQUESTED = 617
ACTION_SPRITE_WEDDING_ACCEPTED = 618
ACTION_SPRITE_WEDDING_REFUSED = 619
ACTION_FIGHT_SUMMONED_STATE = 780
ACTION_DEFIANCE_REQUESTED = 900
ACTION_DEFIANCE_ACCEPTED = 901
ACTION_DEFIANCE_REFUSED = 902
ACTION_JOIN_FIGHT_FAILURE = 903
ACTION_SHOW_ENTERED_FIGHT = 905
ACTION_CHARACTER_ATTACKED = 906
ACTION_TAX_COLLECTOR_ATTACKED = 909
ACTION_SPRITE_SET_STATE = 950
ACTION_PROCESS_NETWORK_MESSAGE = 999
```

```js
DISPLAY_DO_NOT_SHOW = 0
DISPLAY_SHOW_ASYNC = (10 | 11 | 20 | 21 | 50)
DISPLAY_SHOW_SYNC = (12 | 30 | 31 | 40 | 41 | 51)
```

```js
ERROR_TEAM_ALIGNMENT = "a"
ERROR_OPPONENT_SUBSCRIPTION = "b"
ERROR_FIGHT_FULL = "c"
ERROR_DEAD = "d"
ERROR_TEAM_CLOSED = "f"
ERROR_GUILD = "g"
ERROR_MULTI_ACCOUNT = "h"
ERROR_RIGHTS = "i"
ERROR_TOO_LATE = "l"
ERROR_MUTANT = "m"
ERROR_SUBSCRIPTION = "n"
ERROR_OCCUPIED = "o"
ERROR_MAP = "p"
ERROR_OPPONENT_NOT_READY = "r"
ERROR_SUBSCRIPTION_EXPIRED = "s"
ERROR_TEAM_FULL = "t"
ERROR_OPPONENT_OCCUPIED = "z"
```

#### Functions

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

### FinishFightAction

#### Header

```js
"GAF"
```

#### Body

```js
action.id "|" fighter.id
```

---

### StartFightAction

#### Header

```js
"GAS"
```

#### Body

```js
fighter.id
```

---

### StartGameResult

#### Header

```js
"GC"
```

#### Body

```js
FAILURE
```

```js
SUCCESS "|" STATE_NOT_IN_FIGHT {"|" character.name}
```

#### Constants

```js
STATE_NOT_IN_FIGHT = 1
```

---

### CellDetails

#### Header

```js
"GDC"
```

#### Body

```js
[cell.id {";" ENCODE_CELL(cell) <ENCODE_CELL_MASK(cellMask), 16> ";" cell.permanentLevel}, "|"]
```

#### Parameters

```js
cell.permanentLevel = (0 | 1)
```

#### Functions

```js
function NEW_CELL() {
    var cell = {};
    cell.isActive = true;
    cell.layerGroundId = 0;
    cell.layerObject1Id = 0;
    cell.layerObject2Id = 0;
    cell.hasLineOfSight = true;
    cell.layerGroundRotation = 0;
    cell.groundLevel = 7;
    cell.movement = 4;
    cell.groundSlope = 1;
    cell.isLayerGroundFlipped = false;
    cell.layerObject1Rotation = 0;
    cell.isLayerObject1Flipped = false;
    cell.isLayerObject2Flipped = false;
    cell.isLayerObject2Interactive = false;
    return cell;
}
```

```js
function ENCODE_CELL(cell) {
    var e = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    e[0] = cell.isActive << 5;
    e[0] |= (cell.layerGroundId & ((1 << 10) | (1 << 9))) >> 6;
    e[0] |= (cell.layerObject1Id & (1 << 13)) >> 11;
    e[0] |= (cell.layerObject2Id & (1 << 13)) >> 12;
    e[0] |= cell.hasLineOfSight;
    e[1] = (cell.layerGroundRotation & ((1 << 1) | 1)) << 4;
    e[1] |= cell.groundLevel & ((1 << 3) | (1 << 2) | (1 << 1) | 1);
    e[2] = (cell.movement & ((1 << 2) | (1 << 1) | 1)) << 3;
    e[2] |= (cell.layerGroundId & ((1 << 8) | (1 << 7) | (1 << 6))) >> 6;
    e[3] = cell.layerGroundId & ((1 << 5) | (1 << 4) | (1 << 3) | (1 << 2) | (1 << 1) | 1);
    e[4] = (cell.groundSlope & ((1 << 3) | (1 << 2) | (1 << 1) | 1)) << 2;
    e[4] |= cell.isLayerGroundFlipped << 1;
    e[4] |= (cell.layerObject1Id & (1 << 12)) >> 12;
    e[5] = (cell.layerObject1Id & ((1 << 11) | (1 << 10) | (1 << 9) | (1 << 8) | (1 << 7) | (1 << 6))) >> 6;
    e[6] = cell.layerObject1Id & ((1 << 5) | (1 << 4) | (1 << 3) | (1 << 2) | (1 << 1) | 1);
    e[7] = (cell.layerObject1Rotation & ((1 << 1) | 1)) << 4;
    e[7] |= cell.isLayerObject1Flipped << 3;
    e[7] |= cell.isLayerObject2Flipped << 2;
    e[7] |= cell.isLayerObject2Interactive << 1;
    e[7] |= (cell.layerObject2Id & (1 << 12)) >> 12;
    e[8] = (cell.layerObject2Id & ((1 << 11) | (1 << 10) | (1 << 9) | (1 << 8) | (1 << 7) | (1 << 6))) >> 6;
    e[9] = cell.layerObject2Id & ((1 << 5) | (1 << 4) | (1 << 3) | (1 << 2) | (1 << 1) | 1);
    var encodedCell = "";
    for (var i = 0; i < e.length; i++) {
        encodedCell += ENCODE_64(e[i]);
    }
    return encodedCell;
}
```

```js
function DECODE_CELL(encodedCell) {
    var e = [];
    for (var i = 0; i < encodedCell.length; i++) {
        e.push(DECODE_64(encodedCell.charAt(i)));
    }
    var cell = {};
    cell.isActive = (e[0] & (1 << 5)) >> 5;
    if (cell.isActive)
    {
        cell.layerGroundId = ((e[0] << 6) & ((1 << 10) | (1 << 9))) | ((e[2] << 6) & ((1 << 8) | (1 << 7) | (1 << 6))) | e[3];
        cell.layerObject1Id = ((e[4] << 12) & (1 << 12)) | ((e[0] << 11) & (1 << 13)) | (e[5] << 6) | e[6];
        cell.layerObject2Id = ((e[0] << 12) & (1 << 13)) | ((e[7] << 12) & (1 << 12)) | (e[8] << 6) | e[9];
        cell.hasLineOfSight = e[0] & 1;
        cell.layerGroundRotation = (e[1] >> 4) & ((1 << 1) | 1);
        cell.groundLevel = e[1] & ((1 << 3) | (1 << 2) | (1 << 1) | 1);
        cell.movement = (e[2] >> 3) & ((1 << 2) | (1 << 1) | 1);
        cell.groundSlope = (e[4] >> 2) & ((1 << 3) | (1 << 2) | (1 << 1) | 1);
        cell.isLayerGroundFlipped = (e[4] >> 1) & 1;
        cell.layerObject1Rotation = (e[7] >> 4) & ((1 << 1) | 1);
        cell.isLayerObject1Flipped = (e[7] >> 3) & 1;
        cell.isLayerObject2Flipped = (e[7] >> 2) & 1;
        cell.isLayerObject2Interactive = (e[7] >> 1) & 1;
    }
    return cell;
}
```

```js
function NEW_CELL_MASK() {
    var cellMask = {};
    cellMask.isLayerExternalObjectAutoSized = false;
    cellMask.isLayerExternalObjectInteractive = false;
    cellMask.layerExternalObjectFile = false;
    cellMask.isActive = false;
    cellMask.hasLineOfSight = false;
    cellMask.movement = false;
    cellMask.groundLevel = false;
    cellMask.groundSlope = false;
    cellMask.layerGroundId = false;
    cellMask.isLayerGroundFlipped = false;
    cellMask.layerGroundRotation = false;
    cellMask.layerObject1Id = false;
    cellMask.isLayerObject1Flipped = false;
    cellMask.layerObject1Rotation = false;
    cellMask.layerObject2Id = false;
    cellMask.isLayerObject2Flipped = false;
    cellMask.isLayerObject2Interactive = false;
    return cellMask;
}
```

```js
function ENCODE_CELL_MASK(cellMask) {
    var encodedCellMask = 0;
    encodedCellMask |= cellMask.isLayerExternalObjectAutoSized << 16;
    encodedCellMask |= cellMask.isLayerExternalObjectInteractive << 15;
    encodedCellMask |= cellMask.layerExternalObjectFile << 14;
    encodedCellMask |= cellMask.isActive << 13;
    encodedCellMask |= cellMask.hasLineOfSight << 12;
    encodedCellMask |= cellMask.movement << 11;
    encodedCellMask |= cellMask.groundLevel << 10;
    encodedCellMask |= cellMask.groundSlope << 9;
    encodedCellMask |= cellMask.layerGroundId << 8;
    encodedCellMask |= cellMask.isLayerGroundFlipped << 7;
    encodedCellMask |= cellMask.layerGroundRotation << 6;
    encodedCellMask |= cellMask.layerObject1Id << 5;
    encodedCellMask |= cellMask.isLayerObject1Flipped << 4;
    encodedCellMask |= cellMask.layerObject1Rotation << 3;
    encodedCellMask |= cellMask.layerObject2Id << 2;
    encodedCellMask |= cellMask.isLayerObject2Flipped << 1;
    encodedCellMask |= cellMask.isLayerObject2Interactive;
    return encodedCellMask;
}
```

```js
function DECODE_CELL_MASK(encodedCellMask) {
    var cellMask = {};
    cellMask.isLayerExternalObjectAutoSized = (encodedCellMask >> 16) & 1;
    cellMask.isLayerExternalObjectInteractive = (encodedCellMask >> 15) & 1;
    cellMask.layerExternalObjectFile = (encodedCellMask >> 14) & 1;
    cellMask.isActive = (encodedCellMask >> 13) & 1;
    cellMask.hasLineOfSight = (encodedCellMask >> 12) & 1;
    cellMask.movement = (encodedCellMask >> 11) & 1;
    cellMask.groundLevel = (encodedCellMask >> 10) & 1;
    cellMask.groundSlope = (encodedCellMask >> 9) & 1;
    cellMask.layerGroundId = (encodedCellMask >> 8) & 1;
    cellMask.isLayerGroundFlipped = (encodedCellMask >> 7) & 1;
    cellMask.layerGroundRotation = (encodedCellMask >> 6) & 1;
    cellMask.layerObject1Id = (encodedCellMask >> 5) & 1;
    cellMask.isLayerObject1Flipped = (encodedCellMask >> 4) & 1;
    cellMask.layerObject1Rotation = (encodedCellMask >> 3) & 1;
    cellMask.layerObject2Id = (encodedCellMask >> 2) & 1;
    cellMask.isLayerObject2Flipped = (encodedCellMask >> 1) & 1;
    cellMask.isLayerObject2Interactive = encodedCellMask & 1;
    return cellMask;
}
```

---

### CellExternalObjectFrame

#### Header

```js
"GDE"
```

#### Body

```js
"|" [cell.id ";" externalObject.frame, "|"]
```

---

### CellObject2Frame

#### Header

```js
"GDF"
```

#### Body

```js
"|" [cell.id ";" object2.frame {";" object2.isInteractive}, "|"]
```

---

### MapLoaded

#### Header

```js
"GDK"
```

#### Body

```js
EMPTY
```

---

### MapDetails

#### Header

```js
"GDM"
```

#### Body

```js
"|" map.id "|" map.date "|" map.key
```

---

### UpdateCellExternalObject

#### Header

```js
"GDO"
```

#### Body

```js
ADD [cell.id ";" item.modelId ";" (NOT_PADDOCK_ITEM | (PADDOCK_ITEM ";" item.durability ";" item.maxDurability)), "|"]
```

```js
REMOVE [cell.id, "|"]
```

#### Constants

```js
NOT_PADDOCK_ITEM = 0
PADDOCK_ITEM = 1
```

---

### UpdateZone

#### Header

```js
"GDZ"
```

#### Body

```js
[(ADD | REMOVE) cell.id ";" radius ";" layer.name, "|"]
```

---

### FinishFight

#### Header

```js
"GE"
```

#### Body

```js
fight.durationInMilliseconds {";" fight.bonusPercent} "|" fight.id "|" (FIGHT_NEUTRAL | FIGHT_ALIGNED) "|" [entry, "|"]
```

#### Parameters

FIGHT_NEUTRAL:

```js
entry = ((ENTRY_LOOSER | ENTRY_WINNER | ENTRY_TAX_COLLECTOR) ";" entity.id ";" entity.genericName ";" entity.level ";" entity.isDead ";" entity.levelXp ";" entity.totalXp ";" entity.nextLevelXp ";" entity.xpWon ";" entity.guildXp ";" entity.mountXp ";" [item.modelId "~" item.quantity, ","] ";" moneyAmount) | (ENTRY_DROP ";" [item.modelId "~" item.quantity, ","] ";" moneyAmount)
```

FIGHT_ALIGNED:

```js
entry = ((ENTRY_LOOSER | ENTRY_WINNER | ENTRY_TAX_COLLECTOR) ";" entity.id ";" entity.genericName ";" entity.level ";" entity.isDead ";" entity.rankHonor ";" entity.totalHonor ";" entity.nextRankHonor ";" entity.honorWon ";" entity.rank ";" entity.disgrace ";" entity.disgraceWon ";" [item.modelId "~" item.quantity, ","] ";" moneyAmount ";" entity.levelXp ";" entity.totalXp ";" entity.nextLevelXp ";" entity.xpWon) | (ENTRY_DROP ";" [item.modelId "~" item.quantity, ","] ";" moneyAmount)
```

#### Constants

```js
FIGHT_NEUTRAL = 0
FIGHT_ALIGNED = 1
```

```js
ENTRY_LOOSER = 0
ENTRY_WINNER = 2
ENTRY_TAX_COLLECTOR = 5
ENTRY_DROP = 6
```

---

### FighterPosition

#### Header

```js
"GIC"
```

#### Body

```js
"|" [fighter.id ";" fighter.cellId {";" 1?}, "|"]
```

```js
"|" ERROR
```

#### Constants

```js
ERROR = "e"
```

---

### AddFighterEffect

#### Header

```js
"GIE"
```

#### Body

```js
effect.typeId ";" [fighter.id, ","] ";" effect.param1 ";" effect.param2 ";" effect.param3 ";" effect.param4 ";" effect.remainingTurnCount ";" effect.spellId
```

---

### DisablePvpLostHonor

#### Header

```js
"GIP"
```

#### Body

```js
lostHonor
```

---

### ClearFighterEffects

#### Header

```js
"GIe"
```

#### Body

```js
EMPTY
```

---

### JoinFight

#### Header

```js
"GJ"
```

#### Body

```js
SUCCESS STATE_IN_FIGHT "|" canCancel "|" canBeReady "|" isSpectator "|" (FIGHT_START_TIMER | remainingTimerInMilliseconds) "|" fight.typeId
```

#### Constants

```js
FIGHT_START_TIMER = 30000
```

#### Constants

```js
STATE_IN_FIGHT = 2
```

---

### UpdateEntityList

#### Header

```js
"GM"
```

#### Body

```js
"|" entityListUpdate
```

---

### GameOver

#### Header

```js
"GO"
```

#### Body

```js
EMPTY
```

---

### FightStartPositionList

#### Header

```js
"GP"
```

#### Body

```js
ENCODE_CELL_IDS(team0.cellIds) "|" ENCODE_CELL_IDS(team1.cellIds) "|" character.teamIndex
```

#### Functions

```js
function ENCODE_CELL_IDS(cellIds) {
    var encodedCellIds = "";
    for (var cellId of cellIds) {
        var e0 = cellId >> 6;
        var e1 = cellId & ((1 << 6) - 1);
        var encodedCellId = ENCODE_64(e0) + ENCODE_64(e1);
        encodedCellIds += encodedCellId;
    }
    return encodedCellIds;
}
```

```js
function DECODE_CELL_IDS(encodedCellIds) {
    var cellIds = [];
    for (var i = 0; i < encodedCellIds.length; i += 2) {
        var e0 = DECODE_64(encodedCellIds.charAt(i));
        var e1 = DECODE_64(encodedCellIds.charAt(i + 1));
        var cellId = (e0 << 6) | e1;
        cellIds.push(cellId);
    }
    return cellIds;
}
```

---

### ValidateFightState

#### Header

```js
"GR"
```

#### Body

```js
fighter.isReady fighter.id
```

---

### StartFight

#### Header

```js
"GS"
```

#### Body

```js
EMPTY
```

---

### FinishFightTurn

#### Header

```js
"GTF"
```

#### Body

```js
{fighter.id}
```

---

### FightTurnOrder

#### Header

```js
"GTL"
```

#### Body

```js
"|" [fighter.id, "|"]
```

---

### FighterStatList

#### Header

```js
"GTM"
```

#### Body

```js
"|" [{fighter.id ";" (DEAD | (NOT_DEAD ";" fighter.lp ";" fighter.ap ";" fighter.mp ";" (-1 | fighter.cellId) ";" ";" fighter.maxLp))}, "|"]
```

#### Constants

```js
NOT_DEAD = 0
DEAD = 1
```

---

### AcknowledgeFightTurn

#### Header

```js
"GTR"
```

#### Body

```js
fighter.id
```

---

### StartFightTurn

#### Header

```js
"GTS"
```

#### Body

```js
fighter.id "|" (TURN_TIMER | totalTimerInMilliseconds)
```

#### Constants

```js
TURN_TIMER = 29000
```

---

### RemoteKickFighter

#### Header

```js
"GV"
```

#### Body

```js
EMPTY
```

---

### UpdateEntityExtra

#### Header

```js
"GX"
```

#### Body

```js
(REMOVE | extraId) "|" [entity.id, ";"]
```

---

### UpdateNotValidatedFightList

#### Header

```js
"Gc"
```

#### Body

```js
ADD fight.id ";" fight.typeId "|" [team.id ";" team.cellId ";" team.typeId ";" team.alignmentId, "|"]
```

```js
REMOVE fight.id
```

---

### FightChallenge

#### Header

```js
"Gd"
```

#### Body

```js
challenge.id ";" challenge.canFlagTarget ";" challenge.targetId ";" challenge.basicXPBonusPercent ";" challenge.teamXPBonusPercent ";" challenge.basicDropBonusPercent ";" challenge.teamDropBonusPercent
```

---

### FightChallengeResult

#### Header

```js
"Gd"
```

#### Body

```js
CHALLENGE_SUCCESS challenge.id
```

```js
CHALLENGE_FAILURE challenge.id
```

#### Constants

```js
CHALLENGE_SUCCESS = "KO"
CHALLENGE_FAILURE = "OK"
```

---

### FlagFightCell

#### Header

```js
"Gf"
```

#### Body

```js
flagger.id "|" cell.id
```

---

### UpdateFightOption

#### Header

```js
"Go"
```

#### Body

```js
(ENABLE | DISABLE) (OPTION_CANT_JOIN | OPTION_NEED_HELP | OPTION_CANT_JOIN_IF_NOT_GROUP | OPTION_CANT_WATCH) team.id
```

#### Constants

```js
OPTION_CANT_JOIN = "A"
OPTION_NEED_HELP = "H"
OPTION_CANT_JOIN_IF_NOT_GROUP = "P"
OPTION_CANT_WATCH =  "S"
```

---

### UpdateNotValidatedFightFighterList

#### Header

```js
"Gt"
```

#### Body

```js
team.id "|" [((ADD fighter.id ";" fighter.genericName ";" fighter.level) | (REMOVE fighter.id)), "|"]
```

---

### CompassCoordinates

#### Header

```js
"IC"
```

#### Body

```js
{map.x "|" map.y}
```

---

### MarkedCoordinateList

#### Header

```js
"IH"
```

#### Body

```js
[map.x ";" map.y ";" map.id ";" (MARK_OTHER | MARK_PHOENIX), "|"]
```

```js
[map.x ";" map.y ";" map.id ";" MARK_GROUP ";" character.id, "|"]
```

```js
[map.x ";" map.y ";" map.id ";" MARK_SEEK ";" ";" character.name, "|"]
```

#### Constants

```js
MARK_OTHER = 0
MARK_PHOENIX = 1
MARK_GROUP = 2
MARK_SEEK = 3
```

---

### FinishRestoreLife

#### Header

```js
"ILF"
```

#### Body

```js
restoredLp
```

---

### StartRestoreLife

#### Header

```js
"ILS"
```

#### Body

```js
(SITTING_LP_INTERVAL | STANDING_LP_INTERVAL | lpIntervalInMilliseconds)
```

#### Constants

```js
SITTING_LP_INTERVAL = 1000
STANDING_LP_INTERVAL = 2000
```

---

### ItemOverhead

#### Header

```js
"IO"
```

#### Body

```js
sprite.id "|" (ADD | REMOVE) {item.modelId}
```

---

### QuantityOverhead

#### Header

```js
"IQ"
```

#### Body

```js
sprite.id "|" quantity
```

---

### InfoMessage

#### Header

```js
"Im"
```

#### Body

```js
CHAT_INFO [(((INFO_ITEM_RECEIVED | INFO_ITEM_LOST) ";" item.quantity "~" item.modelId) | (INFO_JOB_XP_WON ";" xpWon "~" job.id) | (INFO_JOB_LEARNT ";" job.id) | (INFO_SPELL_LEARNT ";" spell.id) | ((INFO_QUEST_STARTED | INFO_QUEST_UPDATED | INFO_QUEST_FINISHED) ";" quest.id) | ((INFO_ITEM_SOLD | INFO_ITEM_SOLD_OFFLINE) ";" moneyAmount "~" item.modelId "~" "~" item.quantity) | (INFO_ITEM_CREATED ";" item.modelId "~" item.effects) | (INFO_REMOTE_LIVING_ITEM_SAYS ";" item.modelId "~" character.name "~" objectChatId {"~" [objectChatParam, "~"]}) | (INFO_LOCAL_LIVING_ITEM_SAYS ";" item.modelId "~" objectChatId {"~" [objectChatParam, "~"]}) | (infoId {";" [infoParam, "~"]}) | (langId {";" [langParam, "~"]})), "|"]
```

```js
CHAT_ERROR [(((ERROR_JOB_CANT_LEARN | ERROR_JOB_NOT_LEARNT | ERROR_JOB_CANT_UNLEARN) ";" job.id) | (ERROR_SPELL_CANT_LEARN ";" spell.id) | (errorId {";" [errorParam, "~"]}) | (langId {";" [langParam, "~"]})), "|"]
```

```js
CHAT_PVP [((PVP_OWN_ATTACKED ";" subArea.id "~" area.id) | ((PVP_OWN_MUST_REPEL | PVP_OWN_OPENED | PVP_OWN_CLOSED | PVP_OPPOSING_ATTACKED | PVP_OPPOSING_OPENED) ";" area.id) | (pvpId {";" [pvpParam, "~"]}) | (langId {";" [langParam, "~"]})), "|"]
```

#### Constants

```js
CHAT_INFO = 0
CHAT_ERROR = 1
CHAT_PVP = 2
```

```js
INFO_JOB_LEARNT = 2
INFO_SPELL_LEARNT = 3
INFO_JOB_XP_WON = 17
INFO_ITEM_RECEIVED = 21
INFO_ITEM_LOST = 22
INFO_QUEST_STARTED = 54
INFO_QUEST_UPDATED = 55
INFO_QUEST_FINISHED = 56
INFO_ITEM_SOLD = 65
INFO_ITEM_SOLD_OFFLINE = 73
INFO_ITEM_CREATED = 123
INFO_REMOTE_LIVING_ITEM_SAYS = 150
INFO_LOCAL_LIVING_ITEM_SAYS = 151
```

```js
ERROR_JOB_CANT_LEARN = 6
ERROR_SPELL_CANT_LEARN = 7
ERROR_JOB_NOT_LEARNT = 46
ERROR_JOB_CANT_UNLEARN = 49
```

```js
PVP_OWN_ATTACKED = 41
PVP_OWN_MUST_REPEL = 86
PVP_OWN_OPENED = 87
PVP_OWN_CLOSED = 88
PVP_OPPOSING_ATTACKED = 89
PVP_OPPOSING_OPENED = 90
```

---

### JobLevelUp

#### Header

```js
"JN"
```

#### Body

```js
job.id "|" job.level
```

---

### JobOptions

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

### RemoveJob

#### Header

```js
"JR"
```

#### Body

```js
job.id
```

---

### JobSkillList

#### Header

```js
"JS"
```

#### Body

```js
"|" [job.id ";" [skill.id "~" ((skill.harvestMin "~" skill.harvestMax "~" "~" skill.harvestTimeInMilliseconds) | (skill.craftSlot "~" "~" "~" skill.craftProbabilityPercent)), ","], "|"]
```

---

### JobXp

#### Header

```js
"JX"
```

#### Body

```js
"|" [job.id ";" job.level ";" job.levelXp ";" job.totalXp ";" job.nextLevelXp, "|"]
```

---

### StartLock

#### Header

```js
"KC"
```

#### Body

```js
SUCCESS (LOCK_UNLOCK | LOCK_CHANGE) "|" (MAX_SLOT_COUNT | slotCount)
```

#### Constants

```js
LOCK_UNLOCK = 0
LOCK_CHANGE = 1
```

```js
MAX_SLOT_COUNT = 8
```

---

### LockKeyResult

#### Header

```js
"KK"
```

#### Body

```js
FAILURE
```

```js
SUCCESS
```

---

### CloseLock

#### Header

```js
"KV"
```

#### Body

```js
EMPTY
```

---

### AddInventoryItem

#### Header

```js
"OA"
```

#### Body

```js
FAILURE (ERROR_ALREADY_EQUIPPED | ERROR_FULL | ERROR_LEVEL)
```

```js
SUCCESS [(EXCHANGE_MONEY | (EXCHANGE_ITEM [item, ";"])), "*"]
```

#### Constants

```js
ERROR_ALREADY_EQUIPPED = "A"
ERROR_FULL = "F"
ERROR_LEVEL = "L"
```

---

### InventoryItemList

#### Header

```js
"OC"
```

#### Body

```js
"|"? [[item, ";"], "*"]
```

---

### DropItemFailure

#### Header

```js
"OD"
```

#### Body

```js
FAILURE (ERROR_UNABLE | ERROR_SPACE)
```

#### Constants

```js
ERROR_UNABLE = "E"
ERROR_SPACE = "F"
```

---

### ItemFoundOverhead

#### Header

```js
"OF"
```

#### Body

```js
1 "|" (MONEY | (item.modelId "~" item.quantity))
```

#### Constants

```js
MONEY = 0
```

---

### ValidateUseItem

#### Header

```js
"OK"
```

#### Body

```js
MONEY_COST item.id "|" sprite.id "|" cell.id "|" moneyAmount
```

```js
NO_MONEY_COST item.id "|" sprite.id "|" cell.id "|" item.modelId
```

#### Constants

```js
MONEY_COST = "G"
NO_MONEY_COST = "U"
```

---

### MoveInventoryItem

#### Header

```js
"OM"
```

#### Body

```js
item.id "|" item.position
```

---

### InventoryItemQuantity

#### Header

```js
"OQ"
```

#### Body

```js
item.id "|" item.quantity
```

---

### RemoveInventoryItem

#### Header

```js
"OR"
```

#### Body

```js
item.id
```

---

### UpdateEquippedItemSet

#### Header

```js
"OS"
```

#### Body

```js
ADD itemSet.id "|" [item.id, ";"] "|" itemSet.effects
```

```js
REMOVE itemSet.id
```

---

### EquippedJobTool

#### Header

```js
"OT"
```

#### Body

```js
{job.id}
```

---

### EntityAccessories

#### Header

```js
"Oa"
```

#### Body

```js
entity.id "|" entity.accessories
```

---

### InventoryWeight

#### Header

```js
"Ow"
```

#### Body

```js
pods "|" maxPods
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

### StartGroup

#### Header

```js
"PC"
```

#### Body

```js
FAILURE (ERROR_ALREADY | ERROR_FULL)
```

```js
SUCCESS inviter.name
```

#### Constants

```js
ERROR_ALREADY = "a"
ERROR_FULL = "f"
```

---

### FollowGroupMemberResult

#### Header

```js
"PF"
```

#### Body

```js
FAILURE
```

```js
SUCCESS followed.id
```

---

### InviteInGroupResult

#### Header

```js
"PI"
```

#### Body

```js
FAILURE (ERROR_ALREADY | ERROR_FULL | ERROR_CANT_FIND)
```

```js
FAILURE ERROR_CANT_FIND invited.name
```

```js
SUCCESS inviter.name "|" invited.name
```

#### Constants

```js
ERROR_ALREADY = "a"
ERROR_FULL = "f"
ERROR_CANT_FIND = "n"
```

---

### GroupLeader

#### Header

```js
"PL"
```

#### Body

```js
leader.id
```

---

### UpdateGroupMemberList

#### Header

```js
"PM"
```

#### Body

```js
(ADD | UPDATE) [member.id ";" member.name ";" member.gfxId ";" (-1 | member.color1) ";" (-1 | member.color2) ";" (-1 | member.color3) ";" member.accessories ";" member.lp ";" member.level ";" member.initiative ";" member.prospecting, "|"]
```

```js
REMOVE [member.id, "|"]
```

#### Constants

```js
UPDATE = "~"
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

### RemoteKickGroupMember

#### Header

```js
"PV"
```

#### Body

```js
{kicker.id}
```

---

### QuestList

#### Header

```js
"QL"
```

#### Body

```js
"|" [quest.id ";" quest.isFinished ";" quest.sortOrder, "|"]
```

---

### QuestStep

#### Header

```js
"QS"
```

#### Body

```js
quest.id "|" questStep.id "|" [questObjective.id "," questObjective.isFinished, ";"] "|" [questStep.previousStepId, ";"] "|" [questStep.nextStepId, ";"] "|" questStep.dialogId {";" [questStep.dialogParam, ","]}
```

---

### StartBuySellPaddock

#### Header

```js
"RD"
```

#### Body

```js
{owner.id} "|" paddock.defaultPrice
```

---

### MountDetails

#### Header

```js
"Rd"
```

#### Body

```js
mount
```

---

### UpdateEquippedMount

#### Header

```js
"Re"
```

#### Body

```js
FAILURE (ERROR_ALREADY | ERROR_NOT_EMPTY | ERROR_UNABLE)
```

```js
ADD mount
```

```js
REMOVE
```

#### Constants

```js
ERROR_ALREADY = "+"
ERROR_NOT_EMPTY = "-"
ERROR_UNABLE = "r"
```

---

### MountName

#### Header

```js
"Rn"
```

#### Body

```js
mount.name
```

---

### PaddockDetails

#### Header

```js
"Rp"
```

#### Body

```js
(PADDOCK_PUBLIC | PADDOCK_NO_OWNER | {owner.id}) ";" (0 | paddock.price) ";" paddock.maxMountCount ";" paddock.maxItemCount ";" paddock.guildName ";" paddock.guildEmblem
```

#### Constants

```js
PADDOCK_PUBLIC = -1
PADDOCK_NO_OWNER = 0
```

---

### RideMountState

#### Header

```js
"Rr"
```

#### Body

```js
(ENABLE | DISABLE)
```

---

### CloseBuySellPaddock

#### Header

```js
"Rv"
```

#### Body

```js
EMPTY
```

---

### MountXp

#### Header

```js
"Rx"
```

#### Body

```js
mount.xpPercent
```

---

### SpellModifier

#### Header

```js
"SB"
```

#### Body

```js
(MODIFIER_MAX_RANGE | MODIFIER_CAN_BOOST_RANGE | MODIFIER_DAMAGE | MODIFIER_HEAL | MODIFIER_AP_COST | MODIFIER_INTERVAL | MODIFIER_CRITICAL_HIT | MODIFIER_NOT_LINE_ONLY | MODIFIER_NO_LINE_OF_SIGHT | MODIFIER_MAX_COUNT_PER_TURN | MODIFIER_MAX_COUNT_PER_TARGET | MODIFIER_SET_INTERVAL) ";" spell.id ";" value
```

#### Constants

```js
MODIFIER_MAX_RANGE = 281
MODIFIER_CAN_BOOST_RANGE = 282
MODIFIER_DAMAGE = 283
MODIFIER_HEAL = 284
MODIFIER_AP_COST = 285
MODIFIER_INTERVAL = 286
MODIFIER_CRITICAL_HIT = 287
MODIFIER_NOT_LINE_ONLY = 288
MODIFIER_NO_LINE_OF_SIGHT = 289
MODIFIER_MAX_COUNT_PER_TURN = 290
MODIFIER_MAX_COUNT_PER_TARGET = 291
MODIFIER_SET_INTERVAL = 292
```

---

### StartForgetSpell

#### Header

```js
"SF"
```

#### Body

```js
(ADD | REMOVE)
```

---

### SpellList

#### Header

```js
"SL"
```

#### Body

```js
[spell, ";"] {";"}
```

---

### CanShowAllSpellOption

#### Header

```js
"SLo"
```

#### Body

```js
(ENABLE | DISABLE)
```

---

### UpgradeCharacterSpellResult

#### Header

```js
"SU"
```

#### Body

```js
FAILURE
```

```js
SUCCESS spell
```

---

### WelcomeTutorial

#### Header

```js
"TB"
```

#### Body

```js
EMPTY
```

---

### StartTutorial

#### Header

```js
"TC"
```

#### Body

```js
tutorialIdPart0 "|" tutorialIdPart1
```

---

### TutorialTip

#### Header

```js
"TT"
```

#### Body

```js
tip.id
```

---

### StartPortalTransport

#### Header

```js
"WC"
```

#### Body

```js
savedDestination.mapId "|" [destination.mapId ";" destination.cost, "|"]
```

---

### UsePortalTransportFailure

#### Header

```js
"WU"
```

#### Body

```js
EMPTY
```

---

### ClosePortalTransport

#### Header

```js
"WV"
```

#### Body

```js
EMPTY
```

---

### StartCityTransport

#### Header

```js
"Wc"
```

#### Body

```js
{current.mapId} "|" [destination.mapId ";" destination.cost, "|"]
```

---

### StartPrismTransport

#### Header

```js
"Wp"
```

#### Body

```js
{current.mapId} "|" [destination.mapId ";" destination.cost {ATTACK_NEARBY}, "|"]
```

#### Constants

```js
ATTACK_NEARBY = "*"
```

---

### UseTransportFailure

#### Header

```js
"Wu"
```

#### Body

```js
EMPTY
```

---

### CloseCityTransport

#### Header

```js
"Wv"
```

#### Body

```js
EMPTY
```

---

### ClosePrismTransport

#### Header

```js
"Ww"
```

#### Body

```js
EMPTY
```

---

### ChangeAlignmentSpecialization

#### Header

```js
"ZC"
```

#### Body

```js
specialization.id
```

---

### AlignmentSpecialization

#### Header

```js
"ZS"
```

#### Body

```js
(0 | specialization.id)
```

---

### ChangeConquestAreaAlignmentInfo

#### Header

```js
"aM"
```

#### Body

```js
area.id "|" area.alignmentId
```

---

### SubAreaList

#### Header

```js
"al"
```

#### Body

```js
"|" [subArea.id ";" subArea.alignmentId, "|"]
```

---

### ChangeSubAreaAlignment

#### Header

```js
"am"
```

#### Body

```js
subArea.id "|" subArea.alignmentId "|" isMessageHidden
```

---

### SubscribeChatChannelState

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
CHANNEL_PUBLIC = "*"
CHANNEL_PRIVATE = "p"
```

---

### ChatMessage

#### Header

```js
"cM"
```

#### Body

```js
FAILURE (ERROR_SYNTAX | (ERROR_NOT_CONNECTED character.name))
```

```js
SUCCESS "|" character.id "|" character.name "|" publicText "|" [item.modelId "!" item.effects, "!"] {"|" id}
```

```js
SUCCESS (CHANNEL_TEAM | CHANNEL_PARTY | CHANNEL_PRIVATE_FROM | CHANNEL_PRIVATE_TO | CHANNEL_GUILD | CHANNEL_ALIGNMENT | CHANNEL_RECRUITMENT | CHANNEL_TRADING | CHANNEL_NOVICE | CHANNEL_ADMIN) "|" "|" character.name "|" text "|" [item.modelId "!" item.effects, "!"] {"|" id}
```

RETRO:

```js
SUCCESS CHANNEL_EVENT "|" "|" "|" langId {"," [langParam, ","]} {"|"}
```

#### Parameters

```js
publicText = (("*" text "*") | ("!THINK!" text) | ("**" <speakingItemMessage.id + character.id> "**") | text)
```

```js
text = [(("°" itemIndex) | ("[" map.x "," {" "} map.y "]") | chatText), EMPTY]
```

#### Constants

```js
CHANNEL_PRIVATE_FROM = "F"
CHANNEL_PRIVATE_TO = "T"
```

```js
ERROR_SYNTAX = "S"
ERROR_NOT_CONNECTED = "f"
```

---

### UseSmiley

#### Header

```js
"cS"
```

#### Body

```js
sprite.id "|" smiley.id
```

#### Parameters

```js
smiley.id = (1 -> 15)
```

---

### ChatServerMessage

#### Header

```js
"cs"
```

#### Body

```js
chatText
```

---

### StartDocument

#### Header

```js
"dC"
```

#### Body

```js
SUCCESS document.id
```

---

### CloseDocument

#### Header

```js
"dV"
```

#### Body

```js
EMPTY
```

---

### AddEmoteInfo

#### Header

```js
"eA"
```

#### Body

```js
emoteId "|" isMessageShown
```

---

### CharacterDirection

#### Header

```js
"eD"
```

#### Body

```js
sprite.id "|" sprite.directionId
```

---

### EmoteList

#### Header

```js
"eL"
```

#### Body

```js
ENCODE_EMOTE_IDS(emoteIds) "|" ENCODE_EMOTE_IDS(emoteIds)
```

#### Functions

```js
function ENCODE_EMOTE_IDS(emoteIds) {
    var encodedEmoteIds = 0;
    for (var i = 0; i < 32; i++) {
        var emoteId = i + 1;
        if (emoteIds.includes(emoteId)) {
            var e0 = 1 << i;
            encodedEmoteIds |= e0;
        }
    }
    return encodedEmoteIds;
}
```

```js
function DECODE_EMOTE_IDS(encodedEmoteIds) {
    var emoteIds = [];
    for (var i = 0; i < 32; i++) {
        if ((encodedEmoteIds >> i) & 1) {
            var emoteId = i + 1;
            emoteIds.push(emoteId);
        }
    }
    return emoteIds;
}
```

---

### RemoveEmoteInfo

#### Header

```js
"eR"
```

#### Body

```js
emoteId "|" isMessageShown
```

---

### UseEmote

#### Header

```js
"eU"
```

#### Body

```js
FAILURE
```

```js
SUCCESS sprite.id "|" emoteId "|" {durationInMilliseconds}
```

---

### FightCount

#### Header

```js
"fC"
```

#### Body

```js
fightCount
```

---

### FightDetails

#### Header

```js
"fD"
```

#### Body

```js
fight.id "|" [team0Member.genericName "~" team0Member.level, ";"] "|" [team1Member.genericName "~" team1Member.level, ";"]
```

---

### FightList

#### Header

```js
"fL"
```

#### Body

```js
[fight.id ";" fight.startTimestamp ";" team0.typeId "," team0.alignmentId "," team0.fighterCount ";" team1.typeId "," team1.alignmentId "," team1.fighterCount, "|"]
```

---

### TaxCollectorAttackedInfo

#### Header

```js
"gA"
```

#### Body

```js
(TAX_COLLECTOR_ATTACKED | TAX_COLLECTOR_DIED | TAX_COLLECTOR_SURVIVED) taxCollector.name "|" "|" taxCollector.mapX "|" taxCollector.mapY
```

#### Constants

```js
TAX_COLLECTOR_ATTACKED = "A"
TAX_COLLECTOR_DIED = "D"
TAX_COLLECTOR_SURVIVED = "S"
```

---

### CreateGuildResult

#### Header

```js
"gC"
```

#### Body

```js
FAILURE (ERROR_IN_GUILD | ERROR_EMBLEM_USED | ERROR_NAME_USED)
```

```js
SUCCESS
```

#### Constants

```js
ERROR_IN_GUILD = "a"
ERROR_EMBLEM_USED = "ae"
ERROR_NAME_USED = "an"
```

---

### AddTaxCollectorFailure

#### Header

```js
"gH"
```

#### Body

```js
FAILURE (ERROR_ALREADY | ERROR_NOT_YOURS | ERROR_RIGHTS | ERROR_HERE | ERROR_MONEY | ERROR_MAX | ERROR_TIRED)
```

#### Constants

```js
ERROR_ALREADY = "a"
ERROR_NOT_YOURS = "b"
ERROR_RIGHTS = "d"
ERROR_HERE = "h"
ERROR_MONEY = "k"
ERROR_MAX = "m"
ERROR_TIRED = "y"
```

---

### TaxCollectorStats

#### Header

```js
"gIB"
```

#### Body

```js
{maxCount "|" count "|" lp "|" damageBonus "|" pods "|" prospecting "|" wisdom "|" population "|" upgradePoints "|" addCost "|" [spell.id ";" spell.level, "|"]}
```

---

### GuildPaddockList

#### Header

```js
"gIF"
```

#### Body

```js
maxPaddockCount "|" [paddock.mapId ";" paddock.maxMountCount ";" paddock.maxItemCount ";" [mount.modelId "," {mount.name} "," mount.ownerName, ","], "|"]
```

---

### GuildXp

#### Header

```js
"gIG"
```

#### Body

```js
guild.isValid "|" guild.level "|" guild.levelXp "|" guild.totalXp "|" guild.nextLevelXp
```

---

### GuildHouseList

#### Header

```js
"gIH"
```

#### Body

```js
EMPTY
```

```js
ADD [house.id ";" house.ownerName ";" house.mapX "," house.mapY ";" [skill.id, ","] ";" ENCODE_GUILD_HOUSE_OPTIONS(house.guildOptions), "|"]
```

---

### UpdateGuildMemberList

#### Header

```js
"gIM"
```

#### Body

```js
ADD [member.id ";" member.name ";" member.level ";" member.gfxId ";" member.rankId ";" member.guildXp ";" member.xpPercent ";" ENCODE_GUILD_RIGHTS(member.rights) ";" (STATE_OFFLINE | STATE_IN_FIGHT) ";" member.alignmentId ";" member.hoursSinceLastConnection, "|"]
```

```js
REMOVE [member.id, "|"]
```

#### Constants

```js
STATE_OFFLINE = 0
STATE_IN_FIGHT = 2
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

### UpdateTaxCollectorList

#### Header

```js
"gITM"
```

#### Body

```js
EMPTY
```

```js
ADD [<taxCollector.id, 36> ";" taxCollector.name "," taxCollector.adderName "," taxCollector.addDate "," taxCollector.lastCollectorName "," taxCollector.lastCollectDate "," taxCollector.nextCollectDate ";" <taxCollector.mapId, 36> ";" (STATE_IN_COLLECT | STATE_IN_NOT_VALIDATED_FIGHT | STATE_IN_VALIDATED_FIGHT) ";" taxCollector.remainingTimerInMilliseconds ";" taxCollector.totalTimerInMilliseconds ";" taxCollector.maxDefenderCount, "|"]
```

```js
REMOVE [<taxCollector.id, 36>, "|"]
```

#### Constants

```js
STATE_IN_COLLECT = 0
STATE_IN_NOT_VALIDATED_FIGHT = 1
STATE_IN_VALIDATED_FIGHT = 2
```

---

### UpdateTaxCollectorDefenseDefenderList

#### Header

```js
"gITP"
```

#### Body

```js
ADD <taxCollector.id, 36> "|" [<defender.id, 36> ";" defender.name ";" defender.gfxId ";" defender.level ";" (-1 | <defender.color1, 36>) ";" (-1 | <defender.color2, 36>) ";" (-1 | <defender.color3, 36>), "|"]
```

```js
REMOVE <taxCollector.id, 36> "|" [<defender.id, 36>, "|"]
```

---

### UpdateTaxCollectorDefenseAttackerList

#### Header

```js
"gITp"
```

#### Body

```js
ADD <taxCollector.id, 36> "|" [<attacker.id, 36> ";" attacker.name ";" attacker.level, "|"]
```

```js
REMOVE <taxCollector.id, 36> "|" [<attacker.id, 36>, "|"]
```

---

### RemoteGuildInvitationSuccess

#### Header

```js
"gJC"
```

#### Body

```js
EMPTY
```

---

### GuildInvitationFailure

#### Header

```js
"gJE"
```

#### Body

```js
(ERROR_ALREADY | ERROR_CLOSE | ERROR_RIGHTS | ERROR_OCCUPIED | ERROR_NOT_FOUND)
```

```js
ERROR_REFUSED invited.name
```

#### Constants

```js
ERROR_ALREADY = "a"
ERROR_CLOSE = "c"
ERROR_RIGHTS = "d"
ERROR_OCCUPIED = "o"
ERROR_REFUSED = "r"
ERROR_NOT_FOUND = "u"
```

---

### GuildInvitationSuccess

#### Header

```js
"gJK"
```

#### Body

```js
INVITED_JOINED invited.name
```

```js
YOU_JOINED
```

#### Constants

```js
INVITED_JOINED = "a"
YOU_JOINED = "j"
```

---

### LocalGuildInvitation

#### Header

```js
"gJR"
```

#### Body

```js
invited.name
```

---

### RemoteGuildInvitation

#### Header

```js
"gJr"
```

#### Body

```js
inviter.id "|" inviter.name "|" inviter.guildName
```

---

### KickGuildMemberResult

#### Header

```js
"gK"
```

#### Body

```js
FAILURE (ERROR_NOT_MEMBER | ERROR_RIGHTS)
```

```js
SUCCESS kicker.name "|" kicked.name
```

#### Constants

```js
ERROR_NOT_MEMBER = "a"
ERROR_RIGHTS = "d"
```

---

### GuildDetails

#### Header

```js
"gS"
```

#### Body

```js
guild.name "|" <guildEmblem.backId, 36> "|" <guildEmblem.backColor, 36> "|" <guildEmblem.symbolId, 36> "|" <guildEmblem.symbolColor, 36> "|" <character.guildRights, 36>
```

---

### TaxCollectorInfo

#### Header

```js
"gT"
```

#### Body

```js
TAX_COLLECTOR_COLLECTED taxCollector.name "|" "|" taxCollector.mapX "|" taxCollector.mapY "|" taxCollector.adderName "|" taxCollector.xp ";" [item.modelId "," item.quantity, ";"]
```

```js
(TAX_COLLECTOR_REMOVED | TAX_COLLECTOR_ADDED) taxCollector.name "|" "|" taxCollector.mapX "|" taxCollector.mapY "|" taxCollector.adderName
```

#### Constants

```js
TAX_COLLECTOR_COLLECTED = "G"
TAX_COLLECTOR_REMOVED = "R"
TAX_COLLECTOR_ADDED = "S"
```

---

### StartGuild

#### Header

```js
"gU"
```

#### Body

```js
(GUILD_PADDOCKS | GUILD_HOUSES)
```

#### Constants

```js
GUILD_PADDOCKS = "F"
GUILD_HOUSES = "T"
```

---

### CloseCreateGuild

#### Header

```js
"gV"
```

#### Body

```js
EMPTY
```

---

### StartCreateGuild

#### Header

```js
"gn"
```

#### Body

```js
EMPTY
```

---

### BuyHouseResult

#### Header

```js
"hB"
```

#### Body

```js
FAILURE ERROR_UNABLE house.price
```

```js
SUCCESS house.id "|" house.price
```

#### Constants

```js
ERROR_UNABLE = "C"
```

---

### StartBuySellHouse

#### Header

```js
"hC"
```

#### Body

```js
SUCCESS house.id "|" house.price
```

---

### GuildHouseOptions

#### Header

```js
"hG"
```

#### Body

```js
house.id ";" {house.guildName ";" house.guildEmblem ";" ENCODE_GUILD_HOUSE_OPTIONS(house.guildOptions)}
```

---

### UpdateOwnedHouseList

#### Header

```js
"hL"
```

#### Body

```js
ADD [house.id ";" house.isLocked ";" house.isForSale ";" house.hasGuild, "|"]
```

```js
REMOVE [house.id, "|"]
```

---

### HouseDoorDetails

#### Header

```js
"hP"
```

#### Body

```js
house.id "|" ("?" | house.ownerName) ";" house.isForSale {";" house.guildName ";" house.guildEmblem}
```

---

### SellHouseResult

#### Header

```js
"hS"
```

#### Body

```js
FAILURE
```

```js
SUCCESS house.id "|" house.price
```

---

### CloseBuySellHouse

#### Header

```js
"hV"
```

#### Body

```js
EMPTY
```

---

### HouseLockState

#### Header

```js
"hX"
```

#### Body

```js
house.id "|" house.isLocked
```

---

### AddEnemyResult

#### Header

```js
"iA"
```

#### Body

```js
FAILURE (ERROR_ALREADY | ERROR_NOT_FOUND | ERROR_FULL | ERROR_YOURSELF)
```

```js
SUCCESS enemy
```

#### Constants

```js
ERROR_ALREADY = "a"
ERROR_NOT_FOUND = "f"
ERROR_FULL = "m"
ERROR_YOURSELF = "y"
```

---

### RemoveEnemyResult

#### Header

```js
"iD"
```

#### Body

```js
FAILURE ERROR_NOT_FOUND
```

```js
SUCCESS
```

#### Constants

```js
ERROR_NOT_FOUND = "f"
```

---

### EnemyList

#### Header

```js
"iL"
```

#### Body

```js
"|" [enemy, "|"]
```

---

### UpdateOwnedStorageList

#### Header

```js
"sL"
```

#### Body

```js
ADD [storage.id ";" storage.isLocked, "|"]
```

```js
REMOVE [storage.id, "|"]
```

---

### StorageLockState

#### Header

```js
"sX"
```

#### Body

```js
storage.id "|" storage.isLocked
```

---

### LoginServerHello

#### Header

```js
"HC"
```

#### Body

```js
connectionKey
```

#### Parameters

```js
connectionKey = '[a-z]{32}'
```

---

### GameServerHello

#### Header

```js
"HG"
```

#### Body

```js
EMPTY
```

---

### ServerMessage

#### Header

```js
"M"
```

#### Body

```js
SHOW_NOW MESSAGE_SPELL_CHANGE "|" spell.id ";" returnedSpellPoints
```

```js
(SHOW_ON_DISCONNECTION | SHOW_NOW) message.id "|" [message.param, ";"]
```

#### Constants

```js
SHOW_ON_DISCONNECTION = 0
SHOW_NOW = 1
```

```js
MESSAGE_SPELL_CHANGE = 23
```

---

### UpcomingServerDisconnection

#### Header

```js
"k"?
```

#### Body

```js
EMPTY
```

---

### PingResponse

#### Header

```js
"pong"
```

#### Body

```js
EMPTY
```

---

### QuickPingResponse

#### Header

```js
"qpong"
```

#### Body

```js
EMPTY
```

---

### RPing?

#### Header

```js
"rping"
```

#### Body

```js
payload?
```