# Environment Variables from the *env* of the OS *(host machine)*.

In general shell scripts, One can store the environment variables in the env of the Operating System and call them from there whenever required.
Similarly, Python comes with the capability of reading those environment variables. It uses another module called `OS` for getting this job done. 
User should import the `os` module, which needs no installation like `sys` to use this built-in functionality.
In the below clipboard snippet, first line illustrates importing the os module and the remaining shows the usage.
```
import os
os.getenv("<env_name>")

#example:

print(os.getenv("password"))
print(os.getenv("username"))
print(os.getenv("author"))
```
In the above statement `password`,`username`, `author` should be stored as environment variables before executing this code.