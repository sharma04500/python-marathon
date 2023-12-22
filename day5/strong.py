import os

def checking(x):
        try:
          values = os.listdir(x)
          return values, None
        except FileNotFoundError:
          return None, print(f"check your input for {x}")

def main():
    folder = input("Type the folders names with spaces:").split()

    for x in folder:
            values, error_message = checking(x)
            if values:
                print(f"The files in {x} are:", values)

main()

# Comments:
# Line 6: The placement of None is imp here. If None is return first no input will be provided and every output is treated as an error.
# The checking() function is invoked by the for loop in the main() function for every element of the list folder.