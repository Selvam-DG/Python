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
-  
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
