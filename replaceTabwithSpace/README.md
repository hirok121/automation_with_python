# Tab to Space Converter

## Description

A simple Python utility that replaces tab characters with spaces in text files. This is useful for standardizing code formatting and indentation.

## Features

- Processes multiple files in a single run
- Replaces all tab characters with 4 spaces (configurable in code)
- Command-line interface for file paths

## Requirements

No external packages required, uses standard Python libraries.

## How to Run

```bash
python replaceTabwithSpace.py file1.txt file2.py [file3...]
```

## Example Usage

```bash
python replaceTabwithSpace.py code.py document.txt
```

## Notes

- By default, each tab is replaced with 4 spaces
- The script modifies files in place
- Multiple files can be processed in a single command
