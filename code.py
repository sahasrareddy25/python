
"""#guess number higher or lower
class Solution:
    def guessNumber(self, n):
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                right = mid - 1
            else:
                left = mid + 1

#guess the nummber
DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email
AND p1.id > p2.id;

#last pivot element
class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            if left == total - left - nums[i]:
                return i
            left += nums[i]

        return -1
#fizz buzz
class Solution:
    def fizzBuzz(self, n):
        ans = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))

        return ans"""
#student attendance record I
class Solution:
    def checkRecord(self, s):
        return s.count('A') < 2 and "LLL" not in s