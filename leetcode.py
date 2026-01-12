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
                return s[i:][::-1] + s 

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

#length of the longest substring
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        :type s: str
        :rtype: int
        
        n = len(s)
        res = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    res = max(res, j - i + 1)
        return res

#count and say
class Solution:
    def countAndSay(self, n):
        s = "1"
        for _ in range(n - 1):
            result = ""
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                result += str(count) + s[i]
                i += 1
            s = result
        return s"""

#two sum
class solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]



        
        


