#pattern is nothing but printing the different shapes *
"""*
**
***
****"""
n=4                            #rows
for i in range(1, n+1):        #col   
   print("*" * i)

"""
*
**
***
****
*****"""
n=4
for i in range(1, n+1):                 #i controls rows  #*=i
    print(" " *(n-1)+ "*" * (2*i-1))

"""
1
22
333
4444
"""
for i in range(1,n+1):      #rows,columns print statement-3
    print(str(i)*i)

"""
A
BB
CCC
DDDD
"""
n=4
for i in range(1,n+1):
    char=chr(64+i)    #chr() built-in function to cnvrt num to char
    print(char*i)      #64 is the value pf ASCII Values that has a num to every char


