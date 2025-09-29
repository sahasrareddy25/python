#variable basics
#assign name,age,percentage marks to three different variables.print them using f-string
name="sahasra"
age="20"
marks="89.5"
print(f" My name is {name}, I am {20} years old, and I sccored {89.5}% marks.")

#multiple assignments
#Assign values 10,20,30 to three variables a ,b,c in a single line.print the sum
a,b,c=10,20,30
print("sum =",a+b+c)

#Type casting(str to int)
#Take input from the user as a string number.convert it into an integer and multiply it by 2
num_str=input("Enter a number: ")
num_int=int(num_str)
print("result=",num_int*2) 

#implicit type casting
#show how python automatically converts types.add an integer and a float
a=10
b=2.5
c=a+b
print("result=",c)
print("type of result:", type(c))

#mutable vs immutable
#create a list and a string.modify the list and try to modify the string
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
print("after swapping:", x,y)