""""
Key Points to Remember:
1. Object-Oriented Programming makes the program easy to understand as well as efficient.
2. Since the class is sharable, the code can be reused.
3. Data is safe and secure with data abstraction.
4. Polymorphism allows the same interface for different objects, so programmers can write efficient code.
    """

"""
Python Classes:
 1.A class is considered as a blueprint of objects.
 2. It contains all the details about the Object
Python Objects:
 1.An object is called an instance of a class.
 Here's the syntax to create an object.
    objectName = ClassName()
 We use the . notation to access the attributes of a class. For example,
    # modify the name attribute
    bike1.name = "Mountain Bike"
    
    # access the gear attribute
    bike1.gear
"""
"""
Example 1: Python Class and Objects
"""


# define a class
class Bike:
    name = ""
    gear = 0


# create object of class
bike1 = Bike()

# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")

"""
Create Multiple Objects of Python Class
"""


# define a class
class Employee:
    # define an attribute
    employee_id = 0


# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()

# access attributes using employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

# access attributes using employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")

"""
Python Methods
 1.We can also define a function inside a Python class.
 2.A Python Function defined inside a class is called a method.

"""


# create a class
class Room:
    length = 0.0
    breadth = 0.0

    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)


# create object of Room class
study_room = Room()

# assign values to all the attributes
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()

"""
 *Constructors in Python:
 1. Constructors are generally used for instantiating an object. 
 2. The task of constructors is to initialize(assign values) to the data members of 
 the class when an object of the class is created. 
 3. In Python the __init__() method is called the constructor and is always called when an object is created.
 
 Types of constructors : 
  default constructor: 
      a. The default constructor is a simple constructor which doesn’t accept any arguments. 
      b. Its definition has only one argument which is a reference to the instance being constructed.
  parameterized constructor: 
      a. constructor with parameters is known as parameterized constructor. 
      b.The parameterized constructor takes its first argument as a reference to the instance being constructed 
  known as self and the rest of the arguments are provided by the programmer.
"""


class GeekforGeeks:

    # default constructor
    def __init__(self):
        self.geek = "GeekforGeeks"

    # a method for printing data members
    def print_Geek(self):
        print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()


class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)

# creating second object of same class
obj2 = Addition(10, 20)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()
