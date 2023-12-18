# Integers & Float Data Types --> Usage and Functions

### Integers
Any number containing any number of digits without any decimal values or spaces or special charecters in between are usually called as integers.
There are few functions available for integers.

#### *Division*

In order to perform a division and print the answer. Use // to perform the operation as illustrated below:

```
num1 = 25
num2 = 5

ans = num1 // num2
print (ans)
```
The above example divides 25 by 5 and prints the answer. Similarly, In order to get the remainer of the division,
```
num1 = 20
num2 = 3

ans1 = num1 % num2
print (ans1)
```
If we have any negative integer, we can get the absolute value or positive of that value using abs function.
```
ans2 = abs(-15)
print (ans2)
```

### Float Values

Any number which is written along with it's decimals is usually termed as a Float value. There are few functions available for float values.

For example,
```
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
```

If we have any complex float value with many decimals, round function will round off the decimal to desired size as illustrated below.

```
dec = 3.21654641343512354
val = round(dec, 3)
print (val)
```
In the above example, round is the function dec is the variable holding given value and 3 indicates 3 digits after . This prints 3.216 as output.