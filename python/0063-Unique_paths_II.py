'''
Description:
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        n_rows, n_cols = len(obstacleGrid), len(obstacleGrid[0])

        n_ways = [[1 for i in range(n_cols)] for j in range(n_rows)]

        if obstacleGrid[0][0] == 1:
            return 0

        for col_index in range(1, n_cols):
            n_ways[0][col_index] = n_ways[0][col_index - 1] if obstacleGrid[0][col_index] != 1 else 0

        for row_index in range(1, n_rows):
            n_ways[row_index][0] = 0 if obstacleGrid[row_index][0] == 1 else n_ways[row_index - 1][0]

        for row_index in range(1, n_rows):

            for col_index in range(1, n_cols):

                if obstacleGrid[row_index][col_index] == 1:

                    n_ways[row_index][col_index] = 0

                else:

                    n_ways[row_index][col_index] = n_ways[row_index - 1][col_index] + n_ways[row_index][col_index - 1]

        return n_ways[-1][-1]
