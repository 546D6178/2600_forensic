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

Google like Browser : [click here](https://www.foxtonforensics.com/browser-history-examiner/chrome-history-location)

Firefox : [another one](https://www.foxtonforensics.com/browser-history-examiner/firefox-history-location)

Possible d'ajouter Opera, Opera GX, Brave etc

#### EGDE 

- c/Users/%Username%/AppData/Local/Microsoft/Edge/User Data/Default/History
- c/Users/%Username%/AppData/Local/Microsoft/Edge/User Data/Default/History-journal
- c/Users/Your_User_Name/AppData/Local/Microsoft/Edge/User Data/Default/Network/cookie
- c/Users/Your_User_Name/AppData/Local/Microsoft/Edge/User Data/Default/Cache
- c/Users/Your_User_Name/AppData/Local/Microsoft/Edge/User Data/Default/Bookmarks


#### Firefox

- c/Users/Your_User_Name/AppData/Roaming/Mozilla/Firefox/Profiles/xxxx.default-release/cookie.sqlite

- c/Users/Your_User_Name/AppData/Local/Mozilla/Firefox/Profiles/xxxx.default-release/cookie.sqlite
- c/Users/Your_User_Name/AppData/Local/Mozilla/Firefox/Profiles/

#### Chrome

- c/Users/Your_User_Name/AppData/Local/Google/Chrome/User Data/Default/Network/cookie
- c/Users/Your_User_Name/AppData/Local/Google/Chrome/User Data/Default/History-journal
- c/Users/Your_User_Name/AppData/Local/Google/Chrome/User Data/Default/History
- c/Users/Your_User_Name/AppData/Local/Google/Chrome/User Data/Default/Cache
- c/Users/Your_User_Name/AppData/Local/Google/Chrome/User Data/Default/Bookmarks


#### Internet Explorer 



## Journaux Windows EVTX

- C/Windows/system32/winevt/logs/system.evtx
- C/Windows/system32/winevt/logs/security.evtx
- C/Windows/system32/winevt/logs/application.evtx
- C/Windows/system32/winevt/logs/powershell.evtx
- C/Windows/system32/winevt/logs/wmi.evtx
- C/Windows/system32/winevt/logs/WindowsDefender.evtx
- C/Windows/system32/winevt/logs/RDP.evtx



## Fichiers Linux 

### Log 


### Conf


### any ideas ? 
