"""Take a string and print its length.
Take a string and print the first and last character.
Take a string and check if it is empty or not.
Take a name and print "Hello, <name>!".
Check if a string contains the word "python".
Take a string and check if it is a palindrome.
Count the number of vowels in a string.
Take two strings and check if they are equal.
Convert a string to uppercase.
Take a string and print it reversed."""

"""#1.Take a string and print its length.
str="sahasra"
print(len(str))

#2.Take a string and print the first and last character.
str="supercalifragilisticexpialidocious"
print(len(str))
print("first character:", str[0])
print("last character:", str[-1])

str=input("enter the character: ")
print("first character:", str[0])
print("last character:", str[-1])

#3.Take a string and check if it is empty or not.
str=input("enter the string: ")
if str== "":
   print("the string is empty")
else:
   print("the string is not empty")

#4.Take a name and print "Hello, <name>!
name="arvind"
print("Hello:",name)

#5.Check if a string contains the word "python"
str=input("enter the string value: ")
if "python" in str:
    print("yes! the string contains python")
else:
    print("nope, the string doesn' t contain python")

#6.Take a string and check if it is a palindrome.
str=input("enter the string value: ")
if str==str[::-1]:
    print("It' s a palindrome")
else:
    print("not a palindrome")

#7.Count the number of vowels in a string.
str=input("enter the string value: ")
count=0
for ch in str:
    if ch in 'aeiouAEIOU':
        count=count+1
print("no of vowels: ", count)

#8.Take two strings and check if they are equal.
str1=input("enter the string value: ")
str2=input("enter the string value: ")
if str1==str2:
    print("both are equal")
else:
    print("not equal")

#9.Convert a string to uppercase.
str="arvind"
print(str.upper())

str="ARVIND"
print(str.lower())"""

#10.Take a string and print it reversed
str=input("enter the string value: ")
print(str[::-1])