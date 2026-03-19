"""#1. Reverse a string.
str="sahasra"
print(str[::-1])

#2.Check whether a string is palindrome.
str="madam"
if str==str[::-1]:
    print("palidrome")
else:
    print("not a palindrome")

#3.Count the number of vowels in a string.
str="a,e,i,o,u"
count=0"""

"""#4.Count uppercase and lowercase letters.
text="sahasra"
print(text.upper())
text="SAHASRA"
print(text.lower())

#5.Find the length of a string without using len()
str="arvindh"
reversed=" "
for i in range(len(str)-1,-1,-1):
    reversed=reversed+str[i]
print(reversed)
      
#6.counting characters
s="asadfg"
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

#7.checking the anagram
s1="listen"
s2="silent"
if sorted(s1)==sorted(s2):
    print("it is anagram")
else:
    print("not an anagram")

#8.removing duplicates from  string
s="asdgfhgjghf"
result=""
for ch in s:
    if ch not in result:
        result+=ch
print(result)"""

"""#slicing string method in the characters
str="am i loking awkward?"
print(str[3:6])          #using the index values for slicing 


#slicing at the starting and alsoo at the end
str="situations went wrong it seems"
print(str[:7])        

str="situations went wrong it seems"
print(str[1:])        """

#by using negative indexing
str="brooo this sucks hard but still yeah thats fine"
print(str[-7:-1])






