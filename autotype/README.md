# AutoType - Automated Text Typing Tool

## Description

AutoType is a Python automation script that automatically types text from an input file. It's useful for quickly typing large amounts of text, code snippets, or repetitive content using keyboard shortcuts.

## Features

- Hotkey-triggered auto-typing (Shift + Ctrl + Alt + H)
- Emergency stop functionality (Shift + Ctrl + Alt + S or move mouse to top-left corner)
- Configurable typing speed
- Reads text from input.txt file
- Safe-stop mechanisms to prevent runaway typing

## Requirements

- Python 3.x
- keyboard
- pyautogui

## Installation

1. Install required packages:

```bash
pip install -r requirements.txt
```

## How to Run

1. Place the text you want to auto-type in `input.txt`
2. Run the script:

```bash
python autotype.py
```

3. Use hotkeys to control the typing:
   - **Start typing**: Shift + Ctrl + Alt + H
   - **Stop typing**: Shift + Ctrl + Alt + S
   - **Emergency stop**: Move mouse to top-left corner
   - **Exit program**: Ctrl + C

## Usage Example

1. Edit `input.txt` with your desired text
2. Run the script
3. Position your cursor where you want the text to appear
4. Press Shift + Ctrl + Alt + H to start auto-typing

## Notes

- The script includes a 2-second delay after triggering to allow cursor positioning
- Typing speed can be adjusted by modifying the `interval` parameter in the code
- Emergency stop feature helps prevent accidental text insertion
