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
print(freq)

#10.Unique elements
#Given a list of integers, remove duplicates while maintaining order.
Array=[1,1,1,2,4,5,6,6,7,7]
result=[]
for x in Array:
    if x not in result:
        result.append(x)
print("after removing duplicates: ", result)

#11.Check positive / negative / zero
num=int(input("Enter the number: "))
if num>0:
    print("positive numbers")
elif num<0:
    print("negative number")
else:
    print("zero")"""

"""#1.Reverse a String
s="saashra"
print(s[::-1])
#2.Check Palindrome
str="aassfssaa"
if str==str[::-1]:
    print(True)
else:
    print(False)
    
#3.Find Largest Number in a List
nums=[1,2,3,4,5]
largest_number=max(nums)
print(largest_number)

#4.Count Vowels in a String
str=input("enter the string: ")
vowels='aeiou'
count=0
for char in str:
    if char in vowels:
        count+=1
print(count)
#5.Find Factorial of a Number
num=5
factorial=1
for i in range(1, num+1):
    factorial*=i
print(factorial)
#6.Two Sum Problem
nums=[1,2,3,4,5]
target=6
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j]==target:
            print([i,j])

#8.Second Largest Number in List
nums=[1,2,3,4,5]
nums.sort()
print(nums[-2])

#9.Count Frequency of Characters
str="saashra"
freq={}
for char in str:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)

#sort the people
class Solution(object):
    def sortPeople(self, names, heights):
        x=sorted(heights)[::-1]
        a=[]
        for i in x:
            a.append(names[heights.index(i)])
        return a
"""
"""
developer = 'Jessica'
greeting = f'My name is {developer}.'
print(greeting) 


#
my_str = 'Hello world'
print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

#** prints
int_1 = 4
int_2 = 2
print(int_1 ** int_2)

#dictnries usage
example_list = ['example', 'dashed', 'name']
joined_str = ' '.join(example_list)
print(joined_str) 

#
message = 'Python is fun!'
print(message[0:6])"""

#usage of enumerate() func and printing the product details below in a order with the sno.
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
for product in enumerate(products):
    print(product)
"""
#assigning same value to multiple variables
var_1 = var_2 = var_3 = 182  
print("Variable 1:", var_1)  
print("Variable 2:", var_2)  
print("Variable 3:", var_3)  """