print ("Hello, world!")

arn = "arn:aws:iam::123456789012:user/johndoe"

print (arn.split("/"))

print ( arn.split("/")[1] )

print( arn.split("/")[1].upper())

print(arn.split("/")[1].upper().lower())

one = "Hello"
two = arn.split("/")[1].upper()

result = one + " " + two

print (result)

print ("Username :",two)

print (len(arn))

print ("Extract Username from" + arn,"The answer is:"+ two,"The length of string is:", len(arn))

spaced = "   Observe the spaces bro   "

stripped = spaced.strip()

print("Stripped text:", stripped+".")

# Numbers: 
# integers:
num1 = 10
num2 = 15

# Integer division:
ans = num1 // num2
print (ans)

# Divide integers and print the remainder

ans1 = num1 % num2
print (ans1)

# Absolute Values

ans2 = abs(-15)
print(ans2)

num3 = 15.5
num4 = 0.5

# Addition:
add = num3 + num4
print (add)


# Subtraction:
sub = num3 - num4
print (sub)


# Multiplication:
mul = num3 * num4
print (mul)

# Division:
div = num3 / num4
print (div)


# Round function

dec = 3.21654641343512354
val = round(dec, 3)
print (val)