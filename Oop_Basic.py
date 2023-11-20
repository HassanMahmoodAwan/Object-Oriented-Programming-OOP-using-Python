"""
Object-Oriented Programming Concepts

There are two-way of writing code
    1- Functional Programming
    2- OOP

Note: Python Build-in Functionalities are develop using OOP.

Total 6 Concepts in terms of OOP
    Class
    Objects
    Polymorphism
    Encapsulation
    Inheritance
    Data Abstraction

Note: Very important programming Concepts, give max time to work on it.

Important Points:
    1- One class have many instances called Objects.
    2- Attributes|Property, Behavior, Methods.
    3- Attributes define by variables and behavior by methods.
    4- Self is used to represent an object in a method.
    5- __Init__ is a method for defining Attribute for objects, it's like constructor.


Note: A class is a collection of objects.
"""


def python_build_in():
    a = 10
    print(type(a))  # Shows variable 'a' of class <int>


def basic_class_concept():
    class Student:
        # Class Attribute
        university = 'COMSATS, Lahore Campus'

    # Creating an Object
    hassan = Student()
    print(hassan.university)  # Not prefer way.
    print(hassan.__class__.university)  # clarify more (prefer).


def class_concept_instance_attr():
    class Student:
        # declaring instance Attr using Constructor
        def __init__(self, reg_no):
            self.reg_no = reg_no

        # Instance Method
        def display(self):
            return self.reg_no

        # Class Attribute
        university = 'COMSATS, Lahore Campus'

    # Creating an Object
    # pass instance attribute value.
    hassan = Student('SP20-BCS-114')

    print(hassan.__class__.university)
    # Instance Attr
    print(hassan.reg_no)

    print(hassan.display())
    print(Student.display(hassan))  # Work Same.
    print(type(hassan))


def class_advance_concept():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def compare(self, other):
            return True if self.age == other.age else False

        def update(self):
            self.age = 22

    p1 = Person('Hassan', 21)
    p2 = Person('Hamid', 20)

    print('Both are same') if p1.compare(p2) else print('Not same')

    p2.update()
    print(p1.name + "\n" + p2.name)
    print(f"{p2.age}")


# Variables Type in OOP (instance or (static or class)
def variables_oop():
    class Car:
        def __init__(self):
            self.Company = 'Toyota'
            self.model = 'Corolla'

        # Class variable.
        seater = 5

        # Method of display
        def display(self):
            print(self.Company + '\n' + self.model + '\n' + self.seater + ' ')
            return ''

    # you can change variables inside class using object.
    car1 = Car()
    car1.Company = 'Honda'
    car1.model = 'BRV'
    car1.seater = '7'

    print(car1.display())


if __name__ == '__main__':
    variables_oop()
