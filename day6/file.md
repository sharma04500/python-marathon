# Dictionaries  -->  Need and Usage!!!
Dictionaries are used to store detailed and extended information of an entity comprising multiple fields into a single variable. 
Dictionaries are represented in the form of several `key=value` pairs (seperated by commas) which are enclosed within flower braces as illustrated in the below example.
The detailed information of an ec2 instance viz., name, tags, public_Ip, private_IP etc. can be mentioned as a case which requires a data type like dictionaries.
```
student_info = {
    "name": "Sharma",
    "Class": "LKG",
    "Age": 4,
    "D.O.B": "yesterday"
}
```
To extract the data from a dictionary, the variable assigned to the dictionary is called along with the required field as illustrated below.
```
print(student_info) 
# prints the entire dictionary 
```
```
print(student_info["Age"]) 
# prints 4, as mentioned in the dictionary.
```
### *List of Dictionaries:*
Unlike any other data types, dictionaries too can exist as multiple objects and can be specified as a list of dictionaries.
