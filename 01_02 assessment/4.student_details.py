class Student:
    def __init__(self,name,roll_number):
        self.student_name=name
        self.Roll_number=roll_number
    
    def Display_Student(self):
        print(f"name of the student : {self.student_name}")
        print(f"Roll NUmber of student : {self.Roll_number}")
        
def main():
    student=Student("anurag",6629)
    student.Display_Student()
    
main()