class Employee:
    def __init__(self):
        self.emp_name=input("enter the name of the employee: ")
        self.id=input("enter the employee id of the employee: ")
        self.department=input("enter the department of the employee: ")
    
    def display_details(self):
        print(f"name : {self.emp_name}""\n"f"employee ID : {self.id}""\n"f"department : {self.department}")

empp=Employee()
empp.display_details()