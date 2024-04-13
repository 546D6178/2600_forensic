import subprocess
import configparser
import os
import re
from pathlib import Path

def run_cmd(cmd: str, raw=False) -> str:
	return subprocess.check_output(cmd, shell=True, text=(not raw))

def dir_path(string):
    #path_dir = os.path.abspath(string)
    if os.path.exists(string):
        path_dir = string
        if os.path.isdir(path_dir):
            return path_dir
        else:
            os.system(f"ls {path_dir}")
            print(path_dir)
            raise NotADirectoryError(path_dir)

#Get path value from config.ini
def get_path_in_ini(name : str):
    #Check config.ini exists
    if not os.path.isfile('config.ini'):
        raise ValueError(f"config.ini not found. Check config.ini exists and you execute main.py in src directory")

    config = configparser.ConfigParser()
    config.read('config.ini')
    path = config.get(name, 'path')

    #Case a path is undefined
    if path == "":
        raise ValueError(f"Please set a value in config.ini for {name}")
    return path

def is_command_available(command):
    """
    Vérifie si une commande est disponible.

    Args:
        command (str): Nom de la commande à vérifier.

    Returns:
        bool: True si la commande est disponible, False sinon.
    """
    
    command_list = command.split()
    try:
        # Exécutez la commande avec subprocess
        subprocess.run(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except FileNotFoundError:
        raise FileNotFoundError(f"Unable to find '{command}'. ")
    except subprocess.CalledProcessError:
        raise RuntimeError(f"Unable to exec '{command}'.")
	

def find_paths_in_folder(folder_path, pattern):
    """
    Recherche des chemins correspondant à un modèle dans un dossier.

    Args:
        folder_path (str): Chemin du dossier à parcourir.
        pattern (str): Modèle de recherche (regex).

    Returns:
        list: Liste des chemins correspondant au modèle.
    """
    for p in Path(folder_path).rglob( '*' ):
        #print( p )
        #print(pattern)
        #print(str(p))
        if re.search(pattern, str(p), flags=re.IGNORECASE):
            print(p)
            chemin_absolu = os.path.abspath(p)
            print(chemin_absolu)
            return str(chemin_absolu)

    return False

def find_multiple_paths_in_folder(folder_path, pattern):
    list_path = []
    for p in Path(folder_path).rglob( '*' ):
        if re.search(pattern, str(p), flags=re.IGNORECASE):
            chemin_absolu = os.path.abspath(p)
            list_path.append(str(chemin_absolu))
     
    if not list_path:
         return False
    else:
        return list_path
        
   

def escape_spaces(path):
    """
    Échappe les espaces dans le chemin donné.

    Args:
        path (str): Le chemin à traiter.

    Returns:
        str: Le chemin avec les espaces échappés.
    """
    # Divise le chemin en parties
    parts = path.split("/")
    # Échappe les espaces dans chaque partie du chemin
    escaped_parts = [part.replace(" ", r"\ ") for part in parts]
    # Rejoindre les parties échappées en un seul chemin
    escaped_path = "/".join(escaped_parts)
    return escaped_path