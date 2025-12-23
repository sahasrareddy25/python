"""thislist=["mallareddy"]
print(thislist)

#duplicate values
list=["a","a","b","c","c"]
print(list)

#removed specified item using remove() functionc
thislist=["1","3","3","4","4"]
thislist.remove("1")
print(thislist)

thislist=["sahasra","rishitha","ashritha","aravind"]
thislist.pop(1)
print(thislist)

#use square brackets [] to create a list directly. #using square brackets
a=["ujwala","arvind","ashritha"]
b=["sam","jatayu","Ai"]
c=[1,3.4,'wars', True]
print(a,b,c)

#1.Convert a string into a list
text="sahasra"
print(list(text))

#2.Convert a tuple into a list
t=(1,2,3,4,5)
print(list(t))

#3.Convert a list into another list
thislist=["saas","siri","sonu"]
print(list(thislist))

#4.Find the length of a list created from a string
string="education"
print(list(string))
print(len(string))

#5.Count vowels using list()
text="saashra"
chars=list(text)
count=0
vowels="aeiou"
for ch in chars:
    if ch in vowels:
        count+=1
print("vowels count:", count)

#6.Convert numbers string into list of characters
string="123456"
chars=list(string)
print(chars)

#7.Check whether a character exists
string="saashra"
if 'a' in string:
    print("character 'a' exists")
else:
    print("doesn't existed")

#8.Copy a list and modify it
old_list=[1,2,3,4]
new_list=list(old_list)
new_list.append(20)
print("old_list:", old_list)
print("new_list:",new_list)

#9.Reverse using list
string="saashra"
print(list(string))
print(string[::-1])

#10.Separate characters and digits
string="asd2345df"
chars=list(string)
for ch in chars:
    if ch.isdigit():
        print(ch)

#10.Convert the string "computer" into a list and print it.
string="computer"
print(list(string))

#11.Convert the tuple (5, 15, 25, 35) into a list.
t=(5,15,25,35)
char_list=list(t)
print(char_list)

#12.Take a string input from the user and convert it into a list.
string_input="saashra"
char_list=list(string_input)
print(char_list)

#13.Convert a list [2, 4, 6] into another list using list() and print both.
text=[1,23,4,45,4]
char_list=list(text)
print(text)
print(char_list)"""

#14.Convert the string "hello world" into a list and count how many spaces are present.
text="helloworld"
char_list=list(text)
space_count=0
if char_list in char_list:
    if char_list=" ":
      space_count+=1
      print("number of spaces:", space_count)



