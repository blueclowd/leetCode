'''
Description:
Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
'''


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

        n_rows, n_cols = len(mat), len(mat[0])
        dp = [[0] * n_cols for i in range(n_rows)]
        dp[0][0] = mat[0][0]

        for row_idx in range(1, n_rows):
            dp[row_idx][0] = dp[row_idx - 1][0] + mat[row_idx][0]

        for col_idx in range(1, n_cols):
            dp[0][col_idx] = dp[0][col_idx - 1] + mat[0][col_idx]

        for row_idx in range(1, n_rows):
            for col_idx in range(1, n_cols):
                dp[row_idx][col_idx] = mat[row_idx][col_idx] + dp[row_idx - 1][col_idx] + dp[row_idx][col_idx - 1] - \
                                       dp[row_idx - 1][col_idx - 1]

        for row_idx in range(n_rows):
            for col_idx in range(n_cols):
                left_block_sum = dp[min(row_idx + K, n_rows - 1)][col_idx - K - 1] if col_idx - K - 1 >= 0 else 0
                top_block_sum = dp[row_idx - K - 1][min(col_idx + K, n_cols - 1)] if row_idx - K - 1 >= 0 else 0
                top_left_block_sum = dp[row_idx - K - 1][
                    col_idx - K - 1] if row_idx - K - 1 >= 0 and col_idx - K - 1 >= 0 else 0

                mat[row_idx][col_idx] = dp[min(row_idx + K, n_rows - 1)][min(col_idx + K,
                                                                             n_cols - 1)] - left_block_sum - top_block_sum + top_left_block_sum

        return mat