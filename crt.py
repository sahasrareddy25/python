#printing the even and odd numbers in separate array
arr=[1,2,3,4,5,6,7]
even=[]
odd=[]
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:",even)
print("odd numbers:",odd )



