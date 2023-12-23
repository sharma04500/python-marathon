# Sets ---> Need & Usage !!!

Sets are almost similar to lists and tuples in terms of usage with a minor existential difference.
Sets doesn't allow duplicate values i.e., any two elements of a set, irrespective of their positions shouldn't be of the same value, irrespective of the data type. The elements of a set are comma(,) seperated values enclosed in flower braces as illustrated below.
```
example_set = {1, 2, 3, 4, 5}
```
Though the scope for usage of sets is limited in DevOps prospect, writing the names of s3 buckets as a set is an ideal use case, as every bucket should contain a unique name i.e., non-repeated values in Python's view.
```
s3_buckets = {"demo_bucket", "trail_bucket", "test_bucket"}
``` 
Lists are enclosed with ["closed", "braces"]
Tuples are enclosed with ("open", "braces")
Sets are enclosed with {"Flower", "braces"}