import pyautogui
import os
import subprocess
import time
import re
import pyperclip
import sys

# inputPath = sys.argv[1]
# outputPath = sys.argv[2]



# Define the file path
base_path = "/mnt/c/Users/hirok/Desktop/test/"
file_path = "test_cheat.py"
target_path = "/media/sf_vmUbuntuGeneral/mission_cheat/"

ps = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"

def check_and_delete_ofile(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def activate_venv():
    venv_path = "./.venv/Scripts/activate"
    subprocess.run([venv_path])


def filter_file(file_path):
    # filter file with content having "target"
    pattern = r"  "

    files = os.listdir(file_path)
    files = [file for file in files if file.endswith("i.cpp")]
    paths = [os.path.join(file_path, file) for file in files]
    return files, paths


def find_promt(file_path):
    pattern = r"\/\*([\s\S]*)##([ \w\d_.\n]*)\*\/"
    with open(file_path) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        content = "".join(lines)
        result = re.search(pattern, content)
        if result is not None:
            # extract groups
            groups = result.groups()
            return groups
        else:
            return None


def main(prompts):
    # time.sleep(20)
    files, paths = filter_file()
    # print("files", files)
    # print("paths", paths)
    files.sort()
    for file, path in zip(files, paths):
        groups = find_promt(path)
        print(groups)
        if groups and prompts.get(file) != groups[0]:
            prompts[file] = groups[0]
        else:
            continue
        if groups and len(groups[0]):
            pyperclip.copy(groups[0])
            opath = path.replace("i.cpp", "o.cpp")
            check_and_delete_ofile(opath)
            process_id = subprocess.run(["code", opath])
            time.sleep(5)
            pyautogui.hotkey("ctrl", "i")
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("enter")
            time.sleep(20)
            pyautogui.hotkey("ctrl", "enter")
            time.sleep(1)
            pyautogui.hotkey("ctrl", "s")
            time.sleep(1)
            pyautogui.hotkey("ctrl", "w")


if __name__ == "__main__":
    # activate_venv()
    time.sleep(5)
    prompts = {}
    while True:
        main(prompts)
        print("one iteration done")
exit()
