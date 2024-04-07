import re, os

from parsers import BaseParser
from utils import run_cmd


class EWFParser(BaseParser):
	def __init__(self, image_path):
		super().__init__(image_path)
		# Additional initialization for EWF-specific handling
		self.partitions = []

	def list_partitions(self):
		# Implementation for listing partitions in an EWF image

		if self.partitions:
			return self.partitions

		mmls_result = run_cmd(f"mmls -B {self.image_path}")
		
		if not 'GUID Partition Table (EFI)' in mmls_result:
				raise ValueError("mmls command failed.")
		
		self.partitions = []
		for line in list(filter(None, mmls_result.split("\n")))[4:]:
				partition_info = line.split()
				partition = {
						"number": int(partition_info[0][:-1]),
						"slot": partition_info[1],
						"start": partition_info[2],
						"end": partition_info[3],
						"length": partition_info[4],
						"size": partition_info[5],
						"name": " ".join(partition_info[6:]),
						"files": []
				}
				
				self.partitions.append(partition)

		if not self.partitions:
				raise ValueError("No partitions found in the EWF image")
		
		return self.partitions

	def list_files(self, partition):
		# Implementation for listing files in a partition of an EWF image

		if not self.partitions:
			self.list_partitions()

		if partition["files"]:
			return partition["files"]

		if not partition or not isinstance(partition, dict) or not partition in self.partitions:
			raise ValueError("Partition not found")

		fls_results = run_cmd(f"fls -r -mc -o {partition['start']} {self.image_path}")

		# FORMAT : MD5|name|inode|mode_as_string|UID|GID|size|atime|mtime|ctime|crtime
		# ($FILE_NAME), (deleted)

		if not fls_results:
			raise ValueError("fls command failed")
		
		files = []
		for line in list(filter(None, fls_results.split("\n"))):
			file_info = line.split("|")

			deleted = file_info[1].endswith("(deleted)")
			file_name = "($FILE_NAME)" in file_info[1]
			
			file_info[1] = file_info[1].replace(" ($FILE_NAME)", "").replace(" (deleted)", "")
			
			file = {
				"md5": file_info[0],
				"path": file_info[1],
				"name": file_info[1].split("/")[-1] if file_info[1][-1] != "/" else file_info[1].split("/")[-2],
				"inode": file_info[2].split('-')[0],
				"mode": file_info[3],
				"uid": file_info[4],
				"gid": file_info[5],
				"size": file_info[6],
				"atime": file_info[7],
				"mtime": file_info[8],
				"ctime": file_info[9],
				"crtime": file_info[10],
				"deleted": deleted,
				"file_name": file_name
			}
			files.append(file)

		partition["files"] = files

		return files

	def extract_file(self, partition, file, output_path):
		# Implementation for extracting a file from an EWF image
		if file['mode'][2] != 'd':
			if file["deleted"] == True:
				file["path"] += "_deleted"
			icat_result = run_cmd(cmd=f"icat -o {partition['start']} {self.image_path} {file['inode']}", raw=True)

			os.makedirs(f"{output_path}/{'/'.join(file['path'].split('/')[:-1])}",exist_ok=True)

			with open(f"{output_path}/{file['path']}", "wb") as f:
				f.write(icat_result)
			return

		else:
			
			for pfile in partition['files']:
				if file['path'] in pfile['path']:
					os.makedirs(f"{output_path}/{file['path']}", exist_ok=True)
