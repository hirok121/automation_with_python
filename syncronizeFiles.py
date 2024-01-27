#!/usr/bin/env python3

import os
import shutil
import argparse

verbose = []

parser = argparse.ArgumentParser(description='Script description')
parser.add_argument('src', type=str, help='Source directory from where to copy files')
parser.add_argument('dest', type=str, help='Destination directory to where to copy files')
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
parser.add_argument('-o','--override', action='store_true',default=False,help='If set, override files in destination directory')
parser.add_argument('-r','--recursive', action='store_true',default=False,help='if set, copy files recursively')
parser.add_argument('-b','--backup', action='store_true',default=False,help='if set, backup files in destination directory')

args = parser.parse_args()

verbose.append(args)
filescounter = 0
folderscounter = 0

def sync_files(src_dir, dest_dir, recursive=False, override=False,backup=False):

    # def sync_files(src_dir, dest_dir, recursive=False):
    """
    Synchronize files from a source directory to a destination directory.

    Parameters:
    src_dir (str): The source directory.
    dest_dir (str): The destination directory.
    recursive (bool, optional): Whether to copy files recursively. Defaults to False.
    override (bool, optional): Whether to override files in destination directory. Defaults to False.
    backup (bool, optional): Whether to backup files in destination directory. Defaults to False.
    Returns:
    None
    """
    # Function body...  

    global folderscounter
    global filescounter
    # create back up of files
    if backup:
            shutil.copytree(dest_dir,dest_dir+".backup",dirs_exist_ok=True)
            verbose.append(f'Created backup of {dest_dir} in {dest_dir}.backup')
    if recursive:
        # Walk through src_dir
        for dirpath, dirnames, filenames in os.walk(src_dir):
            # Create corresponding directories in dest_dir
            dest_path = os.path.join(dest_dir, os.path.relpath(dirpath, src_dir))
            os.makedirs(dest_path, exist_ok=True)
            folderscounter += 1

            # Copy files
            for filename in filenames:
                src_file = os.path.join(dirpath, filename)
                dest_file = os.path.join(dest_path, filename)
                if not os.path.isfile(dest_file) or override:
                    shutil.copy2(src_file, dest_file)
                    filescounter += 1
    else:
        # Copy files in the root of src_dir only
        for filename in os.listdir(src_dir):
            src_f = os.path.join(src_dir, filename)
            dest_f = os.path.join(dest_dir, filename)
            if os.path.isdir(src_f):
                os.makedirs(dest_f, exist_ok=True)
                folderscounter += 1
            else:
                if not os.path.isfile(dest_f) or override:
                    shutil.copy2(src_f, dest_f)
                    filescounter += 1

if __name__ == "__main__":

    sync_files(src_dir=args.src, dest_dir=args.dest, recursive=args.recursive, override=args.override,backup=args.backup)
    verbose.append(f'Copied {filescounter} files and {folderscounter} folders')

    if args.verbose:
        for line in verbose:
            print(line)


