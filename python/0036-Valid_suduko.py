'''
Description:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:

            values = [int(char) for char in row if char != '.']

            if sum(set(values)) != sum(values):
                return False

        for col_idx in range(9):

            values = [int(board[row_idx][col_idx]) for row_idx in range(9) if board[row_idx][col_idx] != '.']

            if sum(set(values)) != sum(values):
                return False

        for row_index in [0, 3, 6]:
            for col_index in [0, 3, 6]:

                values = []

                for x_step in range(3):
                    for y_step in range(3):

                        if board[row_index + y_step][col_index + x_step] != '.':
                            values.append(int(board[row_index + y_step][col_index + x_step]))

                if sum(set(values)) != sum(values):
                    return False

        return True







