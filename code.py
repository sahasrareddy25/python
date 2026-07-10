
#guess number higher or lower
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