import argparse, os
import parsers
import extractors
import processors
from utils import dir_path, get_path_in_ini, def_os, which_os

# Import all parsers, extractors and processors
# then make them available as command-line options
# This will make the tool automatically generate its 'cli' and 'help' options

# Create a list of all available parsers
available_parsers = [p for p in parsers.__dict__.keys() if "Parser" in p and "Base" not in p]

# Create a list of all available extractors
available_extractors = [e for e in extractors.__dict__.keys() if "Extractor" in e and "Base" not in e]

# Create a list of all available processors
available_processors = [p for p in processors.__dict__.keys() if "Processor" in p and "Base" not in p]

# Create the command-line argument parser
parser = argparse.ArgumentParser(description='Forensic Toolkit')
parser.add_argument('--image', '-i', dest="image_path", type=str, default=get_path_in_ini("Image_path") ,help='The path to the disk image')
parser.add_argument('--os', '-s', dest="os", type=str, default="Windows", help="OS of the disk image (default:Windows, Linux, Max)")
parser.add_argument('--output', '-o', dest="output_path", type=str, default=get_path_in_ini("Output_dir"), help='The path to the output directory')
parser.add_argument('--parser', '-p', dest="parser_type", type=str, default=available_parsers[0], choices=available_parsers, help='The type of parser to use')
args = parser.parse_args()

def main():
	# Initialize the parser with the disk image path
	parser = parsers.__dict__[args.parser_type](args.image_path)
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
	print("Selecting the disk OS")

	#Init file extractor with the correct yml
	if args.os == "Windows":
		print("Windows detected")
		## Need to parse targets from yaml file
		extractor = extractors.FileExtractor("./path_to_extract_windows.yml")
	elif args.os == "Linux":
		print("Linux detected")
		extractor = extractors.FileExtractor("./path_to_extract_linux.yml")
	elif args.os == "Mac":
		print("Mac detected")
		extractor = extractors.FileExtractor("./path_to_extract_mac.yml")
	else:
		raise ValueError("Error: Wrong OS in parameter (Windows or Linux os Mac)")

	#Init source before extract with yml
	extractor.init_source_extract()

	#Get all files available to extract in the disk image
	files_to_extract = extractor.check_file_to_extract(files)
	
	for file in [x for x in files_to_extract if x["deleted"] == False and x["file_name"] == False]:
		parser.extract_file(partition, file, args.output_path)

	print("Selecting the host OS")
	my_pc = def_os()

	match which_os(my_pc):
		case "Windows":
			print("Windows detected")
			#Execute processors compatible with Windows
			
			#EvtxECmd
			try:
				evtx = processors.EvtxProcessor(args.output_path,get_path_in_ini("EvtxECmd"))
				evtx.analyze_data(files_to_extract)
			except Exception as e:
				print(f"Processor EvtxECmd failed with the following error:\n{e}\nSkip")

			#Reg Ripper
			try:
				regripper = processors.RegRipperProcessor("./",get_path_in_ini("RegRipper"))
				regripper.analyze_data()
			except Exception as e:
				print(f"Processor Reg Ripper failed with the following error:\n{e}\nSkip")

			#Hindsight
			try:
				hindsight = processors.HindsightProcessor("./",get_path_in_ini("Hindsight"))
				hindsight.analyze_data()
			except Exception as e:
				print(f"Processor Hindsight failed with the following error:\n{e}\nSkip")
		
		case "Linux":
			print("Linux detected")
			#Execute processors compatible with Linux

			#Hindsight
			try:
				hindsight = processors.HindsightProcessor("./",get_path_in_ini("Hindsight"))
				hindsight.analyze_data()
			except Exception as e:
				print(f"Processor Hindsight failed with the following error:\n{e}\nSkip")

		case "Mac":
			print("Mac detected")
			#Execute processors compatible with Mac

		case _:
			raise ValueError("Error: OS not found")
		

if __name__ == "__main__":
	try:
		main()
		print(f"Extracted files can be found at {args.output_path}")
	except KeyboardInterrupt:
		print('Process interrupted by user')
