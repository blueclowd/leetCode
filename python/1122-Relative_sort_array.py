'''
Description:
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
'''

from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        not_in_arr2 = [v for v in arr1 if v not in arr2]
        not_in_arr2.sort()

        arr1_counter = Counter(arr1)

        result = []

        for v in arr2:
            frequency = arr1_counter[v]

            result += [v] * frequency

        result += not_in_arr2

        return result