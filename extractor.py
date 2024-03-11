import re 
import subprocess
import sys

def extract_offset(path_to_disk):

    commande = f"mmls {path_to_disk}"

    resultat_mmls = subprocess.check_output(commande, shell=True, text=True)

    regex = r'^\d+:\s+\d+\s+(\d+)\s+\d+\s+\d+\s+Basic data partition'
    correspondance = re.search(regex, resultat_mmls, re.MULTILINE)

    if correspondance:
        offset_start = correspondance.group(1)
        print("Offset de start :", offset_start)
    else:
        print("Aucune correspondance trouvée.")



if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) == 0:
        print("Utilisation: python script.py <path_to_disk>")
        sys.exit(1)

    fichier = "/mnt/share/Forensic_cours/ewf/disk/disk.E01"
    path_to_disk = fichier
    #path_to_disk = sys.argv[1]
    extract_offset(path_to_disk)


#/mnt/share/Forensic_cours/ewf/disk/disk.E01

