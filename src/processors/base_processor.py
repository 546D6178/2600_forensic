from abc import ABC, abstractmethod

class BaseProcessor(ABC):
    def __init__(self, data_path):
        """
        Initialize the processor with the path to the data that needs to be analyzed.

        Parameters:
        - data_path (str): The file path or directory containing the data for analysis.
        """
        self.data_path = data_path

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
