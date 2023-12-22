import os

folder = input("Type the folders names with spaces:").split()

def checking(x):
        try:
          values = os.listdir(x)
          return None, values
        except FileNotFoundError:
          return None, print(f"check your input {x}")

def main():
    for x in folder:
            values, error = checking(x)
            if values:
                 print(f"The files in {x} are: ", os.listdir(x))
                 for i in values:
                      print(f"The errorMessage for {x}:", error)

main()
