from processors import BaseProcessor
from utils import run_cmd, find_paths_in_folder, escape_spaces

class HindsightProcessor(BaseProcessor):
    def __init__(self, data_path, path_exe: str=None):
        super().__init__(data_path, path_exe)
        # Additional initialization for specific tool settings

    def analyze_data(self):

        # Implement analysis logic using other's tools
        
        # Analysis logic here

        pattern_chrome = r".*Chrome.*Default.*"
        pattern_edge = r".*Edge.*Default.*"

        match_chrome = find_paths_in_folder(self.data_path,pattern_chrome)
        match_edge = find_paths_in_folder(self.data_path,pattern_edge)

        #self.data_path = self.data_path + "/c/Users/Laurent/AppData/Local/Microsoft/Edge/User\ Data/Default"

        analysis_results = {}

        if match_chrome is not False:
            path = escape_spaces(match_chrome)
            run_cmd(f"{self.path_exe} -i {path} -l ../logs/hindsight_chrome.log -b Chrome -o {self.data_path}/hindsight_result_chrome -f jsonl")

        if match_edge is not False:
            path = escape_spaces(match_edge)
            run_cmd(f"{self.path_exe} -i {path} -l '../logs/hindsight_edge.log' -b Chrome -o '{self.data_path}/hindsight_result_edge' -f jsonl")

        return analysis_results

    def generate_report(self, analysis_results, report_path):
        # Format analysis_results into a readable report and save it to report_path
        
        pass
        # Report generation logic here
