"""for i in range(5, 6):
    print(i)

for i in range(1,5):
    print("Hello")

#counting apples

for apple in range(1, 6):
    print("This is apple no.s ", apple)

#printing names
for i in range(3):
    print("Sahasra")

#counting before before
for i in range(5, 0, -1):                  #here start at 5 and stop before 0
    print("Starting in", i)


#Print numbers from 1 to 10 using a for loop.
for numbers in range(1,11):
 print(numbers)

#Print your name 5 times using a loop.
for i in range(5):
    print("sahasra ")

#Print numbers in reverse order from 10 to 1.
for i in range(10,0,-1):
    print(i)

#leet code prblm- move zeroes
class Solution(object):
    def moveZeroes(self, nums):
        j = 0 
        for i in range(len(nums)):
            if nums[i] != 0: 
                nums[i], nums[j] = nums[j], nums[i]
                j +=1 


#leetcode-climbing stairs
class Solution(object):
    def climbStairs(self, n):
        if n<= 1:
            return 1
        
        dp = [-1] * (n + 1)
        return self.climbStairsHelper(n, dp)
    
    def climbStairsHelper(self, n, dp):
        if n <= 1:
            return 1
        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.climbStairsHelper(n - 1, dp) + self.climbStairsHelper(n - 2, dp)
        return dp[n]

#leetcode-symmetric tree
class Solution(object):
    def isMirror(self, left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val==right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    
    def isSymmetric(self,root):
        if not root:
            return True
        return self.isMirror(root.left,root.right)"""

"""word = "companies"
count = 1
for letter in word:
    if letter =='i':
        count += 2
print(count)"""

"""for i in range(0,11):
    if i % 2 == 0:
        print(i)"""

"""# Program to reverse a number
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed Number:", rev)

# Program to print Fibonacci series up to N terms
n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Program to check whether a number is prime or not
num = int(input("Enter a number: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")

# Program to print alphabets from A to Z
for ch in range(ord('A'), ord('Z') + 1):
 print(chr(ch), end=" ")

#reverse number
num = 1234
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print(rev)

#count vowels in string
s = "education"
vowels = 0

for ch in s:
    if ch in "aeiouAEIOU":
        vowels += 1

print("Vowels:", vowels)

#sum of all even numbers from 1 to 50
sum_even = 0
for i in range(1, 60):
  if i % 2 == 0:
        sum_even += i
print(sum_even)"""

"""#print all characters in string
s = "Sree Sahasra Reddy"
for characters in s:
    print(characters)

#check whether it is a palindrome or not 
num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if temp == rev:
    print("Palindrome number")
else:
    print("Not Palindrome")

#fibonacci seires
n = int(input("Enter number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b"""

#multiplication numer of a table
n =int(input("Enter number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)





















            


