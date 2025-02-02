class BankAccount:
    def __init__(self):
        self.balance=int(input("enter the balance amount at the time of initial transaction : "))
        
    def deposit(self):
        self.deposit_amount=int(input("enter the deposit amount : "))
        self.balance=self.balance+self.deposit_amount
        print(f"the balance amount after deposit : {self.balance}")
    
    def withdraw(self):
        self.withdraw_amount=int(input("enter the withdraw amount : "))
        if(self.balance-self.withdraw_amount>=0):
            self.balance=self.balance-self.withdraw_amount
            print(f"the balance amount after deposit : {self.balance}")
        else:
            print("transaction declined due to overdraft with rupees : ",self.withdraw_amount-self.balance)
def main() :
    BA=BankAccount()
    BA.withdraw()
    BA.deposit()
    BA.withdraw()
    
main()