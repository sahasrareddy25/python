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
        """
#Check if All A's Appears Before All B's
class Solution:
    def checkString(self, s):
        return "ba" not in s
