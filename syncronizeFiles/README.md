# File Synchronizer

## Description

A Python utility for synchronizing files between source and destination directories with various options for control.

## Features

- File and directory copying
- Recursive directory synchronization
- Optional file overriding control
- Backup option for destination files
- Verbose mode for detailed operation logs

## Requirements

No external packages required, uses standard Python libraries:

- os
- shutil
- argparse

## Installation

No installation required beyond Python itself.

## How to Run

```bash
python syncronizeFiles.py source_dir destination_dir [options]
```

### Options:

- `-v, --verbose`: Enable verbose mode for detailed logs
- `-o, --override`: Override files in destination directory
- `-r, --recursive`: Copy files recursively
- `-b, --backup`: Backup destination directory before copying

## Example Usage

```bash
# Basic usage
python syncronizeFiles.py "C:\source" "D:\destination"

# Recursive copy with backup
python syncronizeFiles.py "C:\source" "D:\destination" -r -b

# Verbose mode with override
python syncronizeFiles.py "C:\source" "D:\destination" -v -o
```
