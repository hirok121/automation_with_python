import pyautogui
import os
import subprocess
import time
import re
import pyperclip

import ctypes
# from ctypes import VK_CONTROL, VK_RETURN,VK_I, WM_KEYDOWN, WM_KEYUP
import ctypes

# Virtual-Key Codes
VK_CONTROL = 0x11
VK_RETURN = 0x0D
VK_I = 0x49

# Windows Messages
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101


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
    paths=[os.path.join(file_path, file) for file in files]
    return files, paths

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
    files,paths=filter_file()
    files.sort()
    prev_prompts=[]
    prompts=[]
    for file ,path in zip(files,paths):
        groups=find_promt(file)
        prompts.append(".".join(groups))
        if groups and len(groups[0]):
            pyperclip.copy(groups[0])
            process_id=subprocess.run([ps,"code","-n", file.replace("i.cpp", "o.cpp")])
            time.sleep(2)
            pyautogui.hotkey('win', 'm')
            window_title = file.replace("i.cpp", "o.cpp") ##+ " - Visual Studio Code"
            full_title = pyautogui.getWindowsWithTitle(window_title)[0].title

            # keystroke = VK_RETURN  # VK_RETURN for Enter key
            # # Find the window handle
            handle = ctypes.windll.user32.FindWindowW(0, full_title)
            if ctypes.windll.user32.IsWindow(handle):
                print("Valid window handle found")
            else:
                print("Invalid window handle")

            # # Send the keystroke
            # ctypes.windll.user32.PostMessageW(handle, WM_KEYDOWN, VK_CONTROL, 0)
            ctypes.windll.user32.PostMessageW(handle, WM_KEYDOWN, VK_I, 0)
            time.sleep(0.1)
            # ctypes.windll.user32.PostMessageW(handle, WM_KEYUP, VK_CONTROL, 0)
            ctypes.windll.user32.PostMessageW(handle, WM_KEYUP, VK_I, 0)

            # handle = pyautogui.getWindowsWithTitle(window_title)[0]
            # print(window)
            # window.activate()
            # time.sleep(10)
            # pyautogui.hotkey('ctrl', 'i')
            # pyautogui.hotkey('ctrl', 'v')
            # pyautogui.press('enter')
            # time.sleep(20)
            # pyautogui.hotkey('ctrl', 'enter')
            # pyautogui.hotkey('ctrl', 's')
            # pyautogui.hotkey('ctrl', 'w')
            print("finish------------------")

if __name__ == "__main__":
    # activate_venv()
    main()
    print(process_id)
exit()
# pyautogui.getWindowsWithProcess(process_id)[0].activate()

import SendKeys

# Specify the window title of the process
window_title = "MyProcess"

# Send the desired keystrokes
SendKeys.SendKeys(window_title + "{ENTER}")