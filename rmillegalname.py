# #! /usr/bin/env python3
# -*- coding: utf-8 -*-

# This script renames files with illegal characters in their names
# such as <, >, :, ", /, \, |, ?, *


import os
import argparse
import re

# # Create the parser
parser = argparse.ArgumentParser(description='Rename files with illegal characters in their names')
parser.add_argument('directory', type=str, help='The directory to search for files with illegal characters in their names')

# Parse the arguments
args = parser.parse_args()

# check the file name contains only legal characters
def is_legal(input_string):
    # Regular expression to match only alphabet characters, numbers, or special characters
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_ +\'\-=\[\]{};:\\|,.<>\/?]*$'
    
    # Check if the input string matches the pattern
    if re.match(pattern, input_string):
        return True
    else:
        return False
    
def filter_string(input_string):
    pattern = r'[a-zA-Z0-9!@#$%^&*()_ +\'\-=\[\]{};:\\|,.<>\/?]*'
    filtered_string = ''.join(re.findall(pattern, input_string))
    return filtered_string
    
def get_extention(input_string):
    # Find the last occurrence of '.'
    last_dot_index = input_string.rfind('.')
    
    # Check if '.' exists in the string
    if last_dot_index != -1:
        # Extract the substring starting from the last '.' to the end of the string
        substring = input_string[last_dot_index:]
        return substring
    else:
        # If '.' is not found, return empty string
        return ""


def rename_illegal_files(directory):
    print(f"Searching for illegal file names in {directory}...")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not is_legal(file):
                print(f"Found illegal file name: {file}")
                print("enter skip to skip this file")
                rename = input("Do you want to rename it? (enter to remove illegal chars ): ")
                if rename == "skip":
                    print(f"Skipping file: {file}")
                    continue
                elif rename != "":
                    extention=get_extention(file)
                    new_path = os.path.join(root, rename+extention)
                    os.rename(os.path.join(root, file), new_path)
                    print(f"File renamed to: {rename+extention}")
                elif rename == "":
                    rename = filter_string(file)
                    new_path = os.path.join(root, rename)
                    os.rename(os.path.join(root, file), new_path)
                    print(f"File renamed to: {rename}")

if __name__ == "__main__":
    rename_illegal_files(args.directory)
    print("Done")