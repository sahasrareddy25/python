"""#parent class- Employee-method, child class developer-method- create obj for developer class 
#with the help of it access the parent class method
class Employee:
    def show_employee(self):
        print("Employee class method")
class Developer(Employee):
    def show_developer(self):
        print("Developer class method")
d=Developer()
d.show_developer()
d.show_employee()


#parent method in child.
class animal:
    def sound(Self):
        print("animal make sounds")

class dog(animal):
    def sound(self):
        print("dog barks")
d=dog()
d.sound()


#multilevel inheritance
class a:
    def showa(self):
        print("Class a")
class b(a):
    def showb(self):
        print("Class b")
class c(b):
    def showc(self):
        print("Class c")
obj = c()
obj.showa()
obj.showb()
obj.showc()

#multiple inheritance
class father:
    def skills(self):
        print("Gardening")
class mother:
    def skills(self):
        print("Cooking")
class Child(father, mother):
    def skills(self):
        super().skills()
        print("Coding")
c=Child()
c.skills()

#hierarchical inheritance
class Vehicle:
    def start(self):
        print("Vehicle")
class Car(Vehicle):
    def drive(self):
        print("drives")
class Bike(Vehicle):
    def ride(self):
        print("rides")
c=Car()
b=Bike()
c.start()
b.start()"""