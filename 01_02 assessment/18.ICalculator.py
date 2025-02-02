from abc import ABC,abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def Add(self):
        pass
    @abstractmethod
    def Sub(self):
        pass
    @abstractmethod
    def Divide(self):
        pass
    @abstractmethod
    def Multiply(self):
        pass

class BasicCalculator(ICalculator):
    def Add(self,a,b):
        return a+b
    def Sub(self,a,b):
        return a-b
    def Multiply(self,a,b):
        return a*b
    def Divide(self,a,b):
        return a/b
def main():    
    BasicCalc=BasicCalculator()
    print("addition : ",BasicCalc.Add(14,6))
    print("substraction : ",BasicCalc.Sub(16,10))
    print("Multiplication : ",BasicCalc.Multiply(2,6))
    print("Division : ",BasicCalc.Divide(100,2))
    
main()