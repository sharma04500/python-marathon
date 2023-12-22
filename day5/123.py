import os

folder = input("Type the folders names with spaces:").split()
    
def check_avail():
    for i in folder:
        try:
            os.listdir(i)
        except FileNotFoundError: None
        return None, print(f"Pls check your input {i}") 

        if i in folder:
            print(os.listdir(i))

check_avail()
