'''
Description:
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        farthest = 0

        for i, num in enumerate(nums):

            farthest = max(nums[i] + i, farthest)

            # Cannot reach the current node
            if i >= farthest and i != len(nums) - 1:
                return False

        return True