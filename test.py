"""#here creating a class and adding attributes
class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
 #created method display()
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("marks:", self.marks)

#creating objects
student1=student("sahasra",20,100)
student2=student("arvind",19,100)

student1.display()
student2.display()"""

#creating a class employee 
class employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary

    def show_details(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)

#creaitng objects
emp1=employee("sahasra", "IT", 50000)
emp2=employee("ujwala", "HR", 400000)

emp1.show_details()
emp2.show_details()
        

