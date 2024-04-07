import subprocess
import configparser
import os

def run_cmd(cmd: str, raw=False) -> str:
	return subprocess.check_output(cmd, shell=True, text=(not raw))

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def get_path_tools(tool_name : str):
	config = configparser.ConfigParser()
	config.read('../config.ini')
	return config.get(tool_name, 'path')

def is_command_available(command):
    """
    Vérifie si une commande est disponible.

    Args:
        command (str): Nom de la commande à vérifier.

    Returns:
        bool: True si la commande est disponible, False sinon.
    """
    try:
        # Exécutez la commande avec subprocess
        subprocess.run([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except FileNotFoundError:
        raise FileNotFoundError(f"Unable to find '{command}'. ")
    except subprocess.CalledProcessError:
        raise RuntimeError(f"Unable to exec '{command}'.")
		