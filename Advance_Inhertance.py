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
            self.country = 'Pakistan'

        def __str__(self):
            return 'Hello to Person Class'

    class Employee(Person):
        # Need to assign Values otherwise through Error.
        def __init__(self):
            Person.name = 'Hassan'
            Person.age = '21'

        @staticmethod
        def show():
            print('Its Employee Class')

    # Objects / Instance
    emp1 = Employee()
    print(emp1)
    emp1.show()
    print(emp1.name)
    print(emp1.country)  # Through error. Not recognize.


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
    print(emp1)
    print(emp1.is_employee())


if __name__ == '__main__':
    # inheritance_basics()
    super_keyword()