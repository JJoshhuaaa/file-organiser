import json

class JsonParser:
    """
    A class to and access JSON files.
    """

    @staticmethod
    def load_config(config_file: str) -> str:
        """
        Load a JSON file into a string.
        """
        with open(config_file, 'r') as config_file:
            return config_file.read()

    @staticmethod
    def parse_config(config_string: str) -> dict:
        """
        Parse a JSON string into a dictionary.
        """
        return json.loads(config_string)

    @staticmethod
    def get_pattern_matches(parsed_config: dict, pattern_matches_param: dict = {}, current_pattern_path: str = "FileOrganizer/") -> dict:
        """
        Get the pattern matches from a parsed config.
        """
        pattern_matches = pattern_matches_param

        for directory in parsed_config['dir']:
            if "dir" in directory:
                JsonParser.get_pattern_matches(directory, pattern_matches, current_pattern_path + directory['name'] + "/")
            else:
                for extension in directory['extensions']:
                    pattern_matches[extension] = current_pattern_path + directory['name'] + "/"

        return pattern_matches






    

    