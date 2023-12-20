import existing as basic    # Importing file1 as a module with alias 'basic'.

print(basic.multiply(5500, 10)) # Calling the multiply function from basic i.e., file1 replacing 5500 and 10 with a and b respectively.

print(basic.multiply(5500, 10), basic.addition(10, 30)) # Calling multiple functions in a single statement.


from existing import multiply
print(multiply(100, 20))

from existing import addition
print(addition(10, 30))

from existing import division as fun1
print(fun1(10, 2))

from existing import subtraction as fun2
print(fun2(15, 5))


from existing import *      # to import all the functions using from statement.
print(multiply(2, 5000))