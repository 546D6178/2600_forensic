import argparse, os
from parsers import EWFParser
from extractors import RegistryExtractor

# Import all parsers, extractors and processors
# then make them available as command-line options
# This will make the tool automatically generate its 'cli' and 'help' options

# Move this to helpers
def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser(description='Forensic Toolkit')
parser.add_argument('--image', '-i', dest="image_path", type=str, help='The path to the disk image')
parser.add_argument('--output', '-o', dest="output_path", type=dir_path, help='The path to the output directory')
args = parser.parse_args()

def main():
		# Initialize the parser with the disk image path
		parser = EWFParser(args.image_path)

		# List all partitions in the disk image
		partitions = parser.list_partitions()
		print("list partition done")

		# # Show partitions to the user and ask which partition to list files from
		# print("Partitions found in the disk image:")
		# for partition in partitions:
		# 	print(f" {partition['number']}. {partition['name']} ({partition['size']})")
		# partition_number = int(input("Enter the number of the partition you would like to use: "))
		partition_number = [x["number"] for x in partitions if x["name"] == "Basic data partition"][0]

		# Find the partition object that matches the user's choice
		partition = next((x for x in partitions if x["number"] == partition_number), None)

		# print("="*50)

		# List all files within the specified partition
		files = parser.list_files(partition)

		## Need to parse targets from yaml²
		extractor = RegistryExtractor("./path_to_extract.yml")
		extractor.init_source_extract()

		files_to_extract = extractor.check_file_to_extract(files)

		for file in files_to_extract:#for file in [x for x in files_to_extract if x["deleted"] == False and x["file_name"] == False]:
			parser.extract_file(partition,file,args.output_path)

		#targets = [""]

		# Extract the specified file to the output directory
		#for file in [x for x in files if x["deleted"] == False and x["file_name"] == False]:
		#	if any([x in file["path"] for x in targets]):
		#		parser.extract_file(partition, file, args.output_path)

    # # Iterate over each partition and list the files within it
    # for partition in partitions:
    #     files = parser.list_files(partition)
    #     for file in files:
    #         # Extract each file to the specified output directory
    #         parser.extract_file(file, args.output_path)


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print('Process interrupted by user')
