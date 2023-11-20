"""
Polymorphism: The word polymorphism means having many forms.

In programming, it refers to methods/functions/operators with the same name that can be executed on many objects or classes.


Example:   (Build-in Function Polymorphism)

            len('string')
            len('age')
Note: Same func but use many times and diff result.
"""

# ====== Class Polymorphism ======
def class_polymorphism():
    class Car:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

        def move(self):
            print("Drive!")

    class Boat:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

        def move(self):
            print("Sail!")

    class Plane:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

        def move(self):
            print("Fly!")

    # Instance / Objects
    car1 = Car("Ford", "Mustang")  # Create a Car class
    boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat class
    plane1 = Plane("Boeing", "747")  # Create a Plane class

    for x in (car1, boat1, plane1):
        x.move()


# ====== Inheritance Class Polymorphism =====
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()



if __name__ == '__main__':
    class_polymorphism()



