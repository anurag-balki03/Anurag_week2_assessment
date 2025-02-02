class Person:
    def manage_details(self):
        self.man_name=input("enter the details of manager")
        print(f"{self.man_name} is the manager")
    
class Employee(Person):
    def emp_details(self):
        super().manage_details()
        self.emp_name=input("enter the name of employee")
        print(f"{self.emp_name} is the employee")
    
    def request_leave(self):
        print(f"respected sir {self.man_name}, could you please approve me a leave for two days")            
        
class Manager(Employee):
    def __init__(self):
        super().emp_details()
        super().request_leave()
        
    def approve_leave(self):
        print("leave has been approved for two days")
def main():
    manage=Manager()
    manage.approve_leave()    

main()