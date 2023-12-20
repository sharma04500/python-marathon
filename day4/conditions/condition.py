import sys

type = sys.argv[1]

if type == "t2.micro":
    print("Your instance can be successfully created...")
else:
    print(f"Sorry!! We are in free tier and {type} is chargeable")

# To call variables in a print statement, put the var in flower braces {} and type "f" before
# the string as illustrated in the print statement for else.
    

if type == "t2.micro":
    print("You're in free tier and enjoy t2.micro for 750 hrs/month.")
elif type == "t2.medium":
    print("We can accomodate t2.medium, go for approval.")
elif type == "t2.large":
    print("Buddy!!! Our budgets are tight!!! Please try to use On-prem")
else:
    print(f"Sorry!! {type} is completely out of Budget. Plz optimize :-)")