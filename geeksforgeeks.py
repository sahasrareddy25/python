""" #The Painter's Partition Problem-II
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

#Meeting Rooms
#Difficulty: EasyAccuracy: 65.12%Submissions: 38K+Points: 2
#Given a 2D array arr[][], where arr[i][0] is the starting time of ith meeting and arr[i][1] is the ending time of ith meeting, the task is to check if it is possible for a person to attend all the meetings such that he can attend only one meeting at a particular time.
class Solution:
    def canAttend(self, arr):
        arr.sort(key=lambda x: x[0])
        for i in range(1, len(arr)):
            if arr[i][0] < arr[i-1][1]:
                return False
        return True


#Maximum number of overlapping Intervals
#You are given an array of intervals arr[][], where each interval is represented by two integers [start, end] (inclusive). Return the maximum number of intervals that overlap at any point in time.
class Solution:
    def overlapInt(self, arr):
        n = len(arr)
        start = []
        end = []
        for s, e in arr:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()
        i = j = 0
        curr = 0
        maxi = 0
        while i < n and j < n:
            if start[i] <= end[j]:   # inclusive
                curr += 1
                maxi = max(maxi, curr)
                i += 1
            else:
                curr -= 1
                j += 1
        return maxi """


#Count Inversions
#Given an array of integers arr[]. You have to find the Inversion Count of the array. 
#Note: Inversion count is the number of pairs of elements (i, j) such that i < j and arr[i] > arr[j].
class Solution:
    def inversionCount(self, arr):

        def merge_sort(arr, temp, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2

                inv_count += merge_sort(arr, temp, left, mid)
                inv_count += merge_sort(arr, temp, mid + 1, right)
                inv_count += merge(arr, temp, left, mid, right)

            return inv_count

        def merge(arr, temp, left, mid, right):
            i = left
            j = mid + 1
            k = left
            inv_count = 0

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    inv_count += (mid - i + 1)
                    j += 1
                k += 1

            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = arr[j]
                j += 1
                k += 1

            for idx in range(left, right + 1):
                arr[idx] = temp[idx]

            return inv_count

        temp = [0] * len(arr)
        return merge_sort(arr, temp, 0, len(arr) - 1)

