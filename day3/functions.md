# Functions  --> Need and Usage

Functions are the piece of the code which are called as a replacement a particualar piece of code. Though it might not be appropriate to mention this way, In simple words, "function is a variable for a piece of code".
In python, we'll define a function using the keyword `def` followed by the name for the function and (). We can write anything as a name for a function. 
Though the intrepretor reads all the functions, they are not executed if they aren't invoked explicitly.

Consider the below example:
```
a = 5
b = 10

def addition():
    add = a + b
    print(add)
```
In this case, even after specififying the function *addition*, we won't get any output upon executing this piece of code, as we didn't call for the function. It works only if we invoke the function explicitly as shown below:

```
a = 5
b = 10

def sum():
    sum = a + b
    print(sum)

sum()
```
Syntax to define a function ---> def <name>():
Syntax to invoke or call the function ---> <name>()

The name we're using for a function must be unique throughout the code i.e., name duplication for multiple functions is not a good practice. 
If we name two functions with the same string and explicitly invoke for the function at some point of the code, the system will execute both the functions and will give the output of the last function, irrespective of the desired one as system can't understand the users mental interpretation.

Consider the below example. In this case, A function named addition was intentionally specified for twice and called for twice. Irrespective of the number of times we call for the function, the system will generate the output by using the function specified just above the call.
```
a = 10
b = 15
c = 20

def addition():
    add = a + b
    print("sum:", add)

def addition():
    sub = a - b
    print("sub:", sub)

def multiply():
    mul = a * b
    print("mul:", mul)

def division():
    div = a / b
    print("div:",div)

addition()
addition()
multiply()
division()
```
Consider the below case. In this case, the function addition() was specified and immediately invoked. Later, The same string addition() was used to define the subtraction function and was called twice at the bottom of the script. In this case, the generated response will be according to the definition which is just above the call.

```
a = 10
b = 15
c = 20

def addition():
    add = a + b
    print("sum:", add)

addition()   # prints the answer for a + b

def addition():
    sub = a - b
    print("sub:", sub)

def multiply():
    mul = a * b
    print("mul:", mul)

def division():
    div = a / b
    print("div:",div)

addition()  # prints the answer for a - b
addition()  # prints the answer for a - b
multiply()
division()
```

In general, the series of actions performed by any function are:
* Take the Input
* Perform  the logic and
* Return the output.