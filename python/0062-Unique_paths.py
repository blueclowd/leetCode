'''
Description:
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        n_ways = [[1 for i in range(n)] for j in range(m)]

        for row_index in range(1, m):

            for col_index in range(1, n):
                n_ways[row_index][col_index] = n_ways[row_index - 1][col_index] + n_ways[row_index][col_index - 1]

        return n_ways[-1][-1]