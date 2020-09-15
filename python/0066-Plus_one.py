'''
Description:
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        result = []
        carry_bit = 1

        for i in reversed(range(len(digits))):
            total = digits[i] + carry_bit

            carry_bit = total // 10
            remainder = total % 10

            result.append(remainder)

        if carry_bit != 0:
            result.append(carry_bit)

        return list(reversed(result))
