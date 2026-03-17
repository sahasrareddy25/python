"""#1.creating a set 
nums={1,2,3,4,5,5,6,7}
print(nums)     #here it remove the duplicate values

#2.addding a element to a set
nums={1,2,3,4}
nums.add(25)
print(nums)

#3.removing an element
nums={1,2,3,4,5,6}
nums.remove(6)
print(nums)

#4.union 
#convert a list into set
nums=[1,2,3,4,5,6]
print(set(nums))

#find a commmon digits between 2 lists
a=[1,2,3,4]
b=[1,2,5,7]
set1=set(a)
set2=set(b)
common=set1&set2
print(common)

of two sets
a={1,2,3,4}
b={5,6,7,8,9}
res=a.union(b)
print(res)

#5.intersection
a={1,2,3,4}
b={5,6,7,8,9}
res=a.intersection(b)
print(res)

#6.differnce
a={1,2,3,4}
b={5,6,7,8,9}
res=a.difference(b)
print(res)"""

#7.finding the unique element
nums=[1,2,3,4,5]
unique=[]
for i in nums:
    if nums.count(i)==1:
        unique.append(i)
print(unique)