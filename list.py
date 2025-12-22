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
    print("doesn't existed")"""

#8.Copy a list and modify it
old_list=[1,2,3,4]
new_list=list(old_list)
new_list.append(20)
print("old_list:", old_list)
print("new_list:",new_list)


original_list=[1,2,34,5,6]
new_list=list(original_list)
new_list.append(2)
print("original_list:",original_list)
print("new_list:",new_list)




