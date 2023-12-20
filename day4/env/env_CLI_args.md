# Environment Variables *(env)*

### *Passing env as Command Line Arguments*

Using python, We can pass the environment variables as strings from command line arguments. But the script cant't directly read the environment variables unlike shell scripts.

In case of python, we have an in-built and readily module for reading the env from CLI args named `sys`.
Though sys need not be installed through pip for using in our program, we have to import the module and write logic to read the env from the command line arguments.
In the below clipboard snippet, the first line shows importing the `sys` module into file and the next lines show the syntax to be followed in order to pick the env from the CLI args properly.
`sys.argv[n]` should be used to indicate the index of the argument to be taken, where *n=1,2,3,...,n*.

```
import sys
a = sys.argv[1]
sign = sys.argv[2]
b = sys.argv[3]
```
If the file named `file.py` is containing the above snippet as illustrated in the file.py of this folder, the CLI command to be passed is `python <file.py> <a> <sign> <b>`.
`python file.py 15 add 20` is an example.

*NOTE: By default sys.argv[n] will read the data provided in the CLI as strings only. So, To match the data type in case of giving data of any other format as input from the CLI, please indicate the data type as shown below.*

For example, let us consider the scenario, where env a,b are numbers and *add* (string) is the sign in between them. In this case, write the `sys.argv[n]` as `float(sys.argv[n])` or `int(sys.argv[n])`. To know more about the data types float and int, refer to `day1/numbers.md` of this repository.