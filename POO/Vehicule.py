'''Public Member: Accessible anywhere from otside oclass.
Private Member: Accessible within the class "_"
Protected Member: Accessible within the class and its sub-classes "__"

Name Mangling to access private members
We can directly access private and protected variables from outside of a class through name mangling.
The name mangling is created on an identifier by adding two leading underscores and one trailing underscore, 
like this _classname__dataMember, where classname is the current class, and data member is the private variable name.'''


class Vehicle:
    def __init__(self, name, max_speed, mile_age):
        self.name = name
        self.max_speed = max_speed
        self.mile_age = mile_age

    def __str__(self):
        return f"Vehicle Name: {self.name}\nSpeed: {self.max_speed}\nMileage: {self.mile_age}\n{self.seating_capacity()}"
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    # Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
    def seating_capacity(self, capacity = 50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

bus = Bus("School Volvo", 180, 12)
print(bus)
