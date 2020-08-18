'''
Description:
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i, j = 0, 1

        while j < len(nums):

            if nums[i] == nums[j]:
                del nums[j]

            else:
                i += 1
                j += 1

        return len(nums)