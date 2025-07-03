# Mission Cheat Tool

## Description

A Python automation tool that helps interact with code editors like VS Code for automating tasks. Similar to the Copilot Hack tool, this utility parses special input files and automates interactions with code editors.

## Features

- Automated code generation workflow
- File pattern recognition
- Clipboard integration
- Visual Studio Code automation
- Multiple automation strategies

## Requirements

- Python 3.x
- pyautogui
- pyperclip
- Windows with PowerShell

## Installation

1. Install required packages:

```bash
pip install -r requirements.txt
```

## How to Run

```bash
python main.py
```

or

```bash
python main02.py  # Alternative version with different window handling
```

## Usage

1. Place input files with `.i.cpp` extension containing prompts in the format:

```cpp
/*
 your prompt here
 ##
 */
```

2. Run the script and it will:
   - Read the prompt from input files
   - Open corresponding output files in VS Code
   - Automate the interaction with VS Code
   - Save the generated results

## Notes

- The script uses keyboard automation, so avoid interfering with the keyboard during execution
- Different versions provide alternative window handling methods
