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
print(is_valid("(]"))       """

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