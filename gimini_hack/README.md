# Gemini AI Code Generator

## Description

A Python tool that uses Google's Gemini AI API to generate code solutions based on user input. It can process clipboard content or text files and generate code using a predefined template.

## Features

- Integration with Google Gemini AI API
- Clipboard monitoring for input
- Custom code template support for output
- Real-time code generation

## Requirements

- Python 3.x
- google-generativeai
- pyperclip

## Installation

1. Install required packages:

```bash
pip install -r requirements.txt
```

2. Configure your API key in `keys.py` (already included)

## How to Run

```bash
python main.py
```

## Usage

1. Copy a programming problem description to clipboard
2. The script will detect the clipboard change and send it to Gemini AI
3. Generated code will be printed to the console

## Components

- `main.py`: Main program that handles API integration
- `keys.py`: Stores API credentials
- `getUserInput.py`: Monitors clipboard or files for input
- `promtEngineering.py`: Processes input and formats prompts for the AI
