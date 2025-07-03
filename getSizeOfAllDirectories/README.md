# Directory Size Analyzer

## Description

A Python utility that calculates and displays the size of all directories or files in a given path, with human-readable size formatting (bytes, KB, MB, GB).

## Features

- Calculates directory and file sizes recursively
- Human-readable size formatting (KB, MB, GB)
- Command-line argument support
- Interactive mode if no path provided

## Requirements

No external packages required, uses standard Python libraries:

- os
- argparse

## How to Run

```bash
python getSizeOfAllDirectories.py [path]
```

If no path is provided, you'll be prompted to enter one.

## Example Usage

```bash
python getSizeOfAllDirectories.py "C:\Users\Documents"
```

## Output

The script will output the size of each directory in the specified path with appropriate units (bytes, KB, MB, GB) based on size.
