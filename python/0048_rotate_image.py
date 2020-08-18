'''
Description:
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n_rows, n_cols = len(matrix), len(matrix[0])

        # Vertical Flip
        for row_index in range(n_rows // 2):
            matrix[row_index], matrix[n_rows - row_index - 1] = matrix[n_rows - row_index - 1], matrix[row_index]

        # Transpose
        for row_index in range(n_rows):

            for col_index in range(row_index, n_cols):
                matrix[row_index][col_index], matrix[col_index][row_index] = matrix[col_index][row_index], \
                                                                             matrix[row_index][col_index]