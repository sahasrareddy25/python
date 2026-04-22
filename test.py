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
student2.display()

#


#creating a parent class 
# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child class (inherits from Person)
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)   
        self.marks = marks

    def display(self):
        super().display()            
        print("Marks:", self.marks)
    
# Create object
student1=Student("Sahasra", 20, 95)

#printing details
s1.display()

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
emp2.show_details()"""


#creating a vehicle as a class name 
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick")

c = Car()
b = Bike()

c.start()
b.start()