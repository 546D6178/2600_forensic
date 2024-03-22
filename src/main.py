import argparse, os
import parsers
import extractors
import processors

# Import all parsers, extractors and processors
# then make them available as command-line options
# This will make the tool automatically generate its 'cli' and 'help' options

# Move this to helpers
def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)
		

# Create a list of all available parsers
available_parsers = [p for p in parsers.__dict__.keys() if "Parser" in p and "Base" not in p]

# Create a list of all available extractors
available_extractors = [e for e in extractors.__dict__.keys() if "Extractor" in e and "Base" not in e]

# Create a list of all available processors
available_processors = [p for p in processors.__dict__.keys() if "Processor" in p and "Base" not in p]

# Create the command-line argument parser
parser = argparse.ArgumentParser(description='Forensic Toolkit')
parser.add_argument('--image', '-i', dest="image_path", type=str, help='The path to the disk image')
parser.add_argument('--output', '-o', dest="output_path", type=dir_path, default="output", help='The path to the output directory')
parser.add_argument('--parser', '-p', dest="parser_type", type=str, default=available_parsers[0], choices=available_parsers, help='The type of parser to use')
parser.add_argument('--extractors', '-e', dest="extractor_type", type=str, default=available_extractors[0], choices=available_extractors, help='The types of extractors to use', nargs='+')
parser.add_argument('--processors', '-pr', dest="processor_type", type=str, default=available_processors[1], choices=available_processors, help='The types of processors to use', nargs='+')
args = parser.parse_args()

def main():
		# Initialize the parser with the disk image path
		parser = parsers.__dict__[args.parser_type](args.image_path)
		processor = processors.__dict__[args.processor_type](args.output_path)
		# List all partitions in the disk image
		print("="*50)
		print(f"Listing partitions in the disk image: {args.image_path}")
		partitions = parser.list_partitions()
	
		# Show partitions to the user and ask which partition to list files from
		print("Partitions found in the disk image:")
		for partition in partitions:
			print(f" {partition['number']}. {partition['name']} ({partition['size']})")

		print("Selecting the Basic data partition")
		partition_number = [x["number"] for x in partitions if x["name"] == "Basic data partition"][0]

		# Find the partition object that matches the user's choice
		partition = next((x for x in partitions if x["number"] == partition_number), None)

		print("="*50)

		print(f"Listing files in the selected partition: {partition['name']}")

		# List all files within the specified partition
		files = parser.list_files(partition)

		# Show user stats about the files in the partition
		print(f"Files found in the partition: {len(files)}")
		print(f"Total size of files: {sum([int(x['size']) for x in files])} bytes")

		print("="*50)

		## Need to parse targets from yaml file
		targets = ["c/Users/Laurent/AppData/Local/Microsoft/Edge/User Data/Default"]

		# Extract the specified file to the output directory
		#for file in [x for x in files if x["deleted"] == False and x["file_name"] == False]:
		for file in [x for x in files if x["file_name"] == False]:
			if any([x in file["path"] for x in targets]):
				#print(file["path"])
				parser.extract_file(partition, file, args.output_path)

		processor.analyze_data()
		

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print('Process interrupted by user')