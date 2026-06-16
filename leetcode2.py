"""#rotate image
class Solution:
    def rotate(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(i + 1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for k in range(row):
            matrix[k].reverse()"""

#two sum
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