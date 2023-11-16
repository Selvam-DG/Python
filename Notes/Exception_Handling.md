# Exception handling in Python
#### Topics:
  - Type of Error
  - What is an Exception?
  - Why is Exception required?
  - How to handle the exception
  - User-defined exception
  - Regular Expression in Python
- Debugging
  - The process of removing the bugs from applications
#### Types of Error in a program
  - Compile time  Error
  - Run time Error
    - NameError, TypeError, ValueError, FileNotFoundError, OverflowError, ZeroDivisionError, ImportError, IOError, AttributeError 
  - Logical Error 
- Exception Handling is used to control RunTimeError, Logical Error has to be corrected in the program by rechecking again
- The Errors that can be handled using the Exception handling concept are called Exceptions

- Simply all exceptions are Errors but all Errors are not exceptions.
#### Difference between SyntaxError and Exceptions
- S**yntax Error**: As the name suggests this error is caused by the wrong syntax in the code. It leads to the termination of the program.
- **Exceptions:** Exceptions are raised when the program is syntactically correct, but the code results in an error. This error does not stop the execution of the program, however, it changes the normal flow of the program.
#### **BaseException**
- There are several built-in exceptions that can be raised when an error occurs during the execution of a program. Here are some of the most common types of exceptions in Python
  - ArithmeticError
  - AttributeError
  - AssertionError
  - SyntaxError
  - TypeError
  - EoFError
  - RunTimeError
  - ImportError
  - NameError

- What problem may arise if we don't handle the Exception?
  - lose The data
  - Corruption in Program
    
## try, except, else, finally
#### try, except:
- try block should be used only for that part of the code which you are expecting to raise the error
- Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the **try** clause and the statements that handle the exception are written inside **except** clause
- syntax:
  - try:
    - Condition Statement
  - except:
     - statement
#### try-except-else:
- In Python, you can also use the else clause on the try-except block which must be present after all the except clauses.
- - syntax:
  - try:
    - Condition Statement
  - except:
     - statement
  - else:
     - statement
#### try - except - else - finally:
- Python provides a keyword finally, which is always executed after the try and except blocks. The final block always executes after the normal termination of the try block or after the try block terminates due to some exception.
- Syntax:
  - try:
    -  Some Code
  - except:
    - optional block
    - Handling of exception (if required)
  - else:
    - execute if no exception
  - finally:
    - Some code .....(always executed)
#### Different ways to write Exception statements
- except ExceptionClassName:
- except ExceptionClassName as e:
- except (ExceptionClassName1, ExceptionClassName2,ExceptionClassName3......)
- except:
  - default exception
- while writing the exceptions, order of exceptions is important (child class exception should always come first and then the parent class exception)
#### User-defined Exception:
- 
