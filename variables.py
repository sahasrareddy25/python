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