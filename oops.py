#parent class- Employee-method, child class developer-method- create obj for developer class 
#with the help of it access the parent class method
class Employee:
    def show_employee(self):
        print("Employee class method")
class Developer(Employee):
    def show_developer(self):
        print("Developer class method")
dev=Developer()
dev.show_developer()
dev.show_employee()