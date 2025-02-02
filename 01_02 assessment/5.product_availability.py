class Product:
    def __init__(self):
        self.product_name="bread"
        self.price=int(input("enter the price of product : "))
        self.stock=int(input("enter the stock available : "))
        
    def check_availability(self,required):
        if self.stock>=required :
            self.total=required*self.price
            return "is available it will costs you", {self.total}
        else:
            return f"the required quantity of {self.product_name} is not available"
def main():        
    product=Product()
    required=int(input("enter the requirement : "))
    print(product.check_availability(required))
    required=int(input("enter the requirement : "))
    print(product.check_availability(required))

main()