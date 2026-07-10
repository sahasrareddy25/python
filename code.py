
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
                left = mid + 1"""

#guess the nummber
DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email
AND p1.id > p2.id;