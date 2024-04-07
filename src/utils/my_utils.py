import subprocess
import configparser

def run_cmd(cmd: str, raw=False) -> str:
	return subprocess.check_output(cmd, shell=True, text=(not raw))


def get_path_tools(tool_name : str):
	config = configparser.ConfigParser()
	config.read('../config.ini')
	return config.get(tool_name, 'path')