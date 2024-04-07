from abc import ABC, abstractmethod
import os
import subprocess
import utils

class BaseProcessor(ABC):
    def __init__(self, data_path, path_exe: str=None):
        """
        Initialize the processor with the path to the data that needs to be analyzed.

        Parameters:
        - data_path (str): The file path or directory containing the data for analysis.
        """
        self.data_path = data_path

        #get_path_tool if path_exe is None
        if path_exe is None:
            class_name = type(self).__name__[:-len("Processor")]
            path_exe = utils.get_path_in_ini(class_name)

        # check if executable is installed
        if not os.path.exists(self.path_exe):
            raise FileNotFoundError(f"{os.path.basename(self.path_exe)} not found on system. Please verify your {os.path.basename(self.path_exe)} path into your config.py file.")

        # check if executable is functional
        ret = subprocess.run(self.path_exe, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if ret.returncode != 0:
            raise ValueError(f"Cannot execute {os.path.basename(self.path_exe)}. Please verify your {os.path.basename(self.path_exe)} path into your config.py file.")
        
        self.path_exe = path_exe
        


    @abstractmethod
    def analyze_data(self):
        """
        Analyze the data using specific forensic tools or algorithms.

        This method should implement the logic to process the data according to the requirements
        of the forensic analysis tool it interfaces with. The method can return results in a variety
        of formats, depending on what's most appropriate for the analysis being performed.

        Returns:
        - Any: The results of the analysis, which could be a dict, list, or any structured data format suitable for reporting or further processing.
        """
        pass

    @abstractmethod
    def generate_report(self, analysis_results, report_path):
        """
        Generate a report based on the analysis results.

        Parameters:
        - analysis_results: The results returned by the `analyze_data` method.
        - report_path (str): The file path where the report should be saved.

        This method should handle formatting the analysis results into a human-readable report,
        which could be a text file, PDF, HTML, or any other suitable format.
        """
        pass
