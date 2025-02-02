from abc import ABC,abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(IShape):
    def __init__(self):
        self.length=int(input("enter the length of the rectangle : "))
        self.width=int(input("enter the width of the rectangle : "))
    
    def calculate_area(self):
        return self.length*self.width

class Circle(IShape):
    def __init__(self):
        self.radius=int(input("enter the radius of the circle : "))
    def calculate_area(self):
        return 3.14*(self.radius**2)
    
def main():    
    rect=Rectangle()
    print(rect.calculate_area())
    cir=Circle()
    print(cir.calculate_area())
    
main()