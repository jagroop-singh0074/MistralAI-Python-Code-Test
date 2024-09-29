class Solution(object):
    def maximumValueSum(self, board):
        m, n = len(board), len(board[0])
        row_max = [max(row) for row in board]
        col_max = [max(col) for col in zip(*board)]
        max_sum = float('-inf')

        for i in range(m):
            for j in range(n):
                for k in range(m):
                    if i == k:
                        continue
                    for l in range(n):
                        if j == l:
                            continue
                        max_sum = max(max_sum, board[i][j] + board[k][l] + board[m-i-1][n-j-1])

        return max_sum
