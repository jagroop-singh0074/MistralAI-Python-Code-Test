class Solution(object):
    def maxScore(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [0] * (1 << n)
        for row in grid:
            for j in range(n):
                for i in range(1 << n):
                    if i & (1 << j):
                        dp[i] = max(dp[i], dp[i ^ (1 << j)] + row[j])
        return max(dp)
