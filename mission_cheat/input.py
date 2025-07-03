
pattern = "main.py - Visual Studio Code"


import ctypes

# Define the window title
window_title = "main.py - mission_cheat - HirokPersonal - Visual Studio Code"
window_title="Visual Studio Code"

# Find the window handle
handle = ctypes.windll.user32.FindWindowW(0, window_title)

# Check if the window was found
if handle != 0:
    print(f"Window '{window_title}' found with handle {handle}")
else:
    print(f"Window '{window_title}' not found")
