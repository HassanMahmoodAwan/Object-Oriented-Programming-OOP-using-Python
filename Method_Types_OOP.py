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

Types of Methods in OOP:

    1- Instance Methods:
             Through which perform getter|setter operations and also can do computation in it.

    2- Class Methods:
        Used for the class variables to return them. Also, we need to declare a decorator for this type of method.
        @classmethod

    3- Static Methods:
            Methods which return nothing's, just used to print somthing like message.
            Note: it doesn't use self keyword as it not take attributes/properties.
            @staticmethod

    4- Special Methods:
            Methods like __str__(), which have some specific purpose are special methods.
                Constructor -> __init__(self) is also a special method

"""


def class_methods():
    class Student:
        def __init__(self, name, roll_no):
            self.name = name
            self.roll_no = roll_no
            self.gpa = dict()

        # class variable
        University = 'COMSATS University'

        # Class method
        @classmethod
        def university(cls):
            return cls.University

        # Instance variable
        def compute_gpa(self, subject, gpa):
            update_dict = {f'{subject}': gpa}
            gpa = self.gpa.update(update_dict)

            return gpa

        # static Method
        @staticmethod
        def message():
            print('This Class represents a individual Student')

        # Instance Method
        def display(self):
            print(f'{self.name}, {self.roll_no}, {self.University}, {self.gpa}')

        # __str__() Method (Preferred Way of Display)
        def __str__(self):
            return f'{self.name}, {self.roll_no}, {self.University}, {self.gpa}'

    # Declaring Objects Here
    std1 = Student('Hassan', 'SP20-BCS-114')
    std1.compute_gpa('DSA', '3')
    std1.compute_gpa('DIP', '3.3')

    print(std1.university())
    print(std1.__class__.University)

    # std1.display()
    print(std1)


if __name__ == '__main__':
    class_methods()
