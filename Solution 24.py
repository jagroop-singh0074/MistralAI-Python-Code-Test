class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        max_sum = float('-inf')

        for i in range(n):
            for j in range(m):
                for k in range(i, n):
                    col3 = j + 1 if k == i else j
                    for col2 in range(col3, n):
                        if col2 != i and col2 != k:
                            sum_val = board[j][i] + board[(j + 1) % m][k] + board[(j + 2) % m][col2]
                            max_sum = max(max_sum, sum_val)

        return max_sum
