'''
Description:
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n_nums = len(nums)

        left, right = 0, n_nums - 1

        while left <= right:

            middle = left + (right - left) // 2

            if target == nums[middle]:
                return middle

            elif target > nums[middle]:
                left = middle + 1

            else:
                right = middle - 1

        return left