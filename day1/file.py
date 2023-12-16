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