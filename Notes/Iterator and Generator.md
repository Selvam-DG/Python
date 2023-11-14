# Iterators
#### Iterable:
- An iterator in Python is an object that is used to iterate over iterable objects.
- list, tuple, set, dictionary, string etc., are the iterable objects that the elements in the objects are iterable(able to run for loop over them)
- The Python iterators object is initialized using the iter() method. It uses the next() method for iteration
  - **__iter__()**: The iter() method is called for the initialization of an iterator. This returns an iterator object
  -**__next__()**: The next method returns the next value for the iterable. When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object, which further uses the next() method to iterate over.
 #### Iterable vs Iterator:
- The main difference between them is, iterable in Python cannot save the state of the iteration, whereas in iterators the state of the current iteration gets saved
- Every iterator is also an iterable, but not every iterable is an iterator in Python

# Generator

- A Generator in Python is a function that returns an iterator using the Yield keyword.
- A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with the **yield** keyword rather than **return**.
- If the body of a **def** contains **yield**, the function automatically becomes a Python generator function
- syntax:
  - def function_name():
     - yield statement
     - yield statement (multiple yield statements are possible)
 - return in a function returns only one value whereas multiple yield statements return multiple values in Generator function.
- Generator object always remembers its previous step
- **generator expression** is another way of writing the generator function.
  - syntax:
    - gen_name = (expression for item in iterable)
  - tuple comprehension creates a generator object
#### Advantage:
 - Generator object is executed only when it is executed in a for loop
 - generator object never store the reference of their objects
 - Generators provide a space-efficient method for data processing as only parts of the file are handled at one given point in time
