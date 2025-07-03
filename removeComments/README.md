# Code Comment Remover

## Description

A Python utility that removes comments from source code files of various programming languages. It supports both single-line and multi-line comments for over 30 programming languages.

## Features

- Supports over 30 programming languages
- Removes both single-line and multi-line comments
- Preserves code structure
- Command-line interface
- Verbose mode for operation details

## Requirements

No external packages required, uses standard Python libraries:

- re (regular expressions)
- sys
- argparse

## How to Run

```bash
python removeComments.py filename --lang language [-v]
```

### Arguments:

- `filename`: Path to the source code file
- `--lang`: Programming language (e.g., python, java, cpp)
- `-v, --verbose`: Enable verbose output

## Example Usage

```bash
python removeComments.py script.py --lang python
python removeComments.py code.cpp --lang cpp -v
```

## Supported Languages

The script supports many programming languages including:

- Python
- Java
- C/C++
- JavaScript
- HTML/CSS
- Ruby
- PHP
- Perl
- Bash/Shell
- PowerShell
- Swift
- Go
- Rust
- TypeScript
- and many more...
