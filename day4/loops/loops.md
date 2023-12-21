# Loops --->  Need & Usage!!!

The file `loops.py` in this folder contains few sample loops and is executable.
Loops is a common concept found in almost all the programming languages including shell scripts. Loops are used to automate the handling of the tasks which have repeatitive parts. 

For example, consider a hypothetical scenario, where the user should fetch the id's of some 25 instances and modify all the instances to a particular size like t2.large. 

To get this job done in Python without using loops, a user should write a function using variables and execute the function for 25 times by replacing the values everytime or he should write 25 different functions for 25 different resources.

Using loops, onee can get the job done simply using two loops, one while loop to identify the instance id's and pick them and a for loop to modify them through picking the variables from the previous while loop.

In python, we have two major types of loops in Python to serve different use cases and requirements viz.,
* For loops
* While loops.

### *For Loop*
For loops are the loops which are used to execute the action for desired number of times in two ways. They are

1. Specifying the number of times using `range()` parameter

For loops with range() are employed to serve the sitiations where a loop is to be executed for desired number of times irrespective of the conditions or values given as an input.
```
for i in range(10):
    print ("Sharma Akella")

for i in range(100):
    print (i + 1)
```
The snippet in the above clipboard illustrates two for loops using range function. Both of these loops will be executed for 10 and 100 times with respect to the value specified in range function. range(10) means (0,1,2,..,9)

In the above statement `for` is the keyword to trigger a for loop and `i` is the variable which can be written as any value like x or y .... and `in` specifies the list or range being provided as an input.

2. Specifying a list as an input.
For loops can also be executed with a list or tuple instead of range function. In this case, the variable will pick each and every value, replace the value in the statement and executes the loop on all the elements of the list or tuple specified.
```
for x in ("andhra", "telangana"):
    print(f"{x} is a telugu state.")
```
The above loop executes x with both the values and prints the same statement by replacing the variable x in the loop.
Similarly,
```
for y in {"tamil", "telugu", "malayalam", "kannada"}:
    print(f"{y} is a South Indian Language.")
```
The loop executes the variable y with all the 4 strings mentioned in the list and executes the loop for all the elements specified in the list one after the other and gives the output accordingly.

### *while loop*
While loops are the loops which are used to execute a loop through validating a particular condition. While loops will be executed as long as the condition is satisfied and stops the loop when the condition is met.
For example, consider the below loop where i refers to a variable holding value 1; while is the keyword that triggers a while loop and `i <= 5` is the condition which means i should be less than or equal to 5 and `i = i + 1` is the increment written to make sure that the loop is aware of the count. 
If `i = i + 1` is not explicitly specified, the loop will never stop and causes huge load on the server. The condition can be anything with respect to the requirement.
```
i = 1
while i <= 5:
    print(f"The count is {i}.")
    i = i + 1
```

### *Loop Manipulation:*
Loop manipulation is a concept which explains about conditional handling of the the loop execution based on various requirements using `break` and  `continue` statements with `if` conditions along with the loops to stop the loop or skip the execution of loop on a particular value during execution.

### *break:*
Consider a list of ood numbers from 1 to 11 as shown below and if the condition becomes `i==10`, the loop should stop over there immediately. To match such situation the user should write a break statement as follows.
```
odds = [1, 3, 5, 7, 9, 10, 11]
for i in odds:
    if i==10:
      break
    print (i)
```

### *continue:*
Consider a list of fruits with a city in it as shown below and the loop should skip executing on the name of the city and continue with the remaining values, to match such condition, the user should write a continue statement with for loop as illustrated in the below clipboard.
```
fruits = ["apple", "banana", "grape", "hyderabad", "mango", "pineapple"]
for i in fruits:
    if i == "hyderabad":
        continue
    print (f"{i} is a fruit") 
```