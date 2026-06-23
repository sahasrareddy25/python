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
emp2.show_details()


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
# Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        max_price=0
        min_price=prices[0]
        for price in prices:
            max_price=max(price-min_price,max_price)
            min_price=min(min_price,price)
        return max_price

#number of zig-zag arrays
class Solution:
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        m = r - l + 1
        up = [0] * m
        down = [0] * m
        for i in range(m):
            up[i] = i
            down[i] = m - 1 - i
        for _ in range(3, n + 1):
            prefix = [0] * (m + 1)
            for i in range(m):
                prefix[i + 1] = (prefix[i] + down[i]) % MOD
            suffix = [0] * (m + 1)
            for i in range(m - 1, -1, -1):
                suffix[i] = (suffix[i + 1] + up[i]) % MOD
            new_up = [0] * m
            new_down = [0] * m
            for i in range(m):
                new_up[i] = prefix[i]
                new_down[i] = suffix[i + 1]
            up = new_up
            down = new_down
        ans = 0
        for i in range(m):
            ans = (ans + up[i] + down[i]) % MOD
        return ans
#integer to roman
class Solution(object):
    def intToRoman(self, num):
        value = [1000, 900, 500, 400,
                 100, 90, 50, 40,
                 10, 9, 5, 4, 1]

        symbol = ["M", "CM", "D", "CD",
                  "C", "XC", "L", "XL",
                  "X", "IX", "V", "IV", "I"]

        ans = ""

        for i in range(len(value)):
            while num >= value[i]:
                ans += symbol[i]
                num -= value[i]

        return ans
#jump game II
class Solution:
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps"""
#PERMMUTATIONS
class Solution:
    def permute(self, nums):
        result = []
        def backtrack(path, remaining):
            if not remaining:
                result.append(path)
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        backtrack([], nums)
        return result
