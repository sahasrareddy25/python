#initialise a parent class as Employee-constructor with parameter name, child class as Developer - constructor with parameter prog_lang, user super()
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