'''
Description:
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
At the end, return the modified image.
'''


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        queue = [(sr, sc)]

        src_color = image[sr][sc]

        n_rows, n_cols = len(image), len(image[0])

        visited = [[False] * n_cols for i in range(n_rows)]

        while queue:

            n_p = len(queue)

            for i in range(n_p):

                p = queue.pop(0)
                row, col = p

                image[row][col] = newColor
                visited[row][col] = True

                if self.is_valid((row - 1, col), n_rows, n_cols) and image[row - 1][col] == src_color and not \
                visited[row - 1][col]:
                    queue.append((row - 1, col))
                if self.is_valid((row + 1, col), n_rows, n_cols) and image[row + 1][col] == src_color and not \
                visited[row + 1][col]:
                    queue.append((row + 1, col))
                if self.is_valid((row, col - 1), n_rows, n_cols) and image[row][col - 1] == src_color and not \
                visited[row][col - 1]:
                    queue.append((row, col - 1))
                if self.is_valid((row, col + 1), n_rows, n_cols) and image[row][col + 1] == src_color and not \
                visited[row][col + 1]:
                    queue.append((row, col + 1))

        return image

    def is_valid(self, p, n_rows, n_cols):

        row, col = p

        return (0 <= row < n_rows) and (0 <= col < n_cols)