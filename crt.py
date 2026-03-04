#printing the even and odd numbers in separate array
arr=[1,2,3,4]
even=[]
odd=[]
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:",even)
print("odd numbers:",odd )

#sum of lst n numbers
numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total = total + num
print(total)



