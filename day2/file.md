# Keywords & Variables -->  Need & Usage

#### *keywords:*

Each and every programming language will follow it's own principals and keywords for performing various tags using various logics through understanding the statements, which are determined by the user as explicit functions or individual tasks using various approaches. 

While declaring or triggering different functions in various parts of the code, the user may write various conditions, statements, functions and cases, which is end of the day given as an input to the interpretor, which will parse the code and process it to deliver the output in one way or the other. So, the code which was being written, in this case should be the medium of communication in between the user and the system, which is going to parse and process the code. In order to provision proper functionality, ease of access and useability to various users from different parts of the world with various levels of proficiency, each and every action is defined by a globally useable keyword for all the possible actions, which means various different **keywords** to declare various functions, conditions, operations etc to suit various purposes.

Keywords are predefined in nature and the major thumb rule to follow while using them is they should be used exactly as they were specified ie., the case sensitivity, syntax and use case should match the exact definition of that particular keyword. Any improper usage will result in errors alongside making the words inexecutable. Keywords is a group name which indicates all the possibilities of any programming language covering all the words from the language which had significant and unique use case across various concepts like loops, conditions, functions etc.

Few commonly used keywords in Python are:

*The below mentioned keywords info is extracted from https://github.com/sharma04500/python-abhishek.git only for illustration purpose with no intention of plagarism as I have just started with python and not well verse to list all the keywords and use case.*

1. **and**: It is a logical operator that returns `True` if both operands are true.

2. **or**: It is a logical operator that returns `True` if at least one of the operands is true.

3. **not**: It is a logical operator that returns the opposite of the operand's truth value.

4. **if**: It is used to start a conditional statement and is followed by a condition that determines whether the code block is executed.

5. **else**: It is used in conjunction with `if` to define an alternative code block to execute when the `if` condition is `False`.

6. **elif**: Short for "else if," it is used to check additional conditions after an `if` statement and is used in combination with `if` and `else`.

7. **while**: It is used to create a loop that repeatedly executes a block of code as long as a specified condition is true.

8. **for**: It is used to create a loop that iterates over a sequence (such as a list, tuple, or string) and executes a block of code for each item in the sequence.

9. **in**: Used with `for`, it checks if a value is present in a sequence.

10. **try**: It is the beginning of a block of code that is subject to exception handling. It is followed by `except` to catch and handle exceptions.

11. **except**: Used with `try`, it defines a block of code to execute when an exception is raised in the corresponding `try` block.

12. **finally**: Used with `try`, it defines a block of code that is always executed, whether an exception is raised or not.

13. **def**: It is used to define a function in Python.

14. **return**: It is used within a function to specify the value that the function should return.

15. **class**: It is used to define a class, which is a blueprint for creating objects in object-oriented programming.

16. **import**: It is used to import modules or libraries to access their functions, classes, or variables.

17. **from**: Used with `import` to specify which specific components from a module should be imported.

18. **as**: Used with `import` to create an alias for a module, making it easier to reference in the code.

19. **True**: It represents a boolean value for "true."

20. **False**: It represents a boolean value for "false."

21. **None**: It represents a special null value or absence of value.

22. **is**: It is used for identity comparison, checking if two variables refer to the same object in memory.

23. **lambda**: It is used to create small, anonymous functions (lambda functions).

24. **with**: It is used for context management, ensuring that certain operations are performed before and after a block of code.

25. **global**: It is used to declare a global variable within a function's scope.

26. **nonlocal**: It is used to declare a variable as nonlocal, which allows modifying a variable in an enclosing (but non-global) scope.

*End of the data extracted from python-abhishek.git.*

#### *variables:*

Variables are used in most of the applications where code or script or in any other manifest which is scripted following a requirement with respect to a particular environment. For instance, variables are also used in shell scripting, terraform configuration files, ansible playbooks, jenkins pipelines and in many more cases to provision the ease in usage alongside enhancement of modularity or re-useablity of the code to suit various requirements.

For example, in case of the sample code mentioned below a, b and c are declared at the begining of the code and instead of directly hardcoding the value everywhere, we have used a,b and c with respect to the placement of the corresponding value. In case of new usgae viz., using the same code for a different set of values, we can simply chance a,b and c from 15, 25 and 30 to 100,150,30 respectively and perform the functions following the variables i.e., add, sub, mul, div and rem on the new values instead of writing a new script from scratch.

```
a = 15
b = 25
c = 30

add = a + b + c
sub = a - b - c
mul = a * b * c
div = a / b / c
rem = a // b // c

print ("sum:", add)
print("diff:", sub)
print("product:", mul)
print("division:", div)
print("remainder:", rem)
```

The advantanges that implementation of variables bring into picture are:
* Modularity or reuseability,
* trims down the length of the script,
* Provisions ease in readability,
* Simplifies the process of debugging and troubleshooting,
* Restricted scope with respect to the placement of the variables,
* Enables dynamic programming ie., allows the user to easily reuse the script with new values everytime.