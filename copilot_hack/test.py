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

process_id=subprocess.run([ps,"code","-n", "o.cpp"])

pyperclip.copy("text to paste")

time.sleep(10)
print("10 sec")
# pyautogui.hotkey('win', 'down')
# pyautogui.hotkey('win', 'down')

time.sleep(5)

import ctypes

# Virtual-Key Codes
VK_CONTROL = 0x11
VK_RETURN = 0x0D
VK_I = 0x49

# Windows Messages
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
# VK_V virtual code
VK_V= 0x56
keystroke = VK_CONTROL
keystroke2 = VK_V


window = pyautogui.getWindowsWithTitle("o.cpp")[0]
# Find the window handle
handle = ctypes.windll.user32.FindWindowW(0, window.title)

# Send the Ctrl+V keystroke
if handle != 0:
    ctypes.windll.user32.PostMessageW(handle, WM_KEYDOWN, keystroke, 0)
    time.sleep(0.1)
    ctypes.windll.user32.PostMessageW(handle, WM_KEYDOWN, keystroke2, 0)
    time.sleep(0.1)
    ctypes.windll.user32.PostMessageW(handle, WM_KEYUP, keystroke2, 0)
    time.sleep(0.1)
    ctypes.windll.user32.PostMessageW(handle, WM_KEYUP, keystroke, 0)
    print(f"Sent Ctrl+V to '{window.title}'")
else:
    print(f"Couldn't find window '{window.title}'")




# pyautogui.hotkey('ctrl', 'i')
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.press('enter')
# time.sleep(20)
# pyautogui.hotkey('ctrl', 'enter')
# pyautogui.hotkey('ctrl', 's')
# pyautogui.hotkey('ctrl', 'w')