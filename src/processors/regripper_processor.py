import subprocess
import os
from utils import find_paths_in_folder, find_multiple_paths_in_folder
from datetime import datetime

from processors import BaseProcessor

class RegRipperProcessor(BaseProcessor):
    def __init__(self, data_path, path_exe: str=None):
        """
        Initialization of class and verification of the path of global variables.

        Parameters:
            - path_exe: Path to Reg Ripper executable
        """
        super().__init__(data_path, path_exe)


    def execute_regripper_by_plugin(self, filepath: str, plugin_name: str):
        """
        Execute Reg Ripper with the specified plugin and redirect output to a file.
        """
        command = [self.path_exe, "-r", filepath, "-p", plugin_name]
        
        output_dir = self.data_path
        unique_id = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{plugin_name}_{unique_id}"
        output_file = os.path.join(output_dir, filename)
        
        with open(output_file, 'w') as f:
            ret = subprocess.run(command, stdout=f, stderr=subprocess.PIPE, text=True)
            if ret.returncode != 0:
                raise RuntimeError(f"An unexpected error occured in {self.execute_regripper_by_plugin.__name__} function with plugin {plugin_name} .\n" + \
                        "Subprocess response:\n{}".format(ret.stdout.strip()))
        return ret


    def exec_usbstor(self, filepath: str):
        """
        Execute Reg Ripper with usbstor plugin.
        """
        return self.execute_regripper_by_plugin(filepath, "usbstor")
        
    def exec_mountdev(self, filepath: str):
        """
        Execute Reg Ripper with mountdev plugin.
        """
        return self.execute_regripper_by_plugin(filepath, "mountdev")
    
    def exec_mp2(self, filepath: str):
        """
        Execute Reg Ripper with mp2 plugin.
        """
        return self.execute_regripper_by_plugin(filepath, "mp2")

    def exec_shellbags(self, filepath: str):
        """
        Execute Reg Ripper with shellbags plugin.
        """
        return self.execute_regripper_by_plugin(filepath, "shellbags")

    def exec_userassist(self, filepath: str):
        """
        Execute Reg Ripper with userassist plugin.
        """
        return self.execute_regripper_by_plugin(filepath, "userassist")
    
    def exec_recentdocs(self, filepath: str):
        """
        Execute Reg Ripper with recentdocs plugin.
        """
        return self.execute_regripper_by_plugin(filepath, "recentdocs")

    def exec_networklist(self, filepath: str):
        """
        Execute Reg Ripper with networklist plugin.
        """
        return self.execute_regripper_by_plugin(filepath, "networklist")
    

    def analyze_data(self):
        #pas teste encore
        path_system_hive = find_paths_in_folder(self.data_path, r".*[\\/](c[\\/])?Windows[\\/]?System32[\\/]?config[\\/]?SYSTEM")
        ntuserdotdat = find_multiple_paths_in_folder(self.data_path, r".*[\\/](c[\\/])?Users[\\/][^\\/]+[\\/]?NTUSER\.DAT")
        userclassdotdat = find_multiple_paths_in_folder(self.data_path, r".*[\\/](c[\\/])?Users[\\/][^\\/]+[\\/]?AppData[\\/]?Local[\\/]?Microsoft[\\/]?Windows[\\/]?UsrClass\.dat")
        path_software_hive = find_paths_in_folder(self.data_path, r".*[\\/](c[\\/])?Windows[\\/]?System32[\\/]?config[\\/]?SOFTWARE")


        if path_system_hive:
            self.exec_usbstor(path_system_hive) 
            self.exec_mountdev(path_system_hive)
        if ntuserdotdat:
            for file in ntuserdotdat:
                self.exec_mp2(file)
                self.exec_recentdocs(file)
                self.exec_userassist(file)
        if userclassdotdat:
            for file in userclassdotdat:
                self.exec_shellbags(file)
        if path_software_hive:
            self.exec_networklist(path_software_hive)


    def generate_report(self, analysis_results, report_path):
        # Format analysis_results into a readable report and save it to report_path
        
        pass
        # Report generation logic here
