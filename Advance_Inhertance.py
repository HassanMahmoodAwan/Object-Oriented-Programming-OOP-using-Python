"""
Inheritance: An Important Concept. It's like a Parent Child Relationship. The parent Class can be used by the Child
class, which means attributes as well as methods can be used by child class.


Note: Credit Goes to Geeks for Geeks

Note: Learn Multilevel Inheritance and also Multiclass Inheritance.
"""


def inheritance_basics():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            self.country = 'Pakistan'  # Protected Variable.
            self.__private = 'secret'  # Private variable

        def __str__(self):
            return f'Hello to Person Class {self.name}'

    class Employee(Person):
        # Need to assign Values otherwise through Error.
        def __init__(self, name, age):
            Person.__init__(self, name, age)
            Person.name = 'Hassan'  # not work
            Person.age = '21'       # not work, logic.

            print(self.country)     # work.
            print(self.__private)   # Through error.




        @staticmethod
        def show():
            print('Its Employee Class')

    # Objects / Instance
    emp1 = Employee('hassan', 22)
    print(emp1)
    emp1.show()
    print(emp1.name)
    print(emp1.country)  # Now, it works
    print(emp1.__private)  # Now, it not work, through error.


# ====== Inheritance Super Keyword ======= #
def super_keyword():
    class Person:
        def __init__(self, name, age):
            self.name = name   # gives Hassan
            self.age = age

        def __str__(self):
            return f'{self.name} {self.age} {self.role} {self.company} '

        # Check if a Person is Employee or Not.
        def is_employee(self):
            return False

    class Employee(Person):
        def __init__(self, name, age, role):
            self. company = 'Purelogics'
            self.Name = name  # gives Ali
            self. role = role
            super().__init__('Hassan', age)


        def show(self):
            return f'{self.Name} {self.age} {self.role} {self.company} '

        def is_employee(self):
            return True

    # Objects / Instance
    emp1 = Employee('Ali', 22, 'Real Estate Agent')
    print(emp1.show())
    print(emp1)  # gives Hassan
    print(emp1.is_employee())


if __name__ == '__main__':
    inheritance_basics()
    # super_keyword()