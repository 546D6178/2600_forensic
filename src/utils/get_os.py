import subprocess
import platform

def run_cmd(cmd: str, raw=False) -> str:
	return subprocess.check_output(cmd, shell=True, text=(not raw))

def def_os() -> dict: 
	my_pc = {
		"platform":platform.system(),
		"release":platform.release(),
		"version":platform.version(),
		"machine":platform.machine(),
		"arch":platform.architecture(),
		"python_version":platform.python_version()
	}
	return my_pc


def which_os(my_pc: dict) -> str:
	if "Linux" in my_pc["platform"]:
		return("Linux")

	elif "Darwin" in my_pc["platform"]:
		return("Mac")

	elif "Windows" in platform.system():
		return("Windows")
	else:
		return("Error: OS not found")