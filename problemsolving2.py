"""#Remove Nth Node From End of List
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

#minimum path sum
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]

#insert internal
class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        while i < n:
            result.append(intervals[i])
            i += 1
        return result"""
#30. Substring with Concatenation of All Words
from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        wl = len(words[0])
        total = wl * len(words)
        target = Counter(words)
        ans = []

        for i in range(len(s) - total + 1):
            seen = Counter()
            for j in range(0, total, wl):
                w = s[i + j:i + j + wl]
                if seen[w] == target[w]:
                    break
                seen[w] += 1
            else:
                ans.append(i)

        return ans