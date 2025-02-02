class Animal:
    def speak(self):
        print("animal is the parent class.")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("DOG : BARK")

class Cat(Animal):
    def speak(self):
        super().speak()
        print("CAT : MEOW")
        
def main():
    DOG=Dog()
    CAT=Cat()
    DOG.speak()
    CAT.speak()

main()