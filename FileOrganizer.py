import sys
import os
from JsonParser import JsonParser
from FileMatcher import FileMatcher
from FileMover import FileMover

if __name__ == "__main__":
    if (len(sys.argv) < 4):
        print("Usage: python FileOrganizer.py <path_to_source_folder> <path_to_destination_folder> <path_to_config_file>")
        sys.exit(1)

    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]
    organizer_config_file = sys.argv[3]


    if (not os.path.exists(organizer_config_file)):
        print("Config file does not exist")
        sys.exit(1)

    config_string = JsonParser.load_config(organizer_config_file)
    pattern_matches = JsonParser.get_pattern_matches(JsonParser.parse_config(config_string))
    file_matcher = FileMatcher(pattern_matches)
    file_mover = FileMover(file_matcher)

    for file in os.listdir(source_folder):
        file_mover.move(source_folder, destination_folder, file)
