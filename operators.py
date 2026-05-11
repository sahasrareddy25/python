"""#A.operators in python
a=25
b=30
print("a+b=",a+b)
print("a-b",a-b)
print("a*b",a*b)
print("a/b",a/b)
print("a//b",a//b)
print("a%b",a%b)
print("a**b",a**b)

#calculating intrest   # based on formula
p=10000
r=2
t=5
intrest=(p*r*t)/100
print("intrest:",intrest)

#L.operators
age=int(input("Enter your age:"))
if age>=18:
 print("Eligible to vote")
else:
 print("Not eligible")


#c.operators
a=10
b=14
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

#B.operators
a=10
b=4
print(a&b)
print(a|b)
print(~a)
print(a^b)
print(a>>2)
print(a<<2)

#A.operator
a=10
b=a
print(b)
b+=a
print(b)
b-=a
print(b)
b*=a
print(b)
b<<=a
print(b)

# comparison_operators.py

# Program to demonstrate comparison operators
a = 100
b = 52
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

#l.operator
age=23
citizen=True
if age>= 20 and citizen:
  print("Eligible voting")
else:
  print("Not eligible for Voting")


#shopping price
price=2022
quantity=10
discount=10
totalprice=price*quantity-discount
print("totalprice:",totalprice)

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

#removing a stars from strings
class Solution:
    def removeStars(self, s):
        stack = []
        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)  
        return ''.join(stack)

 class Solution:
    def numDifferentIntegers(self, word):
        num = ""
        s = set()
        for ch in word:
            if ch.isdigit():
                num += ch
            else:
                if num:
                    s.add(int(num))
                    num = ""
        if num:
            s.add(int(num))
        return len(s)

"""
#count subarrays of length three with a condition
class Solution(object):
    def countSubarrays(self, nums):
        count=0
        n=len(nums)
        for i in range(n-2):
            if 2*(nums[i]+nums[i+2])==nums[i+1]:
                count += 1
        return count