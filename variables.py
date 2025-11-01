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
 print("Not Eligible")"""

# converting integer to string
x=10          
y=str(x)      
print(x,type(x))
print(y,type(y))


