from abc import ABC, abstractmethod

def replace_placeholder(path: str) -> str:
    if(re.match(".*%[^/]+%.*",path)) or "$" in path:
        #Replace username
        path = path.replace("%Username%","\w+")
        #Replace number
        path = path.replace("%Number%","\d+")
        #Replace for all directory
        path = path.replace("%Directory%",".*")
        #Replace $MFT
        path = path.replace("$","\$")
    return path

class BaseExtractor(ABC):
    def __init__(self, source_path):
        """
        Initialize the extractor with the path to the source data.

        Parameters:
        - source_path (str): The file path or directory containing the data to be extracted.
        """
        self.source_path = source_path

    @abstractmethod
    def init_source_extract(self):
        pass

    @abstractmethod
    def check_file_to_extract(self, files):
        pass

    @abstractmethod
    def extract_data(self):
        """
        Extracts relevant data based on specific criteria.

        This method should be implemented to parse the source data, apply any necessary filtering or processing,
        and return the extracted data in a structured format.

        Returns:
        - dict/list: The extracted data, structured in a way that is suitable for further analysis or processing.
        """
        pass

    @abstractmethod
    def save_extracted_data(self, output_path):
        """
        Saves the extracted data to a specified location.

        Parameters:
        - output_path (str): The file path or directory where the extracted data should be saved.

        This method should handle any necessary formatting or serialization of the extracted data before saving.
        """
        pass
