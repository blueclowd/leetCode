'''
Description:
Write an algorithm to determine if a number n is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
Return True if n is a happy number, and False if not.
'''


class Solution:
    def isHappy(self, n: int) -> bool:

        next_n = n

        table = {}

        while next_n != 1:

            if next_n in table:

                return False

            else:

                sum_of_square = self.get_sum_of_square(next_n)

                table[next_n] = sum_of_square

            next_n = sum_of_square

        return True

    def get_sum_of_square(self, n: int):

        digits = []

        while n > 0:
            remainder = n % 10
            n = n // 10

            digits.append(remainder)

        return sum([d ** 2 for d in digits])