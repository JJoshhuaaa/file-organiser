import os
from FileMatcher import FileMatcher

class FileMover:
    def __init__(self, file_matcher: FileMatcher):
        self.file_matcher = file_matcher

    def move(self, file_path_old: str, file_path_new: str, file_name: str):
        file_match = self.file_matcher.match(file_name)
        
        if (file_match is None):
            raise ValueError("File does not match any pattern")
        
        if (not os.path.exists(file_path_new + "/" + file_match)):
            os.makedirs(file_path_new + "/" + file_match)

        os.rename(file_path_old + "/" + file_name, file_path_new + "/" + self.file_matcher.match(file_name) + file_name)