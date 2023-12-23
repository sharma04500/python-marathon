student_info = {
    "name": "Sharma",
    "Class": "LKG",
    "Age": 4,
    "D.O.B": "yesterday"
}

print(student_info)
print(student_info["D.O.B"])
print(student_info["Age"])

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

print(s3_buckets[0]["status"])

for index in range(len(s3_buckets)):
    print( "The status of the", s3_buckets[index]["name"]+":", s3_buckets[index]["status"])
