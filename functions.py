"""#creating a function
def my_function():         #def is a key word  
  print("Hellooo func")

#calling a func
def my_function():  
  print("Hello func")
my_function()             #single time

#we can call same func multiple times
def my_function():
  print("Hello func")
my_function()
my_function()            #multiple times
my_function()

#converting fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit-32)*5/9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#calling a func
def my_func():
  print("hey there")
my_func()

#using func with parameters
def wish(name):
  print("happy birthday",name)
wish("sahasra")


#return sum
def add(a,b):
    return a+b
res=add(3,5)
print(res)

#even or odd
def even(n):
    return n%2==0
print(even(4))

#square of number
def square(n):
    return n*n
print(square(5))
    

#max of 2 nummbers
def max_num(a,b):
    if a>b:
        return a
    else:
        return b
print(max_num(10,20))


#consecutive 1's not allowed
class Solution:
    def countStrings(self, n):
        if n == 1:
            return 2
        end_with_0 = 1
        end_with_1 = 1
        for _ in range(2, n + 1):
            new_0 = end_with_0 + end_with_1
            new_1 = end_with_0
            end_with_0 = new_0
            end_with_1 = new_1
        return end_with_0 + end_with_1  


#palindrome check
def is_palindrome(str):
    return str==str[::-1]
print(is_palindrome("mmaaddaamm"))

#prime number or not
def is_prime(num):
    if num>1:
        return True
    else:
        return False
print(is_prime(7))


#second largest number
def second_largest(lst):
    lst=list(set(lst))
    lst.sort()
    return lst[-2]
print(second_largest([1,2,3,4,5,6,8]))

#vowel count
def count_vowels(s):
    count=0
    vowels="aeiouAEIOU"
    for ch in s:
        if ch in vowels:
            count+= 1
    return count
print(count_vowels("hello"))

#combing everything
def add(a,b):
    result=a+b
    print(result)
add(5,3)

#checking even or odd
def even(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
print(even(7))

#maximum number of 3 numbers
def max(a,b,c):
    if a>=b & a>=c:
        return a
    elif b>=a & b>=c:
        return b
    else:
        return c
print(max(10,25,15))"""

#factorial number
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
print(factorial(5))