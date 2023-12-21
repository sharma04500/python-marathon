for i in range(25):
    print(i)

for i in range(10):
    print ("Sharma Akella")

for i in [2, 10, 15, 150, 69, 420]:
    print(i ** 100)

for x in ("andhra", "telangana"):
    print(f"{x} is a telugu state.")

for y in {"tamil", "telugu", "malayalam", "kannada"}:
    print(f"{y} is a South Indian Language.")

i = 1
while i <= 5:
    print(f"The count is {i}.")
    i = i + 1

even = [1, 3, 5, 7, 9, 10, 11]
for i in even:
    if i==10:
      break 
    print (i)

fruits = ["apple", "banana", "grape", "hyderabad", "mango", "pineapple"]
for i in fruits:
    if i == "hyderabad":
        continue
    print (f"{i} is a fruit") 