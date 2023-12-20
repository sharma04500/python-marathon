import sys

a = float(sys.argv[1])
sign = sys.argv[2]
b = float(sys.argv[3])

def addition(a, b):
    add = a + b
    return add

def subtraction(a, b):
    sub = a - b
    return sub

def multiply(a, b):
    mul = a * b
    return mul

def division(a, b):
    div = a / b
    return div

if sign == "add":
    print(addition(a, b))

if sign == "sub":
    print(subtraction(a, b))

if sign == "mul":
    print(multiply(a, b))

if sign == "div":
    print(division(a, b))