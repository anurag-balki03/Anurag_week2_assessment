class car:
    def move(self,mini : int)->int:
        self.max_speed=mini
        print(f"car moves on land with a maximum speed of {self.max_speed}")

class aeroplane:
    def move(self, brand : str)->str:
        self.brand=brand
        print(f"{self.brand} i an aeroplane will fly upto 3000 mts above the sea level")

class flyingcar(car,aeroplane):
    def move(self):
        car.move(self,200)
        aeroplane.move(self,"indigo")
        print("flyingcars can both move on road and can fly in the air") 
        
def main():
    FC=flyingcar()
    FC.move()      

main()