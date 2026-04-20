"""#multiple level inheritance
class Animal:
    def shout(self):
        print("animal is shouting")

class Dog(Animal):
    def make_sound(self):
        print("bow")

class Cat(Animal):
    def make_sound(self):
        print("meow")

dog = Dog()
cat = Cat()

dog.shout()        
dog.make_sound()  

cat.shout()        
cat.make_sound()   


#itialise a parent class as Employee-constructor with parameter name, child class as Developer - constructor with parameter prog_lang, user super()
class Employee:
    def __init__(self,name):
        self.name = name

class Developer(Employee):
    def __init__(self,name,fullname):
        super().__init__(name)
        self.fullname = fullname

d = Developer("saam","jain")
print(d.name)
print(d.fullname)

#multiple inheritance
class Father:
    def skills_father(self):
        print("Gardening")

class Mother:
    def skills_mother(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills_father()
c.skills_mother()


#single  inheritance
class Person:                   
    def display(self):
        print("I am a person")

class Student(Person):
    def study(self):
        print("I am studying")

s = Student()
s.display()
s.study()


#create a cls of animal and add sounds 
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
d = Dog()
d.sound()

#create a multi level inheritance usinf grandparent clss
class Grandparent:
    def show_grandparent(self):
        print("I am Grandparent")
class Parent(Grandparent):
    def show_parent(self):
        print("I am Parent")
class Child(Parent):
    def show_child(self):
        print("I am Child")
c = Child()
c.show_grandparent()
c.show_parent()
c.show_child()

#create a multi level inheritance using father as a method 
class Father:
    def skills(self):
        print("confidence")
class Mother:
    def talent(self):
        print("politician")
class Child(Father, Mother):
    pass
c = Child()
c.skills()
c.talent()

#use a costructor keey word and that child class automatically calls parent constructor.
class A:
    def __init__(self):
        print("Constructor A")
class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor B")
b = B()

#calling a parent method
class Employee:
    def work(self):
        print("Employee works")
class Developer(Employee):
    def work(self):
        super().work()
        print("Developer codes")
d = Developer()
d.work()

#understanding the method which has been called 
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
class D(B, C):
    pass
d = D()
d.show()

#create a class student and object
class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)

s1 = Student("sahasra",90)
s2 = Student("sita",80)

s1.display()
s2.display()

#using constructor create a employee detail adding name ,salary
class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def show_details(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

e= Employee("sahasra", 50000)
e.show_details()

#using inheritance add self constructor and take vehicle as example and add object
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

c=Car()
c.start()
c.drive()"""

#polymorphism
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d=Dog()
c=Cat()

d.sound()
c.sound()
