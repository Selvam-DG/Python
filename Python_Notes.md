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
   - Integer: 
     - Any real number without decimal point
     - Integers can be represented in binary, octal and hexadecimal
     - No concept of short,long int
     - **bin()** function is used to convert from decimal to binary and all digits in 0 & 1, preceded by 0b (eg. 10 is in binary form as 0b1010)
     - **oct()** function is used to convert from decimal to oct and all digits in 0 to 7 preceded by 0o
      - **hex()** function is used to convert from decimal to hexadecimal and all digits in 0 to 9, A-F preceded by 0x (eg. 10 is in binary form as 0b1010)   
   - Float:
      - Represented in decimal format
      - No concept of double in float
   - Complex:
      - real + imaginary values in complex data type
- Boolean:
   - Only two values in Boolean. True = 1;False = 0
- String:
   - Values inside ' '," ", ''' ''', """  """, are strings
   - String is a sequence of characters i.e, an ordered collection of elements.
      - accessed the element from +ve index from left to right and -ve index from right to left
      - Indexing => accessing single element
      - slicing => accessing multiple elements
      - concatenation => combine 2 0r more strings using '+' operator
      - repetition => repetition of a string for more than 1 time, use * operator
      - Membership => to check whether an element or group of elements are part of seq
      - Identity =>
      - len => returns length of string or total number of char
#### Methods related to String:
   - dir(str) gives a library of string methods in Python
   - capitalize() => used to capitalize the first char of the string
   - casefold() => used to convert uppercase to lowercase letters and it is more aggressive
   - lower()=>  used to convert uppercase to lowercase letter
   - swapcase() => used to swap the cases of string
   - upper() => used to convert all to uppercase
   - startswith() or endswith() => returns True or False based on whether the string is starting or ending with given condition
   - title() => return string where every 1st char of the word is capitalize
   - isalnum(), isalpha(), isascii(), isdecimal(), isdigit(), isidentifier(), islower(), isnumeric(), isprintable(), isspace(), istitle(), isupper() => Returns True or False based on the method.
   - find(), rfind, index(), rindex() => returns the index of substring that you are looking for in a given string. find(), index() => start search from left side and rfind(), rindex() => start search from right side
   - strip(), rstrip(), lstrip() => used to remove the unnecessary spaces from the string from string start or end or both but not mid
   - count() => gives the total no. of occurrences of a given string
   - replace() => replaces old string with new string
   - split(), rsplit() => split the string  by spaces and returns a list of words 
   - join() => used to join list of words with a separator. format is different from other methods. (eg: print('',join(string)))


  #### Mutable  and Immutable Data types:
  - List, bytearray, dictionary,set are mutable data types i.e, changes will make on the same object.
  - rest all are immutable i.e not modified the values on the same object.

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



- **ord()** gives ASCII value of Character and chr() is used to get the character from number
- **id()** is used to get the address of the variable.


#### Derived Data Types:
- List
- Tuple
- Set
- Frozenset
- Dictionary
- bytes
- bytearray
- range

#### List
- Any element inside square brackets separated by a comma.
- List is a Sequence, ordered collection of elements that can hold any data type as elements
- List is mutable i.e elements in the list are modified
- List has positive and negative indexing, supports both indexing and slicing
- List can be created from string, tuple, dictionary
- Basic operations are Indexing, slicing, concatenation, Membership, Identity
- **dir(list)** gives the methods on the list.
  - append, clear, copy, count, extend, index, insert, pop, remove, sort
  - for example, list.append([]) => used to add an elements to the list
  - insert, append, extend used to add elements to list
  - pop, remove used to remove elements from the list
  - Aliasing => giving different name to an existing object with the same address (changes reflected on both previous and recent variables)
  - shallow copy => slicing and copy (changes reflected on only recent variables, but id are same in nested list elements)
  - deepcopy => elements in nested list are all different in the deep copy list
- List Comprehension:
   - [expression for i in sequence if condition]







- 


