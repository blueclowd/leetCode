'''
Description:
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
'''


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        n_rows, n_cols = len(matrix), len(matrix[0])

        for row in range(n_rows):
            for col in range(n_cols):

                if matrix[row][col] != 0:
                    matrix[row][col] = min(matrix[row - 1][col] + 1 if row > 0 else float('inf'),
                                           matrix[row][col - 1] + 1 if col > 0 else float('inf'))

        for row in reversed(range(n_rows)):
            for col in reversed(range(n_cols)):

                if matrix[row][col] != 0:
                    matrix[row][col] = min(matrix[row][col],
                                           matrix[row + 1][col] + 1 if row < n_rows - 1 else float('inf'),
                                           matrix[row][col + 1] + 1 if col < n_cols - 1 else float('inf'))

        return matrix