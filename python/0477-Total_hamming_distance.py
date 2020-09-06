'''
Description:
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Now your job is to find the total Hamming distance between all pairs of the given numbers.
'''


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        if not nums:
            return 0

        binaries = []
        for num in nums:

            binary = []
            while num > 0:
                quotient = num // 2
                remainder = num % 2

                binary.append(remainder)

                num = quotient

            binaries.append(binary)

        max_length = max([len(binary) for binary in binaries])

        binaries = [list(reversed(binary + [0] * (max_length - len(binary)))) for binary in binaries]

        total = 0

        for digit_idx in range(len(binaries[0])):
            digits = [binaries[row][digit_idx] for row in range(len(binaries))]

            n_ones = sum(digits)
            n_zeros = len(binaries) - n_ones

            total += n_ones * n_zeros

        return total

