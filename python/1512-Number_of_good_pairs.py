'''
Description:
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
'''


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        table = {}
        count = 0

        for idx, num in enumerate(nums):

            if num in table:
                count += len(table[num])
                table[num].append(idx)

            else:
                table[num] = [idx]

        return count