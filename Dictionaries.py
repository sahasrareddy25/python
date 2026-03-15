#In data structures stroing the data in key value pair 

"""#1.store the student details and print name of the student
student={
    "name": "Saashra",
    "age": "20",
    "branch": "cse"
}
print(student['name'])

#2.counting the frequenccy
nums=[1,2,3,4,4,4,4]
freq={}
for i in nums:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

#3.creating and accessing the dictionary
student={"name":"arvind",
         "Age":20,
         "city":"Wgl",
         }
print(student["Age"])

#4.Adding new keys to the dictionary
student={"name":"arvind",
         "Age":20}
student["college"]="MRU"
print(student)"""

#5.Updating the previously given values
student={"name":"Arvind",
         "Age":20,
}
student["Age"]=21
print(student)