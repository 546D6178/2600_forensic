import os
from processors import BaseProcessor
from utils import run_cmd, find_multiple_paths_in_folder, def_os, which_os

class HindsightProcessor(BaseProcessor):
    def __init__(self, data_path, path_exe: str=None):
        super().__init__(data_path, path_exe)
        # Additional initialization for specific tool settings

    def analyze_data(self):

        # Implement analysis logic using other's tools
        
        # Analysis logic here

        pattern_chrome = r".*Chrome.*Default$"
        pattern_edge = r".*Edge.*Default$"

        match_chrome = find_multiple_paths_in_folder(self.data_path,pattern_chrome)
        match_edge = find_multiple_paths_in_folder(self.data_path,pattern_edge)

        #self.data_path = self.data_path + "/c/Users/Laurent/AppData/Local/Microsoft/Edge/User\ Data/Default"

        analysis_results = {}

        if match_chrome is not False:
            for file in match_chrome:
                output_file = os.path.join(self.data_path, "hindsight_result_chrome")
                my_pc = def_os()
                if which_os(my_pc) == "Windows":
                    res = run_cmd(f"{self.path_exe} -i \"{file}\" -l ../logs/hindsight_chrome.log -b Chrome -o \"{output_file}\" -f jsonl")
                else:
                    res = run_cmd(f"{self.path_exe} -i \"{file}\" -l '../logs/hindsight_chrome.log' -b Chrome -o \"{output_file}\" -f jsonl")
                if res is False:
                    print(f"La commande {self.path_exe} -i {file} -l '../logs/hindsight_chrome.log' -b Chrome -o '{output_file}' -f jsonl a échoué ou s'est mal terminée.")
                    break
                
        if match_edge is not False:
            for file in match_edge:
                output_file = os.path.join(self.data_path, "hindsight_result_edge")
                my_pc = def_os()
                if which_os(my_pc) == "Windows":
                    res = run_cmd(f"{self.path_exe} -i \"{file}\" -l ../logs/hindsight_edge.log -b Chrome -o \"{output_file}\" -f jsonl")
                else:
                    res = run_cmd(f"{self.path_exe} -i \"{file}\" -l '../logs/hindsight_edge.log' -b Chrome -o \"{output_file}\" -f jsonl")
                if res is False:
                    print(f"La commande {self.path_exe} -i {file} -l '../logs/hindsight_edge.log' -b Chrome -o '{output_file}' -f jsonl a échoué ou s'est mal terminée.")
                    break

        return analysis_results

    def generate_report(self, analysis_results, report_path):
        # Format analysis_results into a readable report and save it to report_path
        
        pass
        # Report generation logic here
