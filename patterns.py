#pattern is nothing but printing the different shapes *
"""*
**
***
****"""
n=4
for i in range(1, n+1):
   print("*" * i)

"""
*
**
***
****
*****"""
n=4
for i in range(1, n+1):
    print(" " *(n-1)+ "*" * (2*i-1))

"""
1
22
333
4444
"""
for i in range(1,n+1):
    print(str(i)*i)

"""
A
BB
CCC
DDDD
"""
n=4
for i in range(1,n+1):
    char=chr(64+i)
    print(char*i)


