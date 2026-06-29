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
        return ans"""
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