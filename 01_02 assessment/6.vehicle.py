class Vehicle:
    def display_status(self):
        print("vehicle is a base class")
    
class Bike(Vehicle):
    def display_status(self):
        super().display_status()
        print("bike is a child class of Vehicle")

class Car(Vehicle):
    def display_status(self):
        super().display_status()
        print("car is a child class of Vehicle")

class ElectricCar(Car):
    def display_status(self):
        super().display_status()
        print("electric car is a child class of car")
def main():
    bike=Bike()
    EC=ElectricCar()
    bike.display_status()
    EC.display_status()
    
main()