"""#1.Take an integer input and print its *type*.
a=45
b=4.0
c="sahasra"
d=("sahithi","ujwala","sonu","ashritha")
e=["sam", "sakshi","swaa"]
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#2.Take a float input and print its *double value*.
a=3.0
print(a * 2)

num=float(input("enter the value: "))
print(num * 2)

#3.Store your *name* in a variable and print its *data type*.
x="SHASRA REDDY PERATI"
print(type(x))

x=str(input("enter the name: "))
print(type(x))


#4.Store True in a variable and check its *data type*.
a=True
print(type(a))

#5.Convert an integer to float and print the result.
a=4
b=float(a)
c=str(a)
print(a,type(a))
print(b,type(b))
print(c,type(c))

#6.Convert a string "100" into an integer and print its *square*.
num="100"
num=int(num)
print(num*num)

#7.Store a decimal number and convert it to an integer.
num=9.0
print(int(num))

#8.Check whether the input is of type str.
num="Sahasra"
print(type(num))

#9.Print the type of 5, 5.0, "5", and True.
print(type(5))
print(type(5.0))
print(type("5"))
print(type(True))

#10.Take two numbers as input and print their *sum* and *type of the result*.
a=10
b=11
print(a+b)
print(type(a+b))

#11.Print length of string
a="Sahasra"
print(len(a))

s=str(input("enter the string: "))
print(len(s))

#12. First and last character
a="sahasra"
print(a[0])
print(a[-1])

text=str(input("enter the string: "))
print(text[4])
print(text[-1])

#13. Convert to uppercase
text="Sahasra"
print(text.upper())

text="SAHASRA"
print(text.lower())

text=str(input("enter the string: "))
print(text.lower())

#14.Count vowels
Text=str(input("enter the string: "))
vowels="aeiou"
count=0
for ch in Text:
    if  ch in vowels:
        count+=1
        print(count)

text=str(input("enter the string: "))
vowels="aeiou"
for ch in text:
    if ch in vowels:
        count+=1
        print(count)

#15. Reverse a string
text="Sahasra"
print(text[::-1])

text=str(input("enter the string: "))
print(text[::-1])

#16.Check empty string
text=str(input("enter the string: "))
if text==" ":
    print("string is empty")
else:
    print("string is not empty")

#17.Concatenate two strings and print the result.
a="hello"
b="sahasra"
print(a+ " " +b)

text1="silence"
text2="please"
print(text1+" " +text2)

#18.Check if a word is a *palindrome*.
word="waaaaw"
print(word[::-1])"""

text = input("Enter the string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")






