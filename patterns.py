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

