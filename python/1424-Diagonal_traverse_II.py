'''
Description:
Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.
'''


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        table = {}

        for row_idx in range(len(nums)):

            for col_idx in range(len(nums[row_idx])):

                if row_idx + col_idx in table:
                    table[row_idx + col_idx].append(nums[row_idx][col_idx])
                else:
                    table[row_idx + col_idx] = [nums[row_idx][col_idx]]

        output = []
        for _, values in sorted(table.items(), key=lambda item: item[0]):
            output += list(reversed(values))

        return output