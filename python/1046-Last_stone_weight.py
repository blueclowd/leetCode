'''
Description:
We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
'''

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [stone * (-1) for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:

            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)

            if stone_1 != stone_2:
                heapq.heappush(stones, abs(stone_1 - stone_2) * (-1))

        if len(stones) == 0:

            return 0

        else:

            return stones[0] * (-1)