from abc import ABC,abstractmethod

class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def stop_engine(self):
        pass

class CAR(IVehicle):
    def start_engine(self):
        return "CAR engine is started."
    
    def stop_engine(self):
        return "CAR Engine is stopped"    
class BIKE(IVehicle):
    def start_engine(self):
        return "BIkE engine is started."
        
    def stop_engine(self):
        return "BIKE Engine is stopped"  
        
class TRUCK(IVehicle):
    def start_engine(self):
        return "TRUCK engine is started."
    def stop_engine(self):
        return "TRUCK Engine is stopped"  
def main():    
    bike=BIKE()
    car=CAR()
    truck=TRUCK()

    print(bike.start_engine())
    print(bike.stop_engine())
    print(car.start_engine())
    print(car.stop_engine())
    print(truck.start_engine())
    print(truck.stop_engine())

main()