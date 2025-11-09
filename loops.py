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

# Program to reverse a number
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed Number:", rev)





            


