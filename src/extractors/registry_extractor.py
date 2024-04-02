import yaml
import re

from extractors import BaseExtractor

def replace_placeholder(path: str) -> str:
    if(re.match(".*%[^/]+%.*",path)):
        #Replace username
        path = path.replace("%Username%","\w+")
        #Replace number
        path = path.replace("%Number%","\d+")
    return path

### EN COURS ###
def get_all_path_of_directory(path: str, files: list) -> str:
    path_checked = []

    for file in [x for x in files if x["file_name"] == False]:
        if any(path in file["path"]):
            #print(file["path"])
            path_checked.append(file["path"])
            #parser.extract_file(partition, file, args.output_path)
    return path_checked

class RegistryExtractor(BaseExtractor):
    def __init__(self, source_path):
        super().__init__(source_path)
        # Additional setup for registry extraction

    def init_source_extract(self):
        self.path_to_extract = {}
        
        fd = open(self.source_path,"r")
        raw_content = fd.read()
        fd.close()

        self.path_to_extract = yaml.load(raw_content, Loader=yaml.Loader)

        return self.path_to_extract

    def check_file_to_extract(self, files):
        self.valid_path = []
        
        for category in self.path_to_extract:
            for path in self.path_to_extract[category]:
                #check if path contains placeholder (%xxxxx%)
                path = replace_placeholder(path)

                ### EN COURS ###
                #Extract all directory
                if "%Directory%" in path:
                    path = path.replace("%Directory%","")
                    self.valid_path += get_all_path_of_directory(path, files)

                try:
                    path_checked = next(fil for fil in files if re.search(f"{path}$",fil["path"]))
                except:
                    pass
                else:
                    self.valid_path.append(path_checked)
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
