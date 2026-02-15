"""#The Painter's Partition Problem-II
#Difficulty: HardAccuracy: 27.52%Submissions: 172K+Points: 8
#Given an array arr[] where each element denotes the length of a board, and an integer k representing the number of painters available. Each painter takes 1 unit of time to paint 1 unit length of a board.
#Determine the minimum amount of time required to paint all the boards, under the constraint that each painter can paint only a contiguous sequence of boards (no skipping or splitting allowed).
class Solution:
    def minTime(self, arr, k):
        def canPaint(maxTime):
            painters = 1
            current_sum = 0
            for length in arr:
                if current_sum + length <= maxTime:
                    current_sum += length
                else:
                    painters += 1
                    current_sum = length

                    if painters > k:
                        return False
            return True
        low = max(arr)
        high = sum(arr)
        answer = high
        while low <= high:
            mid = (low + high) // 2
            if canPaint(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer"""

#Chocolate Distribution Problem
#Given an array arr[] of positive integers, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets among m students such that -
#i. Each student gets exactly one packet.
#ii. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum and return that minimum possible difference.
class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)
        if m > n:
            return -1
        arr.sort()
        min_diff = float('inf')
        for i in range(n - m + 1):
            min_diff = min(min_diff, arr[i + m - 1] - arr[i])
            return min_diff
