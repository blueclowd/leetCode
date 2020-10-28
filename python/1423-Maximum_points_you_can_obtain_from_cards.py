'''
Description:
There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
'''


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        max_score = 0
        n = len(cardPoints)
        win_size = n - k

        if n == k:
            return sum(cardPoints)

        total = sum(cardPoints)

        window_sum = sum(cardPoints[:n - k - 1])

        for start_idx in range(0, k + 1):

            if start_idx != 0:
                window_sum -= cardPoints[start_idx - 1]

            window_sum += cardPoints[start_idx + win_size - 1]

            max_score = max(max_score, total - window_sum)

        return max_score
