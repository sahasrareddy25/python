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
        return maxi 


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

#Missing Element in Range Difficulty: MediumAccuracy: 55.45%Submissions: 15K+Points: 4Average Time: 20m Given an array arr[] of integers and a range [low, high], find all the numbers within the range that are not present in the array. return the missing numbers in sorted order.
class Solution:
    def missingRange(self, arr, low, high):
        s = set(arr)
        ans = []

        for i in range(low, high + 1):
            if i not in s:
                ans.append(i)

        return ans

#Form the Largest Number.Given an array of integers arr[] representing non-negative integers, arrange them so that after concatenating all of them in order, it results in the largest possible number. Since the result may be very large, return it as a string.
from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):   # ✅ changed name
        
        arr = [str(x) for x in arr]

        def cmp(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        arr.sort(key=cmp_to_key(cmp))

        if arr[0] == '0':
            return '0'

        return ''.join(arr)

#Find H-Index
#You are given an array citations[], where each element citations[i] represents the number of citations received by the ith paper of a researcher. You have to calculate the researcher’s H-index.
#The H-index is defined as the maximum value H, such that the researcher has published at least H papers, and all those papers have citation value greater than or equal to H.
class Solution:
    def hIndex(self, citations):
        n = len(citations)
        count = [0] * (n + 1)
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        total = 0
        for h in range(n, -1, -1):
            total += count[h]
            if total >= h:
                return h
        return 0

#Count Subarrays with given XOR
#Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.
class Solution:
    def subarrayXor(self, arr, k):
        count = 0
        xr = 0
        freq = {0: 1}

        for num in arr:
            xr ^= num
            if xr ^ k in freq:
                count += freq[xr ^ k]
            freq[xr] = freq.get(xr, 0) + 1

        return count

#Union of Arrays with Duplicates
#You are given two arrays a[] and b[], return the Union of both the arrays in any order.
#The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.
class Solution:
    def findUnion(self, a, b):
        union_set = set()
        
        for num in a:
            union_set.add(num)
            
        for num in b:
            union_set.add(num)
            
        return list(union_set)

#Longest Span in two Binary Arrays
#Given two binary arrays, a1[] and a2[] of equal length. Find the length of longest common span (i, j), where i<= j such that a1[i] + a1[i+1] + .... + a1[j] =  a2[i] + a2[i+1] + ... + a2[j].
class Solution:
    def equalSumSpan(self, a1, a2):
        n = len(a1)
        prefix_sum = 0
        first_index = {}
        max_len = 0
        for i in range(n):
            prefix_sum += a1[i] - a2[i]
            if prefix_sum == 0:
                max_len = i + 1
            if prefix_sum in first_index:
                max_len = max(max_len, i - first_index[prefix_sum])
            else:
                first_index[prefix_sum] = i
        return max_len

#Isomorphic Strings
#Given two strings s1 and s2 consisting of only lowercase English letters and of equal length, check if these two strings are isomorphic to each other.
#If the characters in s1 can be changed to get s2, then two strings, s1 and s2 are isomorphic. A character must be completely swapped out for another character while maintaining the order of the characters. A character may map to itself, but no two characters may map to the same character.
class Solution:
    def areIsomorphic(self, s1, s2):
        
        map1 = {}
        map2 = {}
        
        for i in range(len(s1)):
            c1 = s1[i]
            c2 = s2[i]
            if c1 in map1:
                if map1[c1] != c2:
                    return False
            else:
                map1[c1] = c2
            
            if c2 in map2:
                if map2[c2] != c1:
                    return False
            else:
                map2[c2] = c1
        
        return True

#Number of submatrix have sum X
class Solution:
    def countSquare(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        
        prefix = [[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                prefix[i][j] = mat[i][j]
                if i > 0:
                    prefix[i][j] += prefix[i-1][j]
                if j > 0:
                    prefix[i][j] += prefix[i][j-1]
                if i > 0 and j > 0:
                    prefix[i][j] -= prefix[i-1][j-1]
        
        count = 0
        
        for i in range(n):
            for j in range(m):
                max_len = min(n-i, m-j)
                
                for size in range(1, max_len+1):
                    r2 = i + size - 1
                    c2 = j + size - 1
                    
                    total = prefix[r2][c2]
                    
                    if i > 0:
                        total -= prefix[i-1][c2]
                    if j > 0:
                        total -= prefix[r2][j-1]
                    if i > 0 and j > 0:
                        total += prefix[i-1][j-1]
                    
                    if total == x:
                        count += 1
        
        return count"""

#Find the closest pair from two arrays
def closestPair(arr1, arr2, x):
    n = len(arr1)
    m = len(arr2)
    
    i = 0
    j = m - 1
    
    min_diff = float('inf')
    result = [0, 0]
    
    while i < n and j >= 0:
        current_sum = arr1[i] + arr2[j]
        diff = abs(current_sum - x)
        
        if diff < min_diff:
            min_diff = diff
            result = [arr1[i], arr2[j]]
        
        if current_sum > x:
            j -= 1
        else:
            i += 1
    
    return result


arr1 = [1, 4, 5, 7]
arr2 = [10, 20, 30, 40]
x = 32

print(closestPair(arr1, arr2, x))