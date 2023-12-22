import os

folders = input("Enter the directories to be scanned for the files:").split()

def scan_files():
    for x in folders:
        print(os.listdir(x))