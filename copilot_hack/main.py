import pyautogui
import os
import subprocess
import time
import re
import pyperclip

# Define the file path
base_path="/mnt/c/Users/hirok/Desktop/test/"
file_path = "test_cheat.py"
target_path = "c:/Users/hirok/Desktop/test/mission_cheat/"

ps="C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"

def activate_venv():
    venv_path = "./.venv/Scripts/activate"
    subprocess.run([ps, venv_path])

def filter_file(file_path=target_path):
    files=os.listdir(file_path)
    files=[file for file in files if file.endswith("i.cpp")]
    files=[os.path.join(file_path, file) for file in files]
    return files

def find_promt(file_path="i.cpp"):
    pattern=r"\/\*([ \w\d_.\n]*)##([ \w\d_.\n]*)\*\/"
    with open(file_path) as f:
        lines=f.readlines()
        lines=[line.strip() for line in lines]
        content="".join(lines)
        result=re.search(pattern, content)
        if result is not None:
            # extract groups
            groups=result.groups()
            return groups
        else:
            return None
process_id=None
def main():
    files=filter_file()
    files.sort()
    prev_prompts=[]
    prompts=[]
    for file in files:
        groups=find_promt(file)
        prompts.append(".".join(groups))
        if groups and len(groups[0]):
            pyperclip.copy(groups[0])
            process_id=subprocess.run([ps,"code","-n", file.replace("i.cpp", "o.cpp")])
            time.sleep(20)
            pyautogui.hotkey('ctrl', 'i')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            time.sleep(20)
            pyautogui.hotkey('ctrl', 'enter')
            pyautogui.hotkey('ctrl', 's')
            # pyautogui.hotkey('ctrl', 'w')

if __name__ == "__main__":
    # activate_venv()
    time.sleep(5)
    main()
    print(process_id)
exit()
# pyautogui.getWindowsWithProcess(process_id)[0].activate()

import SendKeys

# Specify the window title of the process
window_title = "MyProcess"

# Send the desired keystrokes
SendKeys.SendKeys(window_title + "{ENTER}")