# Operators
There are different types of operators in python which are capable of performing different unique actions.
In python, Operators can be broadly classified into 7 different types as follows:

* Arithmetic Operators
* Assignment Operators
* Relational Operators
* Logical Operators
* Identity Operators
* Membership Operators
* Bitwise Operators

### 1. Arithmetic Operators

Arithmetic Operators will perform Arithmetic Operations as the name indicates i.e., they'll perform simple mathematical actions. The list of Arithmetic Operators is as follows:
* "+"  - Performs Additions
* "-"  - Performs Subtractions
* "*"  - Performs Multiplications
* "/"  - Performs Divisions
* "%"  - Performs Modulus i.e., This will give remainder of the division as an output.
* "//" - Performs Floor Divisions i.e., This will print the rounded value of the quotient after performing a division. eg: 2//3 returns the output as 3 while the actual answer is 2.5
* "**" - Performs the exponential calculations. i.e., `3**2` gives the output as 9 which is 3^2 (three sqaure).

### 2. Assignment Operators
Assignment Operators are used to assign and modify the values provided to variables. Assignment operators are also capable of performing arithmetic actions while adding the value to the operators. If arithmetic oprators are specified along with the = as below, the mentioned operation is performed on the variable and the value overwrites the existing variable value. Different types of Assignment operators are:

* "="   - Assign value to a variable. eg. x=2
* "+="  - Adds the provided numerical value to the variable. eg. `x+=2` performs 2+2 and x becomes x=4
* "-="  - Subtracts the provided numerical value from the variable. eg. `x-=2` performs 4-2 and x becomes x=2
* "*="  - Multiplies the variable with the provided number. eg. `x*=2` performs `2*2` and x becomes x=4
* "/="  - Divides the variable with the provided number. eg. `x/=2` performs 4/2 and x becomes x=2
* "**=" - Will the raise the variable to the power of provided numerical value. eg. `x**3` performs 2^3 `(2*2*2)` and x becomes x=8.
* "//=" - Performs floor division on the variable with the provided numerical value.
* "%="  - Performs modulus operation on the variable with the provided numerical value.

### 3. Identity Operators
Identity operators will perform the comparision over the value of two different objects and will return the boolean value *(true/false)* as an output. There are only two identity operators.

* "is"      - indicates equality in terms of usage and returns *true* if the condition is satisfied.
* "is not"  - indicates inequality in terms of usage and returns *true* if the condition is satisfied.

### 4. Logical Operators
Logical operators will allow the user to perform logical comparision over two outputs. There are three different logical operators as follows.

* "and" - returns true if both the operands are true.
* "or"  - returns true if one of the oprands is true.
* "not" - returns the opposite bool of the operand.

### 5. Membership Operators
Usually, Membership operators are employed to compare a value with the list of values and check for the availability. There are two different membership operators as follows.

* "in"     - Returns *true* if the provided value is in the provided list.
* "not in" - Returns *true* if the provided value has no match the requested list.

### 6. Relational Operators
In Python, Relational operators are used to compare the values and validate their condition through comparing the relation in between any given values. The different types of relational operators in Python are:

* "=="   - Equal to
* "!="   - Not Equal to
* ">"    - Greater than
* "<"    - Less than
* ">="   - Greater Than or Equal to
* "<="   - Less than or not equal to