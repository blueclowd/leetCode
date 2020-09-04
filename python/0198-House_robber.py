'''
Description:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''


class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        max_amounts = [0] * len(nums)
        max_amounts[0] = nums[0]
        max_amounts[1] = max(nums[:2])

        for i in range(2, len(nums)):
            max_amounts[i] = max(nums[i] + max_amounts[i - 2], max_amounts[i - 1])

        return max_amounts[-1]