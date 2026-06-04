"""#longest common prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        p = strs[0]
        for s in strs[1:]:
            while not s.startswith(p):
                p = p[:-1]
        return p

#count the number of special characters
class Solution(object):
    def numberOfSpecialChars(self, word):
        s = set(word)
        count = 0
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in s and ch.upper() in s:
                count += 1
        return count
        

#erliest finish time to  land and water rides
class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        ans = float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                ans = min(
                    ans,
                    max(landStartTime[i] + landDuration[i], waterStartTime[j]) + waterDuration[j],
                    max(waterStartTime[j] + waterDuration[j], landStartTime[i]) + landDuration[i]
                )
        return ans

#earliest finish time for land and water Rides II
class Solution:
    def earliestFinishTime(self, a, b, c, d):
        ans = float('inf')
        n = len(a)
        minEnd = float('inf')
        for i in range(n):
            minEnd = min(minEnd, a[i] + b[i])
        m = len(c)
        for i in range(m):
            ans = min(ans, d[i] + max(minEnd, c[i]))
        minEnd = float('inf')
        for i in range(m):
            minEnd = min(minEnd, c[i] + d[i])
        for i in range(n):
            ans = min(ans, b[i] + max(minEnd, a[i]))
        return ans
#minimum cost of buying candies with discount
class Solution:
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        return sum(c for i, c in enumerate(cost) if i % 3 != 2)

#3751. Total Waviness of Numbers in Range I
class Solution:
    def totalWaviness(self, num1, num2):
        c = 0
        for n in range(num1, num2 + 1):
            s = str(n)
            for i in range(1, len(s) - 1):
                c += (s[i-1] < s[i] > s[i+1]) or (s[i-1] > s[i] < s[i+1])
        return c"""

#2144. Minimum Cost of Buying Candies With Discount
class Solution:
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        return sum(c for i, c in enumerate(cost) if i % 3 != 2)