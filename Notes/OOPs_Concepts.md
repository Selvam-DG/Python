# Object-Oriented Programming (OOP) in Python

## Why OOP?

When building large-scale applications, traditional programming approaches can cause several issues:

- **No code reusability**: You often need to write the same logic multiple times.
- **Hard to debug**: As the lines of code increase, it's more difficult to identify and fix bugs.
- **Poor maintainability**: Understanding the behavior of the application becomes complex with increasing code size.

OOP solves these problems by organizing code into reusable objects and promoting principles like encapsulation, inheritance, and polymorphism.

---

## What is OOP in Python?

- **Object-Oriented Programming (OOP)** is a programming paradigm that models software design around **objects** and **classes**.
- It mimics real-world entities by incorporating:
  - **Encapsulation**
  - **Inheritance**
  - **Polymorphism**
  - **Abstraction**

---

## OOP Concepts in Python

### 1. Class

- A **class** is a blueprint for creating objects (a logical structure).
- It groups data (attributes) and behaviors (methods).

**Syntax:**

```python
class ClassName:
    # attributes
    # methods
    pass
# Example
class Car:
    wheels = 4  # Class variable

    def __init__(self, brand, model):
        self.brand = brand      # Instance variable
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} started.")
```
### 2. Object
- An object is an instance of a class.
- It has:
  - State (attributes)
  - Behavior (methods)
  - Identity (unique reference in memory)

Example:
```python
my_car = Car("Toyota", "Camry")
my_car.start()  # Output: Toyota Camry started.

```
### 3. `__init__()` Constructor
- Automatically called when a new object is created.
- Used for initializing object attributes.
```python
def __init__(self, attr1, attr2):
    self.attr1 = attr1
    self.attr2 = attr2
```
### 4. `self` Keyword
- Refers to the instance of the class.
- Used to access variables that belong to the class.

#### Types of Variables in Class
##### 1. Instance Variable
- Defined inside the constructor using self.
- Unique to each object.

##### 2. Class Variable (Static Variable)
- Shared across all instances.
- Defined directly in the class body.
```python
class Dog:
    species = "Canis familiaris"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

```

## Inheritance
- Allows one class to inherit properties and methods from another.
- Types:
  - **Single Inheritance**
  - **Multiple Inheritance**
  - **Multilevel Inheritance**
  - **Hierarchical Inheritance**
```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def display(self):
        print("Child")

obj = Child()
obj.show()
obj.display()

```
### `super()` Function
- Used to call methods of the parent class.
```python
class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

```
## Polymorphism
- Means "many forms".
- The same method or function can behave differently based on the context.
- 
**Example: Function Overriding**
```python
  class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

a = Animal()
d = Dog()

a.sound()  # Some sound
d.sound()  # Bark
```
## Encapsulation
- Hides internal details and shows only essential features.
- Achieved by using access modifiers:
  - Public: accessible from anywhere
  - Protected (_): accessible within class and subclasses
  - Private (__): accessible only within the class

```python
class Person:
    def __init__(self, name):
        self.__name = name  # private attribute

    def get_name(self):
        return self.__name

```
## Abstraction
- Hides complex implementation and shows only relevant data.
- Achieved using abstract base classes with the abc module.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

```
## Summary 
| Concept       | Description                                   |
| ------------- | --------------------------------------------- |
| Class         | Blueprint for creating objects                |
| Object        | Instance of a class                           |
| `__init__`    | Constructor method                            |
| `self`        | Refers to current object                      |
| Inheritance   | Reuse code from a base class                  |
| Polymorphism  | Same method name, different behavior          |
| Encapsulation | Restrict direct access to class data          |
| Abstraction   | Hide complexity, show only necessary features |










