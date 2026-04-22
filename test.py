#here creating a class and adding attributes
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
student2.display()

