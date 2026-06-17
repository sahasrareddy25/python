"""#rotate image
class Solution:
    def rotate(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(i + 1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for k in range(row):
            matrix[k].reverse()

#two sum-leet code
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target)) 

#removing special character
s = "a#b%*c123"
result = ""
for ch in s:
    if ch.isalnum():
        result += ch
print("Original:", s)
print("Cleaned:", result)

#valid parenthesis
def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return len(stack) == 0
print(is_valid("()[]{}"))  
print(is_valid("(]"))      

#max sum array
def max_subarray(nums):
    max_sum = nums[0]
    current = nums[0]
    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        max_sum = max(max_sum, current)
    return max_sum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))

#letter combination of a phone number
class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        hashmap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        ans = []
        store = []
        def dfs(i):
            if i == len(digits):
                ans.append("".join(store))
                return
            for ch in hashmap[digits[i]]:
                store.append(ch)
                dfs(i + 1)
                store.pop()
        dfs(0)
        return ans
#first missing positive
class Solution(object):
    def firstMissingPositive(self, nums):
        nums = [x for x in nums if x > 0]  
        nums.sort()
        var1 = 1
        for n in nums:
            if n == var1:
                var1 += 1   
            elif n > var1:
                break       
        return var1
arr = [7,8,9,11,12]
a1 = Solution()
print(a1.firstMissingPositive(arr))  """

#process string with special operations II
class Solution:
    def processStr(self, s, k):
        LIMIT = 10**15 + 1
        n = len(s)

        length = [0] * (n + 1)

        for i, ch in enumerate(s):
            cur = length[i]

            if ch.islower():
                length[i + 1] = min(LIMIT, cur + 1)
            elif ch == '*':
                length[i + 1] = max(0, cur - 1)
            elif ch == '#':
                length[i + 1] = min(LIMIT, cur * 2)
            else:  # '%'
                length[i + 1] = cur

        if k >= length[n]:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]
            cur = length[i]

            if ch.islower():
                if k == cur:
                    return ch
            elif ch == '#':
                if cur > 0:
                    k %= cur
            elif ch == '%':
                if cur > 0:
                    k = cur - 1 - k

        return '.'