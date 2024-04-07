import subprocess
import os

from helpers import BaseHelper

class RegRipperHelper(BaseHelper):
    def __init__(self, path_exe: str) -> None:
        """
        Initialization of class and verification of the path of global variables.

        Parameters:
            - path_exe: Path to Reg Ripper executable
        """
        super().__init__(path_exe)

    def exec_usbstor(self, filepath: str):
        """
        Execute Reg Ripper with usbstor plugin.
        """
        command = [self.path_exe, "-r", filepath, "-p", "usbstor"]
        ret = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if ret.returncode != 0:
            raise RuntimeError("An unexpected error occured in exec_usbstor function.\n" + \
                    "Subprocess response:\n{}".format(ret.stdout.strip()))
        return ret
        
    def exec_mountdev(self, filepath: str):
        """
        Execute Reg Ripper with mountdev plugin.
        """
        command = [self.path_exe, "-r", filepath, "-p", "mountdev"]
        ret = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if ret.returncode != 0:
            raise RuntimeError("An unexpected error occured in exec_mountdev function.\n" + \
                    "Subprocess response:\n{}".format(ret.stdout.strip()))
        return ret
   
    def exec_mp2(self, filepath: str):
        """
        Execute Reg Ripper with mp2 plugin.
        """
        command = [self.path_exe, "-r", filepath, "-p", "mp2"]
        ret = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if ret.returncode != 0:
            raise RuntimeError("An unexpected error occured in exec_mp2 function.\n" + \
                    "Subprocess response:\n{}".format(ret.stdout.strip()))
        return ret
      
    def exec_shellbags(self, filepath: str):
        """
        Execute Reg Ripper with shellbags plugin.
        """
        command = [self.path_exe, "-r", filepath, "-p", "shellbags"]
        ret = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if ret.returncode != 0:
            raise RuntimeError("An unexpected error occured in exec_shellbags function.\n" + \
                    "Subprocess response:\n{}".format(ret.stdout.strip()))
        return ret
