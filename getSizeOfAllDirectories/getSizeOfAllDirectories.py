# a programme that will calculate the size of all directories in a given path and print the size of each directory in the following format:
#
# Directory: <directory_name> Size: <size>
#

import os
import argparse

# Create the parser
parser = argparse.ArgumentParser(
    description="Calculate the size of all directories in a given path"
)
parser.add_argument(
    "path",
    type=str,
    nargs="?",
    default="",
    help="The path to calculate the size of all directories",
)

# Parse the arguments
args = parser.parse_args()


def get_size_of_all_directories(root):
    print(f"Calculating the size of all directories in the path {root}...")

    for item in os.listdir(root):
        get_total_size_of_the_directory(root, item)


def get_total_size_of_the_directory(root, path):
    size = 0
    absulate_path = os.path.join(root, path)
    if os.path.isfile(absulate_path):
        # for file calculate the size of the file
        try:
            size += os.path.getsize(absulate_path)
        except Exception as e:
            pass
    else:
        # for Directory calculate the size of all files in the directory
        for root, dirs, files in os.walk(absulate_path):
            # print(f"Calculating the size of {root}...")
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                # print(f"Calculating the size of {dir_path}...")
                try:
                    size += sum(
                        os.path.getsize(os.path.join(dir_path, file))
                        for file in os.listdir(dir_path)
                        if os.path.isfile(os.path.join(dir_path, file))
                    )
                except Exception as e:
                    pass
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    size += os.path.getsize(file_path)
                except Exception as e:
                    pass
    if size > 1e9:
        print(f"Directory: {path} Size: {size/1e9:.2f} GB")
    elif size > 1e6:
        print(f"Directory: {path} Size: {size/1e6:.2f} MB")
    elif size > 1e3:
        print(f"Directory: {path} Size: {size/1e3:.2f} KB")
    elif size > 0:
        print(f"Directory: {path} Size: {size} bytes")
    else:
        print(f"Directory: {path} Size: 0 bytes")


if __name__ == "__main__":
    path = args.path
    if path == "":
        print("Please provide a path to calculate the size of all directories")
        path = input("Enter the path: ")
    if os.path.exists(path):
        get_size_of_all_directories(path)
