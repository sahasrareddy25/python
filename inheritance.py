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
s.study()"""


#create a cls of animal and add sounds 
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
d = Dog()
d.sound()