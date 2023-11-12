# Function

- Python Functions is a block of statements that return the specific task. The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.


#### Some Benefits of Using Functions
  - Increase Code Readability 
  - Increase Code Reusability
#### Syntax: 
- keyword Function_name (parameters)
  - def function_name(parameter)
   - statement
   - return expression
     
- After creating a function, we can call it by using the name of the function followed by parenthesis containing parameters/arguments of that particular function
  
#### return statement:
- return statement is used to exit from a function and go back to function caller and return the value.
- The return statement can consist of a variable, an expression, or a constant which is returned at the end of the function execution. If none of the above is present with the return statement a None object is returned.
- return value may be a data type if it is a single value and it is a tuple if it returns multiple value
  
#### Types of Functions in Python
- **Built-in library function**:
  - These are Standard functions in Python that are available to use. (print, input, length.....)
- **User-defined function:**
  -  We can create our own functions based on our requirements.
  -  We can create a user-defined function in Python, using the **def** keyword.
   
- difference between function and method :
    - Function is defined outside of class whereas method is defined inside the class
    - to use function, we don't use "." operator but, methods are accessed with "." operator (for eg. list.append())
    

      

#### Types of Arguments in Function
- Default argument
  - parameter that assumes a default value if a value is not provided in the function call for that argument.
    
- Keyword arguments (named arguments)
  - Here specify the argument name with values but the order of the parameters may change
    
- Positional arguments
  - Arguments should be in the correct order while calling the function
  - Number of arguments also match with function calling aruguments.
- Arbitrary arguments (variable-length arguments *args and **kwargs)
  - can pass a variable number of arguments to a function using special symbols.
  - *args in Python (variable-length Non-Keyword Arguments)
  - **kwargs in Python (variable-length Keyword Arguments)
    
#### Ananymous Function:
- a function is without a name. 
- the lambda keyword is used to create anonymous functions.
- syntax:
  - lambda arg1, arg2......: expression
  - here, return value is expression, no need to write return statement explicitly
 
#### Others:
- **filter** => filter a sequence based on some conditions, retuns a filter object
  - syntax:=> filter(funciton,seq)
    - ex=> list(filter(lambdaa num:num%2,seq))
- **map** => mapping every value of existing sequences to a set of values and returns map object
  - syntax=> map(function,sequence)
    
# scope and Namespaces:
- LEGB => L- Local, E- Extended, G - Global, B - Built-ins
- Name (which means name, a unique identifier) + Space(which talks something related to scope)
- Namespace is a container that store values which may be Local container, Extended container, Global container or built-in container
- local containers are in Extended containers, Extended containers are in Global containers, Global containers are in Built-in container
- the values defined in local container, can't be accessed in Global or built-in containers but built-in container values are accessed in local containers. 
