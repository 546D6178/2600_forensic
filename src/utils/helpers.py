import subprocess

def run_cmd(cmd: str, raw=False) -> str:
	return subprocess.check_output(cmd, shell=True, text=(not raw))