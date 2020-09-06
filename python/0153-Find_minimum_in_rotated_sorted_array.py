'''
Description:
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        if nums[left] < nums[right]:
            return nums[left]

        while right - left > 1:

            mid = left + int((right - left) * 0.5)

            if nums[left] > nums[mid]:
                right = mid

            else:
                left = mid

        return nums[right]

