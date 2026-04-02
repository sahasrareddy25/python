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
print(fahrenheit_to_celsius(50))"""

#evenodd 
def evenOdd(x):
    if (x%2==0):
        return "Even"
    else:
        return "Odd"
print(evenOdd(16))
print(evenOdd(7))


