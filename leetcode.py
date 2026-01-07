"""#reverse number
num = 1234
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print(rev)

#-symmetric tree
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
        return self.isMirror(root.left,root.right)
    
    
#climbing stairs
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
    
#move zeroes
class Solution(object):
    def moveZeroes(self, nums):
        j = 0 
        for i in range(len(nums)):
            if nums[i] != 0: 
                nums[i], nums[j] = nums[j], nums[i]
                j +=1 

#length of last word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

#shortest palindrome
class Solution:
    def shortestPalindrome(self, s):
        for i in range(len(s), -1, -1):
            if s[:i] == s[:i][::-1]:
                return s[i:][::-1] + s """

#happy number
class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1:
            if n in seen:  
                return False
            seen.add(n)
            res = 0
            while n > 0:
                rem = n % 10
                res += rem * rem
                n //= 10
            n = res
        return True

