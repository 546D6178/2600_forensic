import os

from processors import BaseProcessor
from utils import run_cmd

class EvtxProcessor(BaseProcessor):
    def __init__(self, data_path, path_exe):
        super().__init__(data_path, path_exe)
        # Additional initialization for specific tool settings

    def analyze_data(self, extracted_file, report_path):
        os.makedirs(f"{os.path.join(report_path,"evtx_report")}",exist_ok=True)
        for file in extracted_file:
            if file["path"].endswith(".evtx"):
                run_cmd(f"`{self.path_exe}` -f {os.path.join(report_path,file[path])} --json \"{os.path.join(report_path,"evtx_report")}\"")
