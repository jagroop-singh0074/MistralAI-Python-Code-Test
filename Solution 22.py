class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            orVal = 0
            for j in range(min(i, k), 0, -1):
                orVal |= nums[i - 1]
                dp[i][j] = max(dp[i][j], dp[i - j][i - j] ^ orVal)
                for l in range(1, j):
                    dp[i][j] = max(dp[i][j], dp[i - l][i - l] ^ (orVal | nums[i - l - 1]))

        return dp[n][k]
