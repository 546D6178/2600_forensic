import os
import subprocess
#from abc import ABC, abstractmethod

class BaseHelper():
    def __init__(self, path_exe: str) -> None:
        """
        Initialization of class and verification of the path of global variables.

        Parameters:
            - path_exe: Path to executable
        """
        self.path_exe = path_exe

        # check if executable is installed
        if not os.path.exists(self.path_exe):
            raise FileNotFoundError(f"{os.path.basename(self.path_exe)} not found on system. Please verify your {os.path.basename(self.path_exe)} path into your config.py file.")

        # check if executable is functional
        ret = subprocess.run(self.path_exe, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if ret.returncode != 0:
            raise ValueError(f"Cannot execute {os.path.basename(self.path_exe)}. Please verify your {os.path.basename(self.path_exe)} path into your config.py file.")
        