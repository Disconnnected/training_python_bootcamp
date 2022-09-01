# OOP Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class OOP():
    def __init__(self) -> None:
        self.ex1 = self.Vehicle
        self.ex2 = self.Vehicle2
        self.ex3 = self.Vehicle3

    class Vehicle():
        """
            OOP Exercise 1: Create a Class with instance attributes
            Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

            OOP Exercise 2: Create a Vehicle class without any variables and methods
        """
        def __init__(self, max_speed, mileage) -> None:
            self.max_speed = max_speed
            self.mileage = mileage

    class Vehicle2():
        """
            OOP Exercise 2: Create a Vehicle class without any variables and methods
        """
        pass

    class Vehicle3():
        """
            OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
        """
        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage

    
    class Bus(Vehicle3):
        pass


# -------------------------------------------------

oop = OOP()
bus = oop.ex3("volvo", 100, 1200)

print(bus)