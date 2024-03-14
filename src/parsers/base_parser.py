from abc import ABC, abstractmethod

class BaseParser(ABC):
    def __init__(self, image_path):
        """
        Initialize the parser with the path to the disk image.

        Parameters:
        - image_path (str): The file path to the disk image.
        """
        self.image_path = image_path

    @abstractmethod
    def list_partitions(self):
        """
        List all partitions found in the disk image.

        Returns:
        - list: A list of partitions, each represented by a dictionary or a custom object.
        """
        pass

    @abstractmethod
    def list_files(self, partition):
        """
        List all files within a specified partition.

        Parameters:
        - partition: The partition from which to list files. This could be an index, identifier, or any partition-specific reference.

        Returns:
        - list: A list of files, each represented by a dictionary or a custom object.
        """
        pass

    @abstractmethod
    def extract_file(self, partition, file, output_path):
        """
        Extract a specific file from the disk image to a given output path.

        Parameters:
        - partition (obj): The partition object which contains all the partition info.
        - file (obj): The file object containing all the files info.
        - output_path (str): The path on the local filesystem where the extracted file should be saved.

        Returns:
        - bool: True if the file was successfully extracted, False otherwise.
        """
        pass
