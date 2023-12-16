# "string - Usage and Basic Functions"
Double quotes are used to specify a string.

String is a group or list of charecters which might or might not be readable but indicate a particular entity. A string is a group of charecters enclosed within single(') or double(") quotes which might or might not contain numbers, letters, special charecters and spaces.

For example, `Hello,` and `world!` are two different words with special charecters and a space in between. If they are enclosed into quotes like "Hello, world!", Python interprets both the words as single string. Any data enclosed by single or double quotes is a `string` in Python's point of view. 

> The print() function prints the specified data in the brackets.
##### *print*
```
print ("Hello, world!")
```

`arn` is the variable storing the string as illustrated below: /n
As the complete arn is places in between quotes, python will consider it as a single string.

```
arn = "arn:aws:iam::123456789012:user/johndoe"
```

The split function splits the given data as specified and prints it in the list format i.e., [0,1,2..n]
##### *function.split()*
```
print (arn.split("/"))
```

If you specify the index position of the value to be printed as shown below along with the split function,It prints that particualr value. In the above case python splits the given arn into two i.e., before and after slash and prints both the values as a list. From the obtained list, the second value is the username, which we are supposed to extract and to get that value, we have to specify the index position of the value from the obtained list, i.e., the second place. As the indexing of values of a list starts from 0, the second place is given by 1 as illustrated in the below example.

```
print ( arn.split("/")[1] )
```
##### *function.upper()*
In python, we have various inbuilt functions to handle the strings in various ways to extract and modify the data. For example If, we intend to print the above extracted data in uppercase letters, just use the function .upper() 
along with the string as illustrated below.

```
print( arn.split("/")[1].upper())
```
##### *function.lower()*
We can also use the function `lower()` to convert the output to lowercase letters. For example:

```
print(arn.split("/")[1].upper().lower())
```
##### *Concatenation*
Consider another variable one as Hello and two as the value being extracted from the above example arn

```
one = "Hello"
two = arn.split("/")[1].upper()
```
To combine both the variables and place a space in between them type one, " " space in quotes and two as the third variable result and print the variable result.

```
result = one + " " + two   # ---> This is called concatenation.
```

concatenation is combining multiple strings and merging them.

To print the variable result:

```
print (result)
```

Using one of the variables with random strings : 

```
print ("Username :",two)
```

##### *function.len()*
To get the length of a string, Use the function len(). This gives the number of charecters in the string. This example gives the no. of charecters present in the arn.

```
print (len(arn))
```

Combining multiple functions. Resusing the first variable arn:

##### *Multiple Functions*
```
print ("Extract Username from" + arn,"The answer is:"+ two,"The length of string is:", len(arn))
```

While generating the Output, comma (,) is printing a space and + isn't printing any space between two values while concatenating.

##### *function.strip()*
Another funtion to handle strings is strip(). Strip function is used to remove Unnecessary spaces before and after the string. In the below example, look at the variable `spaced`. It contains few spaces before and after the text.


Let's consider another variable stripped to strip the spaces from `spaced` and store the value.

```
spaced = "   Observe the spaces bro   "
stripped = spaced.strip()
```

Now, Printing the output i.e., `stripped`. Also I've concatenated a . to indicate the end of a string
```
print("Stripped text:", stripped+".")
```
`file.py` in this folder is an executable python file, with all the python lines mentioned in this markdown file.

Just type `py file.py` or `python file.py` or `python3 file.py` with respect to the machine, which you're using