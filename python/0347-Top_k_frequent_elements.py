'''
Description:
Given a non-empty array of integers, return the k most frequent elements.
'''

from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        outputs = []
        for num, frequency in sorted(counter.items(), key=lambda c: c[1], reverse=True):

            outputs.append(num)

            if len(outputs) == k:
                break

        return outputs