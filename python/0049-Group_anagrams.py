'''
Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for string in strs:
            num = sorted([ord(char) for char in string])

            table["".join(str(num))].append(string)

        return [nums for key, nums in table.items()]
