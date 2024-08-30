# check any of the running process in background

import os
import psutil
import argparse

def check_process_running(process_name):
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def main(directory_to_scan):
    if not os.path.isdir(directory_to_scan):
        print("Invalid directory path")
        return

    file_scaned=0
    running_process_found=0
    result = []

    for root, _, files in os.walk(directory_to_scan):
        for file in files:
            if file.endswith('.exe'):
                file_scaned+=1
                print(f"Checking {file} for running process")
                file_path = os.path.join(root, file)
                if check_process_running(file.split('.')[0]):
                    print(f"Running process found in BG : {file_path}")
                    result.append(file_path)
                    running_process_found+=1
                else:
                    print(f"No running process found in BG : {file_path}")
    
    print("\n")
    print("Summary")
    print("-------")
    print(f"Total files scanned: {file_scaned}")
    print(f"Total running process found in BG: {running_process_found}")
    print("\n")
    print("Details")
    print("-------")
    for i, res in enumerate(result):
        print(f"{i+1}. {res}")
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="check any of the running process in background")
    parser.add_argument('directory', nargs='?', default=None, help='Directory to scan for running process')
    args = parser.parse_args()

    if args.directory is None:
        directory_to_scan = input("Enter the directory path to scan for Running Process: ")
    else:
        directory_to_scan = args.directory
    
    main(directory_to_scan)
    
