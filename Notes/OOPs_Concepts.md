# Why OOPs?
- Problems in a regular program with many thousands of lines
 - No code reusability of existing
 - Debugging and finding errors is difficult
 - Very difficult to understand the behavior of application if the number of lines of code is more


#### In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming
- aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming
- this concept is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.
#### OOPs Concepts in Python
- Class
- Objects
- Polymorphism
- Encapsulation
- Inheritance
- Data Abstraction
### Class:
- Blueprint or model to create an object is known as class.
- Class represents the common behavior of the group of objects
- Simply, A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created.
- A class is a logical entity that contains some attributes and methods
- Attribute is variable and methods are behaviors in class (method is nothing but functions inside the class)
- **Note**:
  - Classes are created by keyword class.
  - Attributes are the variables that belong to a class.
  - Attributes are always public and can be accessed using the dot (.) operator
 - syntax:
    - class ClassName:
       - statement1
       - statement2 ....
       - statement-n
- Attributes and behavior are the members of class
 ### Objects:
 - The object is an entity that has a state and behavior associated with it.
 - An object consists of:
   - **State**: It is represented by the attributes of an object. It also reflects the properties of an object.
   - **Behavior**: It is represented by the methods of an object. It also reflects the response of an object to other objects.
   - **Identity**: It gives a unique name to an object and enables one object to interact with other objects.
 - A Class is defined without an object but without a class, object can't be defined.
 
#### Python __init__ Method
- __init__ method is constructor, it is run as soon as an object of a class is mapped.
- The method is useful to do any initialization you want to do with your object.
#### The Python self  
- Class methods must have an extra first parameter in the method definition. We do not
- give a value for this parameter when we call the method, Python provides it
- If we have a method that takes no arguments, then we still have to have one argument

#### Types of Variable
 - Instance variable
 - Class variable (static variable)

### Python Inheritance
- Inheritance is the capability of one class to derive or inherit the properties from another class.
-  The class that derives properties is called the derived class or child class and the class from which the properties are being derived is called the base class or parent class
- Python also has a **super()** function that will make the child class inherit all the methods and properties from its parent
- The benefits of inheritance are:
  - It represents real-world relationships well.
  - It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
  - It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A











