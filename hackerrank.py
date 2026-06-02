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
        """

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
        