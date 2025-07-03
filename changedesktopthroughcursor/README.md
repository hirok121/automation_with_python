# Desktop Changer - Cursor-Based Virtual Desktop Switcher

## Description

This script automatically switches between Windows virtual desktops by detecting mouse cursor position at screen edges. It provides a seamless way to navigate between virtual desktops without keyboard shortcuts.

## Features

- Automatic desktop switching when mouse reaches screen edges
- Left edge detection for switching to previous desktop
- Right edge detection for switching to next desktop
- Configurable edge buffer zone
- Anti-rapid switching with cooldown period
- Background execution via batch file

## Requirements

- Python 3.x
- pyautogui
- keyboard
- Windows 10/11 with Virtual Desktops enabled

## Installation

1. Install required packages:

```bash
pip install -r requirements.txt
```

## How to Run

### Method 1: Direct Python execution

```bash
python desktopChange.py
```

### Method 2: Background execution (Recommended)

```bash
desktopChange.bat
```

or double-click the `desktopChange.bat` file

### Method 3: Using the shortcut

Double-click the `desktopChange.bat - Shortcut.lnk` file

## Usage

1. Run the script using any of the above methods
2. The script will run continuously in the background
3. Move your mouse to the left edge of the screen to switch to the previous virtual desktop
4. Move your mouse to the right edge of the screen to switch to the next virtual desktop
5. The script detects edge contact in the middle 60% of screen height (20%-80%)

## Configuration

- **Edge buffer**: 10 pixels from screen edge (configurable in code)
- **Cooldown period**: 1.5 seconds to prevent rapid switching
- **Detection zone**: Middle 60% of screen height

## Notes

- The script runs indefinitely until manually stopped
- Uses Windows keyboard shortcuts (Ctrl+Win+Left/Right) for desktop switching
- The batch file runs the script in background mode (pythonw) for silent operation
- To stop the script, use Task Manager or Ctrl+C in the terminal window
