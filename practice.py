"""#1.reverse string
word="Hello Iam Sahasra"
words=word.split()
print(" ".join(words[::-1]))

#2.Count frequency of words
sentence="hello Sashra, currentlu working on the most trending ascept of the technology to gain knowledge"
print(len(sentence.split()))
 
#if counting characters
sentence="hello Sashra, currentlu working on the most trending ascept of the technology to gain knowledge"
print(len(sentence))

#3.Remove Duplicates for list
arr=[1,3,5,3,1,4,5,5,7,9]
result=list(set(arr))
print(result)

#4.Take two numbers as input and print their sum
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
print("sum", a+b)

#5.Take a number as input and print if it is even or odd
num=int(input("enter the number: "))
if num%2:
    print("The number is even")
else:
    print("the number is odd")

#6.Take a string and print its length
str="Sahasra"
print(len(str))

#7.Take a string and print its length without using len() keyword
str=input("enter the string: ")
count=0
for ch in str:
    count+=1
    print("length", count)

#8.Print Numbers from 1 to N
num=int(input("enter num: "))
for i in range(1, num+1):
    print(i)

#9.Given a string, return the character with the highest frequency.
#Freqquency count
str="sahasra"
freq={}
for ch in str:
    if ch not in freq:
        freq[ch]=1
    else:
        freq[ch]+=1
print(freq)"""

#10.Unique elements
#Given a list of integers, remove duplicates while maintaining order.
Array=[1,1,1,2,4,5,6,6,7,7]
result=[]
for x in Array:
    if x not in result:
        result.append(x)
print("after removing duplicates: ", result)

Array=[1,1,2,3,4,5,6,7,7,8,8,9,]
result=[]
for ch in Array:
    if x not in result:
        result.append(x)
print("after removing of duplicates:", result)






