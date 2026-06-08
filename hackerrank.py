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
        return c

#2144. Minimum Cost of Buying Candies With Discount
class Solution:
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        return sum(c for i, c in enumerate(cost) if i % 3 != 2)

#3sum closet
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s-target) < abs(ans-target):
                    ans = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return target
        return ans

#left and right sum difference
class Solution:
    def leftRightDifference(self, nums):
        s=sum(nums)
        l=0
        ans=[]
        for x in nums:
            s-=x
            ans.append(abs(l-s))
            l+=x
        return ans
#reverse integer
class Solution:
    def reverse(self, x):
        r=int(str(abs(x))[::-1])
        if x<0:r=-r
        return r if -2**31<=r<=2**31-1 else 0

#longest valid parenthesis
class Solution:
    def longestValidParentheses(self, s):
        st=[-1]
        ans=0
        for i,c in enumerate(s):
            if c=='(':
                st.append(i)
            else:
                st.pop()
                if st:
                    ans=max(ans,i-st[-1])
                else:
                    st.append(i)
        return ans

#create binary tree from descriptions
class Solution:
    def createBinaryTree(self, descriptions):
        nodes = {}
        childs = set()

        for p, c, l in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)

            if l:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]

            childs.add(c)

        for p, _, _ in descriptions:
            if p not in childs:
                return nodes[p]"""

#partition array according to the given pivot
class Solution(object):
    def pivotArray(self, nums, pivot):
        l=[];
        e=[];
        g=[];
        for i in nums:
            if(i<pivot):
                l.append(i);
            elif(i==pivot):
                e.append(i);
            else:
                g.append(i);
        return l+e+g
        