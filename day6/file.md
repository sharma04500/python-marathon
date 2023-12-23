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
Unlike any other data types, dictionaries too can exist as multiple elements and can be specified as a list of dictionaries.

Data related to multiple ec2 instances or s3 buckets or commits made to a github repo etc are examples for data which can exist in the form of list of dictionaries.

```
s3_buckets = [
    {
        "name": "demo-bucket",
        "status": "Present"
    },
    {
        "name": "trail-bucket",
        "status": "Removed"
    },
    {
        "name": "third-bucket",
        "status": "InfrequentAccess"
    }
]
```
To extract a particular field from data stored into different elements, the syntax is:
```
print(s3_buckets.[0]["status"])
print(s3_buckets.[1]["status"])
print(s3_buckets.[2]["name"])
```
To extract data from all the elements, we should use a for loop as follows:
```
for index in range(len(s3_buckets)):
    print( "The status of the", s3_buckets[index]["name"]+":", s3_buckets[index]["status"])
```
*In the above for loop length function is called b'coz the purpose of using the variable in  our requirement is to call the index, which should be the number indicating the position of the element. i.e., in the above case length function gives the output as "3" and range function resolves it as [0, 1, 2], which are our desired values.*
