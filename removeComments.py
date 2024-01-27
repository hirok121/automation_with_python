import sys
import argparse
import re

comment_chars = {
        'python': {
            'single': '#',
            'multi': ('"""', '"""')
        },
        'java': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'c': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'cpp': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'javascript': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'html': {
            'single': '<!--',
            'multi': ('<!--', '-->')
        },
        'css': {
            'single': '/*',
            'multi': ('/*', '*/')
        },
        'ruby': {
            'single': '#',
            'multi': ('=begin', '=end')
        },
        'php': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'perl': {
            'single': '#',
            'multi': ('=begin', '=cut')
        },
        'bash': {
            'single': '#',
            'multi': (': <<\'', '\'\n')
        },
        'powershell': {
            'single': '#',
            'multi': ('<#', '#>')
        },
        'swift': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'go': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'rust': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'typescript': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'kotlin': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'scala': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'r': {
            'single': '#',
            'multi': ('/*', '*/')
        },
        'lua': {
            'single': '--',
            'multi': ('--[[', ']]')
        },
        'matlab': {
            'single': '%',
            'multi': ('%{', '%}')
        },
        'groovy': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'haskell': {
            'single': '--',
            'multi': ('{-', '-}')
        },
        'objective-c': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'shell': {
            'single': '#',
            'multi': (': <<\'', '\'\n')
        },
        'sql': {
            'single': '--',
            'multi': ('/*', '*/')
        },
        'perl6': {
            'single': '#',
            'multi': ('=begin', '=end')
        },
        'elixir': {
            'single': '#',
            'multi': ('=begin', '=end')
        },
        'clojure': {
            'single': ';;',
            'multi': ('#_', '\n')
        },
        'dart': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'fortran': {
            'single': '!',
            'multi': ('/*', '*/')
        },
        'julia': {
            'single': '#',
            'multi': ('#=', '=#')
        },
        'ocaml': {
            'single': '(*',
            'multi': ('(*', '*)')
        },
        'pascal': {
            'single': '//',
            'multi': ('(*', '*)')
        },
        'prolog': {
            'single': '%',
            'multi': ('/*', '*/')
        },
        'scheme': {
            'single': ';;',
            'multi': ('#|', '|#')
        },
        'vb': {
            'single': "'",
            'multi': ("'comment", "'")
        },
        'vbscript': {
            'single': "'",
            'multi': ("'comment", "'")
        },
        'verilog': {
            'single': '//',
            'multi': ('/*', '*/')
        },
        'vhdl': {
            'single': '--',
            'multi': ('/*', '*/')
        },
        'xml': {
            'single': '<!--',
            'multi': ('<!--', '-->')
        },
        'yaml': {
            'single': '#',
            'multi': ('#', '\n')
        }
    }

verbose = []

parser = argparse.ArgumentParser(description='Script description')
parser.add_argument('filename', type=str, help='Files to remove comments from')
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
parser.add_argument('--lang', help='Specify language')

args = parser.parse_args()


def removeComments():
    path=args.filename
    lang=args.lang
    counter = 0
    comment_char1,comment_char2= comment_chars[lang]["multi"]
    comment_char1=comment_char1.replace("/","\\/").replace("*","\\*")
    comment_char2=comment_char2.replace("/","\\/").replace("*","\\*")
    comment_charsingle=comment_chars[lang]["single"]
    lines = []
    with open(path, 'r') as file:
        lines = file.readlines()

    # remove single line comments
    for line in lines:
        if line.strip().startswith(comment_charsingle):
            lines.remove(line)
            counter += 1
    verbose.append(f'Removed {counter} single line comments')
    # remove multi line comments
    contents="".join(lines)
    pattern = r"{}[\s\S]*{}".format(comment_char1,comment_char2)
    contents=re.sub(pattern, "", contents, flags=re.DOTALL)
    with open(path, 'w') as file:
        file.write(contents)


if args.lang:
    verbose.append(f'Specified language: {args.lang}')
    removeComments()
        
if args.verbose:
    for line in verbose:
        print(line)