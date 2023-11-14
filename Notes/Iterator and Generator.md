# Iterators
#### Iterable:
- An iterator in Python is an object that is used to iterate over iterable objects.
- list, tuple, set, dictionary, string etc., are the iterable objects that the elements in the objects are iterable(able to run for loop over them)
- The Python iterators object is initialized using the iter() method. It uses the next() method for iteration
 - __iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object
 - __next__(): The next method returns the next value for the iterable. When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object, which further uses the next() method to iterate over.
