from processors import BaseProcessor
from utils import run_cmd

class HindsightProcessor(BaseProcessor):
    def __init__(self, data_path, path_exe):
        super().__init__(data_path, path_exe)
        # Additional initialization for specific tool settings

    def analyze_data(self):

        matching_folders = []

        for item in self.data_path:
            return 1
        # in progress


        self.data_path = self.data_path + "/c/Users/Laurent/AppData/Local/Microsoft/Edge/User\ Data/Default"

        # Implement analysis logic using other's tools
        analysis_results = {}
        # Analysis logic here

        print(f"RUNNING hindsight.py -i `{self.data_path}` -l logs/hindsight.log -b Chrome -o output/hindsight_result -f jsonl")
        hindsight_result = run_cmd(f"`{self.path_exe}` -i {self.data_path} -l logs/hindsight.log -b Chrome -o output/hindsight_result -f jsonl")
        #hindsight.py -i repertoire_Browser -b Chrome -o navigation -f jsonl

        return analysis_results

    def generate_report(self, analysis_results, report_path):
        # Format analysis_results into a readable report and save it to report_path
        pass
        # Report generation logic here
