'''
Description:
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        for index in range(len(nums) - 1):

            if nums[index] == nums[index + 1]:
                return True

        return False