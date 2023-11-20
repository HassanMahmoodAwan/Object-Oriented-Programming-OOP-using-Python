"""
Object-Oriented Programming Concepts

Total 5 Concepts in terms of OOP
    Class
    Objects
    Polymorphism
    Encapsulation
    Inheritance
    Data Abstraction

Note: Very important programming Concepts give max time to work on it.


Inheritance: An Important Concept. It's like a Parent Child Relationship. The parent Class can be used by the Child
class, which means attributes as well as methods can be used by child class.

"""


def inheritance():
    # Parent Class
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        # Instance Method
        def display(self):
            print(f'{self.name} {self.age}')

    # Child Class
    class Student(Person):
        def __init__(self, name, age, roll_no, degree):
            super().__init__(name, age)
            self.roll_no = roll_no
            self.degree = degree

        # Class attribute
        University = 'COMSATS University'

        # Just return in __Str__ method, then print by Object.
        def __str__(self):
            return f'{self.name} {self.age} {self.roll_no} {self.degree} {self.University}'

    std1 = Student('Hassan', 21, '114', 'BCS')

    std1.display()

    print(std1)


if __name__ == '__main__':
    inheritance()
