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
        return result
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

#text verification
class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        while i < len(words):
            j = i
            length = 0
            while j < len(words) and length + len(words[j]) + (j - i) <= maxWidth:
                length += len(words[j])
                j += 1
            gaps = j - i - 1
            line = ""
            if j == len(words) or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                spaces = maxWidth - length
                even = spaces // gaps
                extra = spaces % gaps
                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (even + (1 if extra > 0 else 0))
                    if extra:
                        extra -= 1
                line += words[j - 1]
            res.append(line)
            i = j
        return res
#candy
class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
#remove linked lists
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
#Maximum Depth of N-ary Tree
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)"""

#search insert positition
class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left