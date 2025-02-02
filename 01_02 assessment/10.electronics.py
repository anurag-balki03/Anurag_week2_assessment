class ElectronicDevice:
    def Brand(self,brand):
        self.brand=brand
        
    def functioning(self):
        print(f"{self.brand} has good market in electric goods")

class MobileDevices(ElectronicDevice):
    def Brand(self,brand):
        self.brand1=brand
        super().Brand("Mobiles")
        
    def functioning(self):
        super().functioning()
        print(f"{self.brand1} is a smartphone it gives the compactability")

class SmartPhones(MobileDevices):
    def Brand(self,brand):
        self.brand2=brand
        super().Brand("android")
        
    def functioning(self):
        super().functioning()
        print(f"{self.brand2} is the best available smartphone in the market")
        
def main():        
    smart = SmartPhones()
    smart.Brand("samsung")
    smart.functioning()
    
main()