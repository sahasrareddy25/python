"""#combination sum II
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        def dfs(start, target, path):
            if target == 0:
                ans.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(i + 1, target - candidates[i], path)
                path.pop()
        dfs(0, target, [])
        return ans
#unique paths II
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]
        return dp[m - 1][n - 1]

# Convert Sorted List to Binary Search Tree
class Solution:
    def sortedListToBST(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        return build(0, len(nums) - 1)

#Populating Next Right Pointers in Each Node
from collections import deque
class Solution:
    def connect(self, root):
        if not root:
            return root
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i < size - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
#Convert Sorted Array to Binary Search Tree
class Solution:
    def sortedArrayToBST(self, nums):

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)
#partition list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head, x):
        small = ListNode(0)
        large = ListNode(0)
        s = small
        l = large
        while head:
            if head.val < x:
                s.next = head
                s = s.next
            else:
                l.next = head
                l = l.next
            head = head.next
        l.next = None
        s.next = large.next
        return small.next
#decode ways
class Solution:
    def numDecodings(self, s):
        n = len(s)
        if s[0] == '0':
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[n]
#search in rotated array II
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Skip duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            # Left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
#populating Next Right Pointers in Each Node II
from collections import deque

class Solution:
    def connect(self, root):
        if not root:
            return root

        q = deque([root])

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()

                if i < size - 1:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root

#1358. Number of Substrings Containing All Three Characters
class Solution(object):
    def numberOfSubstrings(self, s):
        n = len(s)
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        ans = 0

        for right in range(n):
            count[s[right]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                ans += n - right
                count[s[left]] -= 1
                left += 1

        return ans

#pow(x,n)
class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1.0

        if n < 0:
            x = 1.0 / x
            n = -n

        ans = 1.0

        while n > 0:
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2

        return ans

#1967. Number of Strings That Appear as Substrings in Word
class Solution:
    def numOfStrings(self, patterns, word):
        count = 0

        for pattern in patterns:
            if pattern in word:
                count += 1

        return count
    
#Maximum Element After Decreasing and Rearranging
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()

        arr[0] = 1

        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)

        return arr[-1]"""
#merge intervals
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
        