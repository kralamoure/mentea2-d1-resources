# Admin console

## Index

* [Command index](#command-index)
* [Syntax](#syntax)
* [Commands](#commands)

## Command index

|                                                                                                               |
|---------------------------------------------------------------------------------------------------------------|
| [Start sprite anim [DEBUG MODE]](#start-sprite-anim-[debug-mode])                                             |
| [Show alert with lang](#show-alert-with-lang)                                                                 |
| [Show alert with text](#show-alert-with-text)                                                                 |
| [Send network message [DEBUG MODE]](#send-network-message-[debug-mode])                                       |
| [Clear cache](#clear-cache)                                                                                   |
| [Get cell id](#get-cell-id)                                                                                   |
| [Get cell info](#get-cell-info)                                                                               |
| [Remove sprites on cells [RETRO]](#remove-sprites-on-cells-[retro])                                           |
| [Clear console [RETRO]](#clear-console-[retro])                                                               |
| [Remove sprites on cell](#remove-sprites-on-cell)                                                             |
| [Encode cells [RETRO]](#encode-cells-[retro])                                                                 |
| [Send plain network message [DEBUG MODE]](#send-plain-network-message-[debug-mode])                           |
| [Toggle debug mode](#toggle-debug-mode)                                                                       |
| [Decode cells [RETRO]](#decode-cells-[retro])                                                                 |
| [Switch servers fast [RETRO]](#switch-servers-fast-[retro])                                                   |
| [Set console log file [RETRO]](#set-console-log-file-[retro])                                                 |
| [Toggle fps counter](#toggle-fps-counter)                                                                     |
| [Get some info](#get-some-info)                                                                               |
| [Get lang file size](#get-lang-file-size)                                                                     |
| [Get picto list](#get-picto-list)                                                                             |
| [Get sprite list](#get-sprite-list)                                                                           |
| [Toggle log map disconnections [RETRO]](#toggle-log-map-disconnections-[retro])                               |
| [Check line of sight](#check-line-of-sight)                                                                   |
| [Get map id](#get-map-id)                                                                                     |
| [Search monster [CLASSIC]](#search-monster-[classic])                                                         |
| [Toggle sprite mount](#toggle-sprite-mount)                                                                   |
| [Find clip](#find-clip)                                                                                       |
| [Ping](#ping)                                                                                                 |
| [Flag picto](#flag-picto)                                                                                     |
| [Flag sprite](#flag-sprite)                                                                                   |
| [Get jail dialog [RETRO]](#get-jail-dialog-[retro])                                                           |
| [Reload](#reload)                                                                                             |
| [Set sprite size](#set-sprite-size)                                                                           |
| [Search alignment [RETRO]](#search-alignment-[retro])                                                         |
| [Search race [RETRO]](#search-race-[retro])                                                                   |
| [Search item [RETRO]](#search-item-[retro])                                                                   |
| [Search job [RETRO]](#search-job-[retro])                                                                     |
| [Search monster [RETRO]](#search-monster-[retro])                                                             |
| [Search npc [RETRO]](#search-npc-[retro])                                                                     |
| [Search quest [RETRO]](#search-quest-[retro])                                                                 |
| [Search spell [RETRO]](#search-spell-[retro])                                                                 |
| [Search sub area [RETRO]](#search-sub-area-[retro])                                                           |
| [Get sequencer actions [RETRO]](#get-sequencer-actions-[retro])                                               |
| [Toggle skip fight animations [ALPHA VERSION] [RETRO]](#toggle-skip-fight-animations-[alpha-version]-[retro]) |
| [Toggle skip fight ended ui [ALPHA VERSION] [RETRO]](#toggle-skip-fight-ended-ui-[alpha-version]-[retro])     |
| [Play sound](#play-sound)                                                                                     |
| [Get time](#get-time)                                                                                         |
| [Get timer count](#get-timer-count)                                                                           |
| [Toggle sprite visibility](#toggle-sprite-visibility)                                                         |
| [Toggle ui interface](#toggle-ui-interface)                                                                   |
| [Get tutorial variables](#get-tutorial-variables)                                                             |
| [Check client id](#check-client-id)                                                                           |
| [Zoom](#zoom)                                                                                                 |

## Syntax

```js
"a" = a IS TEXT
```

```js
a = a IS VARIABLE
```

```js
a b = JOIN a AND b WITH " "
```

```js
(a | b) = a OR b
```

```js
{a} = a IS OPTIONAL
```

## Commands

### Start sprite anim [DEBUG MODE]

```js
"/anim" animationName {timer}
```

### Show alert with lang

```js
"/askok" langId JOIN(langParam)
```

### Show alert with text

```js
"/askok2" text
```

### Send network message [DEBUG MODE]

```js
"/c" (SEND | PROCESS) message

SEND = ">"
PROCESS = "<"
```

### Clear cache

```js
"/cache"
```

### Get cell id

```js
"/cellid"
```

### Get cell info

```js
"/cellinfo" cell.id
```

### Remove sprites on cells [RETRO]

```js
"/cleancells"
```

### Clear console [RETRO]

```js
"/clear"
```

### Remove sprites on cell

```js
"/clearcell" cell.id
```

### Encode cells [RETRO]

```js
"/cryptcells" [cell.id, ","]
```

### Send plain network message [DEBUG MODE]

```js
"/d" (SEND | PROCESS) message

SEND = ">"
PROCESS = "<"
```

### Toggle debug mode

```js
"/debug"
```

### Decode cells [RETRO]

```js
"/decryptfightcells" cells
```

### Switch servers fast [RETRO]

```js
"/fastserverswitch" server.id
```

### Set console log file [RETRO]

```js
"/fileoutput" (DISABLED | ENABLED | FULL)

DISABLED = 0
ENABLED = 1
FULL = 2
```

### Toggle fps counter

```js
"/fps"
```

### Get some info

```js
"/infos"
```

### Get lang file size

```js
"/langfile" (TOTAL | LANG | langName)

TOTAL = "total"
LANG = "lang"
```

### Get picto list

```js
"/listpictos"
```

### Get sprite list

```js
"/listsprites"
```

### Toggle log map disconnections [RETRO]

```js
"/logdisco" {isEnabled}
```

### Check line of sight

```js
"/los" cell1.id cell2.id
```

### Get map id

```js
"/mapid"
```

### Search monster [CLASSIC]

```js
"/monster" monster.name
```

### Toggle sprite mount

```js
"/mount" {mount.modelId {rider.gfxId}}
```

### Find clip

```js
"/movieclip"
```

### Ping

```js
"/ping"
```

### Flag picto

```js
"/pointpicto" gfxId
```

### Flag sprite

```js
"/pointsprite" gfxId
```

### Get jail dialog [RETRO]

```js
"/printjaildialog"
```

### Reload

```js
"/reboot"
```

### Set sprite size

```js
"/scale" scaleX {scaleY}
```

### Search alignment [RETRO]

```js
"/searchalignment" alignment.name
```

### Search race [RETRO]

```js
"/searchbreed" race.name
```

### Search item [RETRO]

```js
"/searchitem" item.name
```

### Search job [RETRO]

```js
"/searchjob" job.name
```

### Search monster [RETRO]

```js
"/searchmonster" monster.name
```

### Search npc [RETRO]

```js
"/searchnpc" npc.name
```

### Search quest [RETRO]

```js
"/searchquest" quest.name
```

### Search spell [RETRO]

```js
"/searchspell" spell.name
```

### Search sub area [RETRO]

```js
"/searchsubarea" subArea.name
```

### Get sequencer actions [RETRO]

```js
"/seqactions"
```

### Toggle skip fight animations [ALPHA VERSION] [RETRO]

```js
"/skipfightanimations" {isEnabled}
```

### Toggle skip fight ended ui [ALPHA VERSION] [RETRO]

```js
"/skiplootpanel" {isEnabled}
```

### Play sound

```js
"/somaplay" soundName
```

### Get time

```js
"/time"
```

### Get timer count

```js
"/timerscount"
```

### Toggle sprite visibility

```js
"/togglesprites"
```

### Toggle ui interface

```js
"/ui" interfaceName
```

### Get tutorial variables

```js
"/vars"
```

### Check client id

```js
"/verifyidentity" clientId
```

### Zoom

```js
"/zoom" scale x y
```