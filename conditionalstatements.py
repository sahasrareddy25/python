"""#if condition 
x=10
if x>5:
 print("x is greater than 5")

x=22
if x<2:
  print("x is less than 2")"""

"""age=20
if age>=18:
 print("Eligible to vote")"""

"""age=16
if age<18:
 print("are minors")

#here 0's can't be used as condition and it is false
if 0:
  print("")

wish="helloo"
print("helloo")

a=5
b=20
if a<b:
 print("a is greater than b")"""

"""total_marks=100
pass_mark=35
if total_marks>=pass_mark:
  print("student has passed")

total_purchase=1000
if total_purchase>700:
  print("customer gets 30% discount")

phone_battery=100
if phone_battery>20:
    print("phone battery is below")

marks=100
if marks >=90:
 print("grade: A")
if marks >=70:
 print("grade: c")
if marks>=50:
 print("grade: e")"""
 
 
#10.10.2025

"""#Positive or Negative
if 5 > 0:
  print("number is positive")
if -5 < 0:
  print("number is negative")
if 0 == 0:
 print("number is zero")

#Even or odd
number=5
if number % 2==0:
 print("numnber is even")
if number % 7!=0:
 print("number is odd")
if number % 4==0:
 print("number is divisible by 4")


#voting eligibility
age=20
if age>=18:
 print("eligible to vote")
if age<18:
 print("not eligible to vote")
if age==18:
 print("eiligible for first time voting")

#largest of two numbers
a=10
b=20
if a>b:
  print("a is greater")
if b>a:
 print("b is greater")
if a==b:
 print("both are equal")

#multiple of 5
number=15
if number % 5==0:
  print("number is multiple of 5")
if number % 5!=0:
 print("number is not multiple of 5")  

#grade calculation
marks=85
if marks>=90:
  print("grade A")
if marks>=75:
 print("grade B")
if marks>=60:
 print("grade c")
if marks<60:
 print("grade D")

#smallest of three numbers 
a=10
b=20
c=40
if a<b and a<c:
 print("a is smallest")
if b<a and b<c:
 print("b is smallest")
if c<a and c<b:
 print("c is smallest")"""

#11.10.2025

"""#elif statements
age=25
if age<=12:
  print("Child.")
elif age<=19:
  print("Teenager.")
elif age<=35:
  print("Young adult.")
else:
  print("Adult.")

#marks & grades
int_marks=int(input("Enter your marks: "))
if int_marks>=90:
  print("Grade A")
elif int_marks>=75:
  print("Grade B")
elif int_marks>=50:
  print("Grade C")
else:
  int_marks<50
  print("Garde D")

#voting eligibility
age=int(input("enter your age:"))
if age>=18:
  print("you're eligible to vote")
elif age<18:
  print("you're not eligible to vote")
else:
  age==18
  print("you're eligible for first time voting")"""

"""#enter a number from 1 to 7

day = int(input("Enter a number (1-7): "))
if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")
else:
  print("Invalid input!")"""

"""#Find the largest number
a=int(input("Enter first number: "))
b=int(input("Enter second number:"))
c=int(input("Enter third number: "))
if a>=b and a>=c:
    print(a is largest number)
elif b>a and b>=c:
    print(b is largest number)
else:
    print(c is largest number)"""

"""#find the largest number
a=30
b=10
c=20
if a>b and c<a:
 print("a is the largest number")
elif b>c and b>a:
 print("b is the largest number")
else:
   print("c is the largest number")

#check grade
marks=int(input("enter marks:"))
if marks>=90:
  print("grade A")
if mark>=75:
  print("grade B")
if  marks>=50:
  print("grade c")
  if marks<50:
    print("grade D")
else:
    print("fail")"""

"""#day of week
day=int(input("enter a number"))
if day==1:
  print("monday")
elif day==2:
  print("tuesday")
elif day==3:
  print("wednesday")
elif day==4:
  print("thursday")
elif day==5:
  print("friday")
elif day==6:
  print("saturday")
elif day==7:
  print("sunday")

#temperature check
temp=int(input("enter temperature:"))
if temp>30:
  print("temperature is hot")
elif temp>20:
  print("temperature is warm")
elif temp>10:
  print("temperature is cool")
else:
  print("temperature is cold")

#14.10.2025
#if-else
#pass or fail
student_marks=int(input("enter numbers: "))
if student_marks>=100:
    print("you passed! congratulations ")
if student_marks>=70:
    print("congratulations")
elif student_marks<=50:
     print("Unfortunately, you failed!")

#odd or even
number=int(input("enter a number: "))
if number % 2==0:
    print("the number is even")

#positive or negative
num=int(input("enter the number: "))
if num>2:
    print("the number is positive")
elif num<0:
    print("the number is negative")
else:
    print("zero")

#multichoice if-else
#grading system
student_score=int(input("enter the number: "))
if student_score>90:
    print("grade A")
elif student_score>80:
    print("grade B")
elif student_score>70:
    print("grade c")
elif student_score>60:
    print("grade D")

elif student_score<60:
    print("fail")"""

#ticket price calculator
age=int(input("enter the number: "))
if age<5:
    print("ticket price is $0")
elif age<=13:
    print("ticket price for child is $20 ")
elif age<=64:
    print("ticket price for adult is $20")
elif age<100:
    print("ticket price is $15")



