import pyperclip
import os


# get last copy from the clipboard if it is     a text
def get_clipboard_text():
    return pyperclip.paste()


# set path to the file
# get text from the file endswith i.txt
def get_file_text(path="."):
    # list all files in the current directory and get the last file that ends with i.txt
    files = [f for f in os.listdir(".") if f.endswith("i.txt")][
        0
    ]  # get the first file that ends with i.txt
    if len(files) == 0:
        return ""  # return empty string if no file found
    file_path = os.path.join(path, files)  # get the full path of the file
    with open(file_path, "r") as file:
        return file.read()
