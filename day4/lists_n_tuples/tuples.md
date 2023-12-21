# Tuples  ---> Need and Usage !!!

Tuples are used to feed the data which is intended to be restricted and should be immutable throughout the program irrespective of the requirements. Declaring admin users to an entity using python will form an use case for tuples.

Tuples are almost similar to lists but are mentioned in open braces ().

The very basic existence of Tuples meant to restrict mutation of the data stored in them and Python limits the memory allocation to tuples as per the first input only.
In case of Tuples, users can't modify or play with the data stored into the variable unlike lists as the data can be fed only once and can't be modified through out the execution of the program.

```
example = ("hyderabad", "Chennai", "Banglore", 45)
```

Users can neither add nor remove the elements whenever needed and hence tuples are said to be `immutable` in nature.

Like lists, tuples too support writing data of multiple data types as elements into the same tuple and are `heterogenous` in nature.

Extracting element values and Indexing of tuples is similar to lists and first element of a tuple is considered as a zeroth element like lists.

Though modifying a tuple midway is not supported, Users can create a new tuple from concatenating the elements of multiple tuples viz., `new_tuple = example_tuple + extra_tuple`

### *length():*
Users can check the length or size of the tuple using the len() function.
For example: `print(len(example))`

### *Presence of an element*
Users in Python can also check for presence of a particular element in a tuple or list as follows. In the below clipboard, kolkata is an element and example is the tuple called in the beginning of this file.


```
is_present = 'kolkata' in example
```
another example:
`is_present = "Hyderabad" in example`