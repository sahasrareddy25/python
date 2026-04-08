"""#method overidding
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# objects
a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()


#using loopS
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

#payment system
class Payment:
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")

class NetBanking(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Net Banking")
payments = [CreditCard(), UPI(), NetBanking()]
for p in payments:
    p.pay(1000)"""


#example problem
class Student:
    def role(self):
        print("I am a student")

class Teacher:
    def role(self):
        print("I am a teacher")

people = [Student(), Teacher()]

for p in people:
    p.role()