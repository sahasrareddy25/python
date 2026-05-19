"""#revising each and every topic in python as scheduled
#1.variables
#storing the data in container, here container is nothing but a variable. varaible stores the data
name="saashra"
age=20
details=name,age
print("details:", details)

#python varaible has feature  called updating the data assigned to the variable before 
x=10
x=40
print(x)

#printing multiple varaibles
a,b,c,=1,2,3
print("nums:", a,b,c)

#printing same value to multiple varaibles
x=y=z=100
print("x,y,z:", x,y,z)"""

"""
#Determine if String Halves Are Alike
class Solution:
    def halvesAreAlike(self, s):
        vowels = "aeiouAEIOU"
        mid = len(s) // 2
        return sum(c in vowels for c in s[:mid]) == sum(c in vowels for c in s[mid:])        
        
#Check if All A's Appears Before All B's
class Solution:
    def checkString(self, s):
        return "ba" not in s

#removing duplicates from the list
def duplicates(nums):
    result=[]
    for i in nums:
        if i not in result:
            result.append(i)
    return result
print(duplicates([1,2,3,4,4,5,5,5]))"""

#fibonacci series(n):
def fib(n):
    a=0
    b=1
    for i in range(n):
        print(a, end=" ")
        temp=a+b
        a=b
        b=temp
fib(8)
