import yaml
import re

from extractors import BaseExtractor

def replace_placeholder(path: str) -> str:
    if(re.match(".*%[^/]+%.*",path)):
        #Replace username
        path = path.replace("%Username%","\w+")
        #Replace number
        path = path.replace("%Number%","\d+")
        #Replace for all directory
        path = path.replace("%Directory%",".*")
    return path

class RegistryExtractor(BaseExtractor):
    def __init__(self, source_path):
        super().__init__(source_path)
        # Additional setup for registry extraction

    def init_source_extract(self):
        self.path_to_extract = {}
        
        #open yml
        fd = open(self.source_path,"r")
        raw_content = fd.read()
        fd.close()

        #load yml content in self var
        self.path_to_extract = yaml.load(raw_content, Loader=yaml.Loader)

        return self.path_to_extract

    def check_file_to_extract(self, files):
        self.valid_path = []
        
        for category in self.path_to_extract:
            for path in self.path_to_extract[category]:
                
                #check if path contains placeholder (%xxxxx%)
                path = replace_placeholder(path)

                #search file which match with path
                for fil in files:
                    if re.search(f"{path}$",fil["path"]):
                        self.valid_path.append(fil)


        return self.valid_path

    def extract_data(self):
        # Implementation for extracting data from registry files
        extracted_data = {}
        # Extraction logic here
        return extracted_data

    def save_extracted_data(self, output_path):
        # Implementation for saving extracted registry data
        pass
        # Save logic here
