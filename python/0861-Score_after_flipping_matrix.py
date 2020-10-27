'''
Description:
We have a two dimensional matrix A where each value is 0 or 1.
A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.
After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
Return the highest possible score.
'''


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:

        n_rows, n_cols = len(A), len(A[0])

        for row_idx, row in enumerate(A):

            if row[0] == 0:
                A[row_idx] = [1 - cell for cell in row]

        for col_idx in range(1, n_cols):

            n_ones = sum([A[row_idx][col_idx] for row_idx in range(n_rows)])
            n_zeros = n_rows - n_ones

            if n_zeros > n_ones:

                for row_idx in range(n_rows):
                    A[row_idx][col_idx] = 1 - A[row_idx][col_idx]

        total_sum = 0
        for row in A:

            row_sum = 0
            for idx in range(n_cols):
                row_sum = row_sum * 2 + row[idx]

            total_sum += row_sum

        return total_sum
