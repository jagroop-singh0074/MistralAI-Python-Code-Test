class Solution(object):
    def validSequence(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[] for _ in range(n + 1)]
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j] or (j < n - 1 and word1[i] == word2[j + 1]):
                    if j == n - 1 or len(dp[j + 1]) > 0:
                        dp[j].append(i)
        return dp[0][::-1] if dp[0] else []
