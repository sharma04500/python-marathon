# Modules

Modules are the reuseable piece of code i.e., if we write or declare a function in any of the files we have written till date, we can simply call for that function through importing the file as a module into the current code. 

For importing the pre-existing code as a module into current py file, Use the keyword `import` followed by the path to the file.

The syntax to import a file name named `existing.py` as a module into the current file named `latest.py` with `basic` as an alias is illustrated below. To call for the execution of the module, simply type the name of the module as illustrated in the third line of the below clipboard. In place of `existing` in the below clipboard write the path to your existing python file without extension.

#### *import*

```
import existing as basic

basic
```
The first line of the above clipboard imports entire module with alias `basic` and if we call for the module using the alias basic, the entire module gets executed in this program. This is the fundamental and raw example for usage of modules in python.

#### *from*

Instead of importing an entire module, one can explicitly specify a particular function of the module and import only that particular function using `from` statement as illustrated in the clipboard below. 
Though importing a particular function alone from the module might seem to be a small resource saving act in these practise versions, this feature has incredible resource saving capability in case of importing a particular function from a practical real-time module containinng 10000 lines and 1000 unique functions.

In the below clipboard, the from statement will import only `multiply` function from the module `existing`.
Second line is to print the multiply statement by replacing a with 100 and b with 20.
```
from existing import multiply

print(multiply(100, 20))
```

If we have a requirement of importing all the functions from a module, we can simply use the following line:
`from existing import *`
This imports all the functions from the module individually and is not a recommended approach as we cannot specify a single alias for multiple unique functions. So, using `import existing as basic` is the best practice to match such requirement. As we can write a simple alias for the entire module.

#### *Alias*

Aliasing plays a crucial part in case of practical scenarios where a module is imported from somewhere and is to be specified in multiple parts of the code we are writing. 

While writing a code, the best practice is to specify an alias for the module while importing and specify the alias everywhere instead of writing the name of the module directly.
This approach gives the flexibility to handle the code easily in case of modifying the name of the module with respect to any future requirements. 
In such case, alias will be coded at multiple spots and upgrading the title of the module in `from` or `import` statement alone makes the code ready as per the new standard, as we've alias coded everywhere in place of the module name and the alias is now pointing towards the new name. 
The below snippet illustrates aliasing the module fetched using import statement.
>In this case, first line indicates writing an alias for module and the remaining two illustrates the usage of alias for invoking the functions from the imported module using alias.
```
import existing as basic    
print(basic.multiply(5500, 10))     
print(basic.multiply(5500, 10), basic.addition(10, 30))
```

The below snippet illustrates aliasing a particular function imported from a module using from statement.
```
from existing import division as fun1
print(fun1(10, 2))

from existing import subtraction as fun2
print(fun2(15, 5))
```

In this case, if we are importing multiple functions, we can't give a single alias to all the functions as they are being imported as multiple unique functions in a single statement instead of being imported as a single module.
For example, we can't write an alias for the statement `from existing import *`