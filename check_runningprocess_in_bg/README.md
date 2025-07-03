# Process Scanner - Background Process Detector

## Description

A Python utility that scans directories for executable files (.exe) and checks if they are currently running in the background as active processes.

## Features

- Recursive directory scanning
- Automatic process detection
- Summary reporting with counts and details
- Command-line argument support

## Requirements

- Python 3.x
- psutil

## Installation

1. Install required packages:

```bash
pip install -r requirements.txt
```

## How to Run

```bash
python check_runningprocess_in_bg.py [directory_path]
```

If no directory path is provided, you'll be prompted to enter one.

## Example Usage

```bash
python check_runningprocess_in_bg.py "C:\Program Files"
```

## Output

The script will output:

1. Scanning progress information
2. A summary with total files scanned and processes found
3. Detailed list of running processes found in background
