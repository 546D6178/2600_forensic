import re 
import subprocess
#import sys


fichier = "/mnt/share/Forensic_cours/ewf/disk/disk.E01" #input("Entrez le chemin du fichier : ")

commande = f"mmls {fichier}"

resultat_mmls = subprocess.check_output(commande, shell=True, text=True)

regex = r'^\d+:\s+\d+\s+(\d+)\s+\d+\s+\d+\s+Basic data partition'
correspondance = re.search(regex, resultat_mmls, re.MULTILINE)

if correspondance:
    offset_start = correspondance.group(1)
    print("Offset de start :", offset_start)
else:
    print("Aucune correspondance trouvée.")

#/mnt/share/Forensic_cours/ewf/disk/disk.E01

