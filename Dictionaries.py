#In data structures stroing the data in key value pair 

#1.store the student details and print name of the student
student={
    "name": "Saashra",
    "age": "20",
    "branch": "cse"
}
print(student['name'])

#2.counting the frequenccy
nums=[1,2,3,3,4,4,5,6,6,6]
freq={}
for i in nums:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)