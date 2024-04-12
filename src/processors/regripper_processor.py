import subprocess
import os
from utils import find_paths_in_folder

from processors import BaseProcessor

class RegRipperProcessor(BaseProcessor):
    def __init__(self, data_path, path_exe: str) -> None:
        """
        Initialization of class and verification of the path of global variables.

        Parameters:
            - path_exe: Path to Reg Ripper executable
        """
        super().__init__(data_path, path_exe)

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


    def analyze_data(self):
        #pas tester encore
        path_system_hive = find_paths_in_folder(self.data_path, r"*.c/Windows/System32/config/SYSTEM.*")
        ntuserdotdat = find_paths_in_folder(self.data_path, r"*.c/Users/%Username%/NTUSER.DAT.*")
        userclassdotdat = find_paths_in_folder(self.data_path, r"*.c/Users/%Username%/AppData/Local/Microsoft/Windows/UsrClass.dat.*")
        path_software_hive = find_paths_in_folder(self.data_path, r"*.c/Windows/System32/config/SOFTWARE.*")

        if path_system_hive:
            exec_usbstor(self, path_system_hive) 
            exec_mountdev(self, path_system_hive)
        if ntuserdotdat:
            exec_mp2(self, ntuserdotdat)
        if userclassdotdat:
            exec_shellbags(self, userclassdotdat)
        if path_software_hive:
            pass
