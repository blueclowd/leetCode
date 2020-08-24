'''
Description:
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
'''


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        ab_sum = {}
        count = 0

        for a in A:
            for b in B:
                if a + b in ab_sum:
                    ab_sum[a + b] += 1
                else:
                    ab_sum[a + b] = 1

        for c in C:
            for d in D:
                if -(c + d) in ab_sum:
                    count += ab_sum[-(c + d)]

        return count
