# Illegal Filename Fixer

## Description

A Python utility that detects and renames files with illegal characters in their names. This helps solve problems with files that have characters not allowed by the operating system.

## Features

- Recursive directory scanning
- Interactive file renaming
- Options to skip problematic files
- Automatic illegal character filtering
- Preserves file extensions

## Requirements

No external packages required, uses standard Python libraries:

- os
- re (regular expressions)
- argparse

## How to Run

```bash
python rmillegalname.py directory_path
```

## Example Usage

```bash
python rmillegalname.py "C:\Users\Documents"
```

## Interaction

The script will:

1. Find files with illegal characters in their names
2. For each file, prompt with options:
   - Press Enter: Auto-filter illegal characters
   - Enter new name: Rename to provided input
   - Enter "skip": Skip the current file

## Illegal Characters

This script detects and handles characters that are typically not allowed in filenames:

- < (less than)
- > (greater than)
- : (colon)
- " (double quote)
- / (forward slash)
- \ (backslash)
- | (vertical bar)
- ? (question mark)
- - (asterisk)
