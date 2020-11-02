'''
Description:
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
'''


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        nums.sort()

        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(target + 1):

            for num in nums:

                if i + num <= target:

                    dp[i + num] += dp[i]

                else:
                    break

        return dp[target]