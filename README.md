# 2600_forensic

## Prérequis 

- sleuth kit
- reg ripper
- evtxcmd ? (evtx to json)
- hindsight-master ? (extraire donnée de navigation)


## Liste minimum à extraire

Attention, les chemins sont normalement sous Windows séparés par des `\`, mais dans fls c'est le `/` qui est utilisé. Exemple : `c/Users/Laurent/AppData/Local/Microsoft/Edge/User Data/Default/History`

### Le registre

- c/Windows/System32/config/SAM
- c/Windows/System32/config/SECURITY
- c/Windows/System32/config/SOFTWARE
- c/Windows/System32/config/SYSTEM
- c/Users/%Username%/NTUSER.DAT
- c/Users/%Username%/AddData/Local/Microsoft/Windows/UsrClass.dat
- c/Windows/inf/setupapi.dev.log
- c/Windows/system32/sru/SRUDB.dat

### Navigation internet 

(historique, download, cookie, cache)

#### EGDE 

- c/Users/%Username%/AppData/Local/Microsoft/Edge/User Data/Default/History
- c/Users/%Username%/AppData/Local/Microsoft/Edge/User Data/Default/History-journal
- c/Users/Your_User_Name/AppData/Local/Microsoft/Edge/User Data/Default/Network/cookie


#### Firefox

C:\Users\Your_User_Name\AppData\Roaming\Mozilla\Firefox\Profiles\xxxx.default-release\cookie.sqlite

#### Chrome

#### Internet Explorer 

