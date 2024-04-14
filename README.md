# 2600_forensic

## Descriptions 

Voici notre outil d’extraction de données forensique. 

## Prérequis et installation

- The Sleuth Kit
- [reg ripper](https://github.com/keydet89/RegRipper3.0)
- [evtxcmd](https://github.com/EricZimmerman/evtx)
- [hindsight-master](https://github.com/obsidianforensics/hindsight) (extraire donnée de navigation)

Veuillez renseignez les liens des outils dans le fichier ``config.ini`` en respectant le format attendu. 

L'installation des requierements : `pip3 install -r requirements.txt`

## Notes

Attention, les chemins sont normalement sous Windows séparés par des `\`, mais dans fls c'est le `/` qui est utilisé. Exemple : `c/Users/Laurent/AppData/Local/Microsoft/Edge/User Data/Default/History`

Nous gérons une liste de fichier à extraire en fonction de l'OS de l'image disque cible via les fichiers `path_to_extract_%os_name%`.  

## Utilisation 

Vous pouvez obtenir le message d'aidee avec un `-h `

````bash
python3 main.py -h                                              
usage: main.py [-h] [--image IMAGE_PATH] [--os OS] [--output OUTPUT_PATH] [--parser {EWFParser}] [--extractors {FileExtractor} [{FileExtractor} ...]]
               [--processors {HindsightProcessor,RegRipperProcessor} [{HindsightProcessor,RegRipperProcessor} ...]]

Forensic Toolkit

options:
  -h, --help            show this help message and exit
  --image IMAGE_PATH, -i IMAGE_PATH
                        The path to the disk image
  --os OS, -s OS        OS of the disk image (default:Windows, Linux, Max)
  --output OUTPUT_PATH, -o OUTPUT_PATH
                        The path to the output directory
  --parser {EWFParser}, -p {EWFParser}
                        The type of parser to use
  --extractors {FileExtractor} [{FileExtractor} ...], -e {FileExtractor} [{FileExtractor} ...]
                        The types of extractors to use
  --processors {HindsightProcessor,RegRipperProcessor} [{HindsightProcessor,RegRipperProcessor} ...], -pr {HindsightProcessor,RegRipperProcessor} [{HindsightProcessor,RegRipperProcessor} ...]
                        The types of processors to use
````

Le script lorsqu'il est appelé interprète l'OS cible de l'image disque comme Windows par défaut. 

Le chemin de l'image s'il n'est pas renseigné sera celui définit dans ``[Image_path]`` dans le fichier ``config.ini``.

Le script lance donc les outils disponibles. 

Les fichiers extraits iront dans le dossier ``OUTPUT_PATH`` qui par défaut est le fichier définit ``[Output_dir]`` dans le fichier ``config.ini``.

Vous pouvez retrouver les logs d'executions dans le dossier `logs`. 