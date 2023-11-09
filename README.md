# Python

#### Data Types in Python:
- Fundamental Data Types
   - Integers
   - Floats
   - Complex
   - Boolean
   - None
   - String
- Number Data Types
   - Integer 
     - Any real number without decimal point
     - Integers can be represented in binary, octal and hexadecimal
     - No concept of short,long int
     - **bin()** function is used to convert from decimal to binary and all digits in 0 & 1, preceded by 0b (eg. 10 is in binary form as 0b1010)
     - **oct()** function is used to convert from decimal to oct and all digits in 0 to 7 preceded by 0o
      - **hex()** function is used to convert from decimal to hexadecimal and all digits in 0 to 9, A-F preceded by 0x (eg. 10 is in binary form as 0b1010)   
   - Float
      - Represented in decimal format
      - No concept of double in float
   - Complex
      - real + imaginary values in complex data type
- Boolean
   - Only two values in Boolean. True = 1;False = 0

#### Operators:
- Arithmetic Operators
   - +, -, *, / (true division), // (floor division => quotient), % (Modulus => remainder), ** (Exponent)
   - % &// operators do not work on complex numbers
- Comparison Operators
   - <, <=,>, >=
   - comparison between int and float is possible, but comparison between other data types and complex comparisons are not possible.
- Equality Operators
   - ==, !=
   - Equality comparison between different data types is possible and it compares the values only
- Logical Operators
   - and, or, not
- Bitwise Operators
   - & (and), |(or), ^ (xor), ~ (negation), << (left-shift), >> (right-shift)
   - The above operators works only on bits => True(1) and False (0)
- Assignment Operators
   - =, used to assign values to a variable 
- Compound Operators
   - +=,-+,*=, /=, //=, %=, **=, &=, |=, ~=, <<=, >>=
- Membership Operators
   - in, not in are membership operators
   - check whether element is part of sequence or mapping type or not
   - It works on str, list, tuple, frozenset, dictionary, bytes, range, bytearray
- Identity Operators
   - is, is not are identity operator
   - Returns True/False if condition satisfies/fails
- Ternary Operators
  - expression_1 if condition else expression_2
  - expression_1 if condition_1 else expression_2 if condition_2 else expression_3



- ord() gives ASCII value of Character and chr() is used to get the character from number
- id() is used to get the address of the variable.


