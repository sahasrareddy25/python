"""#variable basics
name="sahasra"
age="20"
marks="89.5"
print(f"My name is {name},I am {20} years old, and I sccored {89.5}% marks.")

#mutable vs immutable
my_list=[1,2,3]
print("before:",my_list)
my_list.append(4)
print("after:", my_list)
my_str="Hello"
print("original string:",my_str)
new_str="h" + my_str[1:]
print("modified string:",new_str)

#multiple assignments
a,b,c=10,20,30
print("sum =",a+b+c)

#Type casting(str to int)
s="10"  
n=int(s)  
cnt=5
f=float(cnt)  
age=25
s2=str(age)  

#implict type casting
a=10
b=2.5
c=a+b
print("result=",c)
print("type of result:", type(c))

#mutable vs immutable
my_list=[1,2,3]
print("before:",my_list)
my_list.append(4)
print("after:", my_list)
my_str="Hello"
print("original string:",my_str)
new_str="h" + my_str[1:]
print("modified string:",new_str)

#declare two integer variables and point their sum 
a=10
b=20
sum_result=a+b 
print("the sum of", a,"and", b,"is:",sum_result)

#Assign multiple values to multiple variables in one line and print them
a,b,c=10,20,30
print("a=",a)
print("b=",b)
print("c=",c)

#Store a number in a variable and print its square using that variable
num=5
square=num**2
print("the square of", num,"is", square)

#Concatenate two string variables and print the result
str1="hello"
str2="gud morning!"
result=str1+" " +str2
print(result)

#swapping
x=5
y=10
print("before swapping:", x,y)
x,y=y,x
print("after swapping:",x,y)

#global variable 
msg="helloo"
def display():
    print("Inside function:", msg)
display()
print("Outside function:", msg)

#Svariable
s="sahasra"
print(s)

#MVariables
M="sahasra"
age=20
city="warangal"
print(M,age,city)

#3inputs
x,y,z=input("Enter three values:").split()
print("Total number of students:",x)
print("Number of boys is:",y)
print("Number of girls is:",z)

#CU input
age=int(input("Enter your age:"))
if age>=18:
 print("Eligible")
else:
 print("Not Eligible")

# converting integer to string
x=10          
y=str(x)      
print(x,type(x))
print(y,type(y))

#converting to integer
a="50"        
b=int(a)      
print(a,type(a))
print(b,type(b))


#Store your name in a variable and print it
name= "sahasra"
print("the name is ", name)

#Store two numbers in variables and print their sum
a=10
b=20
print("the sum of ", a+b)

#Store length and width, print area of rectangle
length=10
width=5
area=length*width
print("area of the rectangle", area)

#Store a number and print its square
num=5
square=num*num
print("square: ", square)

#Store three subject marks and print total & average
math=100
phy=99
chem=90
total=math+phy+chem
average=math+phy+chem/3
print("total:" , total)
print("average: " ,average)

#Convert Celsius to Fahrenheit
c=10
f=(c*9/5)+32
print("fahrenheit:", f)

#Swap two variables
a=5
b=25
a,b =b,a
print("a=", a)
print("b=",b)

#Store a sentence and print number of characters
sentence="mental health"
print("number of characters: ", len(sentence))

#Store price & quantity and print total cost
price=1000
quantity=5
total=price*quantity
print("total cost:", total)

#Store two numbers and print the larger one
x=10
y=15
if x>y:
    print("larger number: ", x)
else:
    print("larger number:", y)

#Store a number and check if it is even or odd
num=9
if num%2 == 0:
    print("even")
else:
    print("odd")

#Store three numbers and print the maximum
a=10
b=20
c=30
maximum=max(a,b,c)
print("maximum number is: ", maximum)

#Store year and check if it is a leap year
year=2025
if(year%400==0) or (year%4==0 and year%100!=0):
   print("leap year")
else:
   print("not a leap")

#Store principal, time, rate → calculate simple interest
p=100
T=2
R=5
SI=(p*T*R)/100
print("simple intrest:", SI)




age=20
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")
  
num=16
if num & 1==0:
    print("even")
else:
    print("odd")

#counting vowels
text="education"
vowels="aeiou"
count=0
for char in text:
    if char in vowels:
        count+=1
print("count:", count)

#counting vowels
text="education"
vowels="aeiou"
count=0
for char in text:
    if char in vowels:
        count+=1
print("count:", count)

num = 25
print(num > 10 and num < 50)

ch="e"
print(ch== "a" or ch=="e" or ch=="i" or ch=="o" or  ch=="u")


# Counting Characters in a String
word="Dhurandhar"
length=len(word)
print("length of the word:", length)


#Create a variable and print its value.
x=10
print(x)

#Store your name in a variable and print
x="sahasra"
print(x) 

#Create two variables and print their sum.
x=10
y=15
z=x+y
print(z)

#Store a number in a variable and print its square.
x=10 
square=x*x
print("square:",square)

#Create a variable price and print
price=250
print("price: ", price)

#Assign the same value 100 to three variables in one line
a = b = c = 100
print(a, b, c)

#Swap two variables using a temporary variable.
a=10
b=15
a,b=b,a
print(a,b)

#Swap two variables without using a temporary variable
a=10
b=15
a,b=b,a
print("a: ", a)
print("b: ", b)

#Store your age and print whether it is greater than 18.
age=20
if age>=18:
    print("is greater than 18")

#Create a variable and check its data type.
x=10
print(type(x))

x="sahasra"
print(type(x))

x=0.5
print(type(x))

#Take a number as input and store it in a variable. Print it
num=int(input("enter the number: "))
print("num: ", num)

#Take two numbers as input and print their sum.
x=int(input("enter the first number: "))
y=int(input("enter the second number: "))
print(x+y)

x=10
y=20
print(x+y)

#Take a name as input and print
name="sahasra"
print("name: ",name)


#Take two numbers and print difference, product, and division
x=10
y=15
print(x*y)
print(x-y)
print(x%y)

#Create a variable a and assign value 10. Print it
a=10
print("a: ", a)

#Take length and breadth as variables and calculate area of rectangle
length=4
breadth=6
print(1/2*breadth)


#Take a number and print its double and triple
a=35
print(a*2, a*3)


#take radius as input and calculate area of circle
r=float(input("enter the radius: "))
print(3.14 * r * r)


#Take salary and bonus, then calculate total salary.
salary=1000
bonus=500
total_Salary=salary+bonus
print("total_Salary: ", total_Salary)

#Take marks of a student and print them in a sentence.
student_marks= int(input("enter the student's marks: "))
print("student_marks: ",student_marks)

#1.Store a number and display it
x=10
y=20
print(x*y)

#2. Store two numbers and find their sum
a=256
b=678
print(a+b)

#3. Store two numbers and find the difference
x=10
y=20
print(x-y)

#4.Store two numbers and find the product
x=10
y=20
print(x*y)

#5. Store two numbers and find the quotient
x=10
y=20
print(x%y)

#6.Store your name and age and display them
name="sahasra"
age=20
print("name:", name)
print("age:", age)

#7.Swap two variables
x=20
y=30
x,y=y,x
print(x,y)

#8. Store length and breadth of a rectangle and find area
length=500
breadth=550
print(length*breadth)

#9. Store radius of a circle and find area
radius=45
print(3.14*45*45)

#10.Store marks of three subjects and find average
math=100
fam=99
chem=90
print("math,fam,chem:", math,fam,chem)
 
#11.Store price and quantity and find total cost
price=345678
quality=890
cost=price*quality
print("cost:", cost)"""

"""#26/12-just solving problems given by chatgpt
#1.Store your name in a variable and print it.
x="saashra"
print(x)

#2.Store your age in a variable and print it.
x=20
print(x)

#3.Store two numbers in two variables and print their sum.
x=10
y=20
print(x+y)"""

#4.Store two numbers and print their difference.
x=20
y=30
print(x-y)



























