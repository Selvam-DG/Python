# Numpy
- Numpy is nothing but Numerical Python which deals with array either 1D or N-D arrays
- NumPy is a Python library used for working with arrays, used for computation with 1D or 2D arrays
- List is a heterogenous collection of items that stores integer, char, float etc and it takes more memory than the array
- An array is homogenous collection of numbers and stored at one continuous place in memory unlike lists, so access and  manipulate them very efficiently. So Numpy array objects are faster than Python lists.
- NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.
#### Why Numpy?
- Every data in the world is represented in the form of an array. so we can easily perform analysis by accessing and manipulating them very easily in Numpy or Matlab because it is collection of homogeneous items.
- A powerful N-dimensional array object, useful in linear algebra, Fourier transform, and random number capabilities.
### Numpy Array Creation:
- You can create an array from a regular Python list or tuple using the array() function
-  The array object in NumPy is called ndarray. We can create a NumPy ndarray object by using the array() function
-  NumPy Arrays provides the **ndim** attribute that returns an integer that tells us how many dimensions the array have
-  0-D Arrays
   - 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
- 1-D Arrays
  - An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array. These are the most common and basic arrays.
 
- 2-D Arrays
  - An array that has 1-D arrays as its elements is called a 2-D array. These are often used to represent matrix or 2nd order tensors.
- 3-D arrays
  - An array that has 2-D arrays (matrices) as its elements is called 3-D array. These are often used to represent a 3rd order tensor.
- NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have
- **Numpy Data Types**:
  - Below is a list of all data types in NumPy and the characters used to represent them.
     - i is integer
     - b is boolean
     - u is unsigned integer
     - f is float
     - c is complex float
     - m is timedelta
     - M is datetime
     - O is object
     - S is string
     - U is unicode string
  - The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
- **arange**: This function returns evenly spaced values within a given interval and Step size is specified.
   - Syntax:
      - varible = np.arange(start,stop,step_size)
- **linspace**: It returns evenly spaced values within a given interval
   - Syntax:
      - variable = np.linspace(start, end, evenly number of elements)
- **Reshaping array**: We can use reshape method to reshape an array.
   - while reshaping the array, the number of elements remains unchanged that is row and columns is equal to the number of elements in the array.
   - syntax:
      - variable1 = varaible.reshape(row,columns)
- **Flatten array**: We can use the flatten method to get a copy of the array collapsed into one dimension array. It accepts order argument
   - syntax:
     - variable2 = varaible.flatten()
- NumPy offers several functions to create arrays with initial placeholder content. These minimize the necessity of growing arrays, an expensive operation. For example: np.zeros, np.ones, np.full, np.empty, np.eye etc.,
   - syntax:
     - variable = np.zeros(row, columns)
     - var2 = np.full((m,n),value)
     - var3 = np.random.rand((rows,column))
     - var4 = np.eye(rows, columns)

### NumPy Array Indexing:
- **Slicing**: Just like lists in Python, NumPy arrays can be sliced. As arrays can be multidimensional, you need to specify a slice for each dimension of the array.
- **Integer array indexing**: In this method, lists are passed for indexing for each dimension. One-to-one mapping of corresponding elements is done to construct a new arbitrary array.
- **Boolean array indexing**: This method is used when we want to pick elements from the array which satisfy some condition.

### NumPy Basic Operations:
- **Operations on a single NumPy array**
  - We can use overloaded arithmetic operators to do element-wise operations on the array to create a new array. In the case of +=, -=, *= operators, the existing array is modified.
    
- **Unary Operators**
  - Many unary operations are provided as a method of ndarray class. This includes sum, min, max, etc. These functions can also be applied row-wise or column-wise by setting an axis parameter
    
- **Binary Operators**
  - These operations apply to the array elementwise and a new array is created. You can use all basic arithmetic operators like +, -, /,  etc. In the case of +=, -=, = operators, the existing array is modified

- **Introduction to NymPy’s ufuncs**
  - NumPy provides familiar mathematical functions such as sin, cos, exp, etc. These functions also operate elementwise on an array, producing an array as output.
  - Note:
     -  All the operations we did above using overloaded operators can be done using ufuncs like np.add, np.subtract, np.multiply, np.divide, np.sum, etc

- **NumPy Sorting Arrays**:
  - There is a simple np.sort() method for sorting Python NumPy array


- **Iterating over array elements**
  - Iterating means going through elements one by one.
  - As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python

- **Slicing arrays**:
   - Slicing in python means taking elements from one given index to another given index.
   - We pass slice instead of index like this: [start:end].
   - We can also define the step, like this: [start:end:step].
   - Use the minus operator to refer to an index from the end (Negative Indexing)
- **Joining Arrays**:
   - concatenate() function is used to add two arrays, along with the axis.
   - Stacking is same as concatenation, the only difference is that stacking is done along a new axis
     - hstack ()
     - vstack ()
     - dstack ()
- **Copy vs View**:
   - The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
   - The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view
- **Splitting an array**:
  - use array_split() for splitting arrays, we pass it the array we want to split and the number of splits
  - synatx:
    - variable = np.array_split(array_Name, Size)
   
- **where()** method is used to search a value in an array.
- **searchsorted()** method performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
-fitering array is used to filter the values which satisf the condition and returns boolean values as True or False corresponding to Indices
