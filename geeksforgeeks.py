#The Painter's Partition Problem-II
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
        return answer