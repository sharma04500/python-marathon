# Lists --> Need and Usage!!!
To understand the necessity of loops, Lets look at a requirement, where we have the names of 100 Ec2 instances and 50 s3 buckets and we have to add a particular tag to all of those poor things!!!
In this case, if we fetch the list of all the objects and apply a simple loop, that loop can add a tag to all the resources.

### *List*
`List` is a powerful data type which had the potential to store multiple values to a single variable.
Python treats any specified list as a list of various elements irrespective of the data type of individual data type and hence, lists are said to be `heterogenous in nature`. 
For example, the list in the below mentioned clipboard snippet consists of values which are of different data types and python allows the user to use one such list.

```
example_list = ["raju", "booju", 69, 420, "kaju", "icefruit"]
```  
### *list.append()*
Lists allow the user to modify them at point of time in the program through various functions and are said to be `dynamic and mutable` in nature.

User can append new entries to the list at any point of time using the function `<var_name>.append(<value>)`. For example consider the above list, `example.append("sunny")` adds the string "sunny" as a new element to the list.

```
example_list = ["raju", "booju", 69, 420, "kaju", "icefruit"]
example.append("sunny")
print("example_list")
print(len("example_list"))
```
There's an another function called `len("example_list")` as mentioned above, which gives the length of the list, i.e., the number of elements present in the list.

### *Indexing the elements*
The indexing of elements in the list starts from 0 i.e., we have to specify the position of a particular element of a list by starting the count from 0 not 1. The index positions of the elements of a list will be [0, 1, 2,3,..,n].

For example, the index of the string "kaju" in the above mentioned example_list will be 4 as it's in the fifth position and the string "raju" acquires zeroth position.

Newly added element "sunny" will hold the 6th position as it will be the 7th entry into the list.

Python will have no memory restrictions while storing the list.

To call a particular element from the list, we should use the index position of that element in that list.

Considering the above example_list, `example_list[0]` represents the first element i.e., raju and `example_list[3]` indicates the fourth element of the list ie., 420.

### *Removing elements*
Users can also remove the elements from the list at any point of time in the entire program with respect to the requirements using the function `<list_name>.remove("<element>")`.
Considering the above example,`example_list.remove("raju")` will remove the string raju from the above list and a print function then executed will show the exclusion of this string.
Similarly, the fifth line of the below clipboard will remove the element "booju" from the list and following print statement will show the updated data.
```
example_list = ["raju", "booju", 69, 420, "kaju", "icefruit"]
example_list.append("sunny")
print("example_list")
print(len("example_list"))
example_list.remove("booju")
print(example_list)
```
### *Slice a list*

Users can also create a slice from the list i.e., can extract a portion from the existing list and can create a new list from the extracted elements using the syntax shown below.
```
example_list = ["raju", "booju", 69, 420, "kaju", "icefruit", "sunny"]
new_list = example_list[0:2]
```
In the above line, 0 indicates the index position of the elements and 2 indicates the no. of elements to be extracted from the specified index position. 
Basing on the above logic, the new_list will contain only two elements from the zeroth position ie., `new_list = ["raju", "booju"]`

Similarly, `sub_list = example_list[2:4]` will extract elements from the secnd index position when counted from 0 ie., from 69 to the 4th element in the list when index position of the example_list is counted from 1 and creates the list `sub_list = [69, 420]` as the int 69 is in the second index position and python pics 4 elements from 69 including it.

#### *Syntax:*
```
In 
<list_name>[x:y], 
<list_name> = variable assigned to the list,
x = index position when counted from 0, 
y = yth element when index position counted from 1 instead of 0.
```

### *Concatenation*
Python allows the users to concatenate two lists using the following syntax.
```
cat = example_list + [1, 15, 230]
print(cat)      # above list will be appended to example_list

#  (or)

bat = new_list + sub_list
print(bat)      # appends the above slices lists, new_list and sub_list
```

### *Sorting*
Users can sort a list of values into an order in python, for example
```
primes = [7 , 3, 11, 5, 13]
primes.sort()
print(primes)
```
The function `<list_name>.sort()` is used to sort the elements of a list into an order. sort() function shouldn't be called inside a print function. It should be explicitly specified and print then prints the current state of the list.