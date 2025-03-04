'''Public Member: Accessible anywhere from otside oclass.
Private Member: Accessible within the class "_"
Protected Member: Accessible within the class and its sub-classes "__"

Name Mangling to access private members
We can directly access private and protected variables from outside of a class through name mangling.
The name mangling is created on an identifier by adding two leading underscores and one trailing underscore, 
like this _classname__dataMember, where classname is the current class, and data member is the private variable name.'''
import time

if __name__ == '__main__':

    class Vehicle:
        fuel_type_list = ["Gasoline", "Diesel", "Electricity", "Hybrid"]
        def __init__(self, brand, max_speed, color, year, fuel_type, is_running = False):
            self.brand = brand
            self.max_speed = max_speed
            self.color = color
            self.year = year

            self.fuel_type = fuel_type
            if self.fuel_type not in self.fuel_type_list:
                raise ValueError(f"Fuel type not available! Choose between {self.fuel_type_list}")

            self.is_running = is_running

        def __str__(self):
            return f"Vehicle Brand: {self.brand}\nMax speed: {self.max_speed} km/h\nColor: {self.color}\nYear: {self.year}\nFuel: {self.fuel_type}\nState: {self.is_running}\n{self.seating_capacity()}"
        
        def seating_capacity(self, capacity=5):
            return f"The seating capacity of a {self.brand} is {capacity} passengers"  
        
        def start(self):
            print("Starting... ")
            time.sleep(2)
            print("The car is running")
            self.is_running = True

        def stop(self):
            print("Stopping...")
            time.sleep(2)
            print("The car is turned-off")
            self.is_running = False

        def status(self):
            if self.is_running == True:
                print("State of the car: running")
            elif self.is_running == False:
                print("State of the car: turned-off")


    vehicle_1 = Vehicle("suzuki s cross 2025", 195, "green", 2025, "Electricity")
    print("------------------------------------------")
    print(vehicle_1)
    print("------------------------------------------")
    vehicle_1.start()
    time.sleep(2)
    print("------------------------------------------")
    vehicle_1.status()
    time.sleep(2)
    print("------------------------------------------")
    vehicle_1.stop()
    time.sleep(2)
    print("------------------------------------------")
    vehicle_1.status()

















































































'''class Bus(Vehicle):
    # Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
    def seating_capacity(self, capacity = 50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

bus = Bus("School Volvo", 180, 12)
print(bus)'''