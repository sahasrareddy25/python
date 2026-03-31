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
d.show_employee()"""


#parent method in child.
class animal:
    def sound(Self):
        print("animal make sounds")

class dog(animal):
    def sound(self):
        print("dog barks")
d=dog()
d.sound()
