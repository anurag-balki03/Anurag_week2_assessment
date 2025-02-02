class shape:
    def SHAPE(self, shape):
        self.shape=shape
    def area(self):
        print(f"the area of {self.shape}")

class square(shape):
    def SHAPE(self):
        super().SHAPE("square")
    def area(self):
        self.side=int(input("enter the side of a square : "))
        super().area()
        print(self.side**2)
        
class triangle(shape):
    def SHAPE(self):
        super().SHAPE("triangle")
    def area(self):
        self.base=int(input("enter the base of a triangle : "))
        self.height=int(input("enter the height of the triangle : "))
        super().area()
        print(0.5*self.base*self.height)

squ=square()
tri=triangle()
squ.SHAPE()
tri.SHAPE()
squ.area()
tri.area()  