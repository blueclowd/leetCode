'''
Description:
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:

        if s == '':
            return -1

        table = defaultdict(list)

        for idx, char in enumerate(s):
            table[char].append(idx)

        uniques = [indices[0] for char, indices in table.items() if len(indices) == 1]

        return min(uniques) if uniques else -1