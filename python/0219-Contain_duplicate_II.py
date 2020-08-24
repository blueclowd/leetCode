'''
Description:
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        table = {}

        for index, num in enumerate(nums):

            if num in table:

                prev_index = table[num]

                if index - prev_index <= k:
                    return True
                else:
                    table[num] = index

            else:

                table[num] = index

        return False