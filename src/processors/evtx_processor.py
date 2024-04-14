import os

from processors import BaseProcessor
from utils import run_cmd

class EvtxProcessor(BaseProcessor):
    def __init__(self, data_path, path_exe):
        super().__init__(data_path, path_exe)
        # Additional initialization for specific tool settings

    def analyze_data(self, extracted_file):
        output_path = os.path.abspath(self.data_path)
        os.makedirs(f"{os.path.join(output_path,'evtx_report')}",exist_ok=True)
        for file in extracted_file:
            if file["path"].endswith(".evtx"):
                run_cmd(f"`{self.path_exe}` -f {os.path.join(output_path,file['path'])} --json \"{os.path.join(output_path,'evtx_report')}\"")

    def generate_report(self, analysis_results, report_path):
        pass