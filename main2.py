#Parent class
class Student( object ):
    def __init__(self,name,admission_number):
        self.name=name
        self.admission_number=admission_number
    def display(self):
        print(self.name)
        print(self.admission_number)
# child class
class Subject(Student):
    def __init_(self,name,admission_number,subject,grade):
        self.subject=subject
        self.grade=grade
        Student.__init__(self,name,admission_number)
a = Subject('Malik',18000,'Chemistry', 10)
a.display()









































































































































































































