import os
import shutil
import json

while True:
    source_folder = input("Enter the path of the folder you want to organize or 'x' to exit: " + "\n")
    if source_folder.lower() == 'x':
        print("Exiting the program.")
        exit()
    if os.path.isdir(source_folder):
        print(f"Organizing files in: {source_folder}")
        app_continue = input("Do you want to continue? (y/n): " + "\n")
        if app_continue.lower() == 'n':
            print("Exiting the program.")
            exit()
        elif app_continue.lower() == 'y':
            print("Continuing...")
    else:
        print(f"The path {source_folder} is not a valid directory.")
        exit()