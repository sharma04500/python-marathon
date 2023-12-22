import os

folders = input("Enter the directories to be scanned for the files:").split()

def scan_files():
    for x in folders:
        print(f"The files present in {x}:", os.listdir(x))

scan_files()