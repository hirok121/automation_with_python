# GitHub Copilot Automation Tool

## Description

A Python utility that automates interaction with GitHub Copilot for code generation. It reads input files with prompts and automatically uses Copilot to generate solutions.

## Features

- Automated file processing
- Clipboard integration
- Pattern recognition for special prompts
- Visual Studio Code integration
- Keyboard shortcut automation

## Requirements

- Python 3.x
- pyautogui
- pyperclip
- Visual Studio Code

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

1. Place input files with `.i.cpp` extension containing prompts
2. The script will:
   - Read the prompt from the input file
   - Open a corresponding output file in VS Code
   - Trigger Copilot interaction
   - Save the generated code

## Input Format

Input files should follow this format:

```cpp
/*
 your prompt here
 ##
 */
```

## Notes

- The script uses keyboard automation, so avoid interfering with the keyboard during execution
- Different versions are provided for Windows and Linux operating systems
