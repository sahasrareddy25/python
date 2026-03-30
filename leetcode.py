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
        return s

#two sum
class solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]

#Number of island
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"  # mark visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count

#grey code
class Solution(object):
    def grayCode(self, n):
        
        :type n: int
        :rtype: List[int]
        
        result = []
        total_numbers = 1 << n

        for i in range(total_numbers):
            result.append(i ^ (i >> 1))

        return result

#countAndsay
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
        return s

#two sum
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]

#Gas station problem
class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        current_tank = 0
        
        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]
            
            if current_tank < 0:
                start = i + 1
                current_tank = 0
        
        return start


#house robber
class Solution:
    def rob(self, nums):
        rob, skip = 0, 0
        
        for money in nums:
            new_rob = skip + money   # rob current house
            new_skip = max(skip, rob)  # skip current house
            
            rob, skip = new_rob, new_skip
        
        return max(rob, skip)

#palindrome 
class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        rev = ""
        for i in s:
            rev = i + rev
        if (rev==s):
            return True
        else:
            return False

#grey code
class Solution(object):
    def grayCode(self, n):
        result = []
        total_numbers = 1<< n

        for i in range(total_numbers):
            result.append(i ^ (i >> 1))

        return result

#contains duplicate
class solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

#anagram
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())

#house robber
class Solution:
    def rob(self, nums):
        rob, skip = 0, 0
        for money in nums:
            new_rob = skip + money   # rob current house
            new_skip = max(skip, rob)  # skip current house
            
            rob, skip = new_rob, new_skip
        
        return max(rob, skip)

#Two sum
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]

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
        return s

#contains duplicates
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
        
#two sum
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]


#contains dulicates
class solution:
    def containsDuplicates(Self,num):
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==num[i-1]:
               return True
        return False

#Number of 1 bits
class Solution(object):
    def hammingWeight(self, n):
        bits = bin(n)[2:]
        return bits.count("1")  


#rotate string
class Solution(object):
    def rotateString(self, s, goal):
        return len(s) == len(goal) and goal in s + s

#Partitioning Into Minimum Number Of Deci-Binary nums
class Solution(object):
    def minPartitions(self, n):
        return int(max(n)) 


#Check if Binary String Has at Most One Segment of Ones
class Solution(object):
    def checkOnesSegment(self, s):
        idex=0
        for i in range(len(s)):
            if s[i] =="1":
                if i-idex>1:
                    return False
                idex=i
        return True

#167. Two Sum II - Input Array Is Sorted
class Solution(object):
    def twoSum(self, numbers, target): 
        left=0
        target_value=9
        right=len(numbers)-1
        while left<right:
            sum=numbers[left]+numbers[right]
            if sum==target:
                return [left+1,right+1]
            elif sum<target:
               left+=1
            else:
               right-=1

#Moves zeroes
class Solution(object):
    def moveZeroes(self, nums):
        j=0
        for i in range(len(nums)):
           if nums[i]!=0:
            nums[i], nums[j]=nums[j], nums[i]
            j+=1

#find unique Binary Strings
class Solution(object):
    def findDifferentBinaryString(self, nums):
       res=""
       for i in range(len(nums)):
           if nums[i][i]=='0':
              res+='1'
           else:
                res+='0'
       return res

#minimum String Length
class Solution(object):
    def minimizedStringLength(self, str):
        list={}
        for i in str:
            list[i]=0
        return len(list)

#palindrome Number
class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False        
        s=str(x)
        return s==s[::-1]

#container with most waster
class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0  
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area) 
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

#to lower case
class Solution:
    def toLowerCase(self, s):
        res = ""
        for i in s:
            if i.isupper():
                res += chr(ord(i) + 32)
            else:
                res += i
        return res

#count odd numbers in an interval range
class Solution(object):
    def countOdds(self, low, high):
        odd=(high-low)//2
        if low%2==1 or high%2==1:
            odd+=1
        return odd


#find the greates element of array
class Solution(object):
    def findGCD(self, nums):
        x=min(nums)
        y=max(nums)
        while y:
            x,y=y, x%y
        return x
"""

#shortest palindrome
class Solution(object):
    def shortestPalindrome(self, s):
       rev=s[::-1]
       for i in range(len(s)+1):
        if s.startswith(rev[i:]):
                 return rev[:i] + s



