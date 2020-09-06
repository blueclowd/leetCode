'''
Description:
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
'''


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        triangle = [[1], [1, 1]]

        for i in range(2, numRows):

            n_nodes = i + 1

            row = [1] * n_nodes
            for j in range(1, n_nodes - 1):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle
