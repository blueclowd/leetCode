'''
Description:
Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.
'''


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        n_rows, n_cols = len(mat), len(mat[0])

        # Start from (i,j), the farthest can be reached in row
        dp = [[0 for i in range(n_cols)] for j in range(n_rows)]

        for row_idx in reversed(range(n_rows)):
            for col_idx in reversed(range(n_cols)):

                if col_idx == n_cols - 1:
                    dp[row_idx][col_idx] = mat[row_idx][col_idx]

                else:

                    if mat[row_idx][col_idx] != 0:
                        dp[row_idx][col_idx] = dp[row_idx][col_idx + 1] + 1

        count = 0

        for row_idx in range(n_rows):
            for col_idx in range(n_cols):

                min_value = float('inf')

                for k in range(row_idx, n_rows):
                    min_value = min(min_value, dp[k][col_idx])

                    count += min_value

        return count
