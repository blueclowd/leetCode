'''
Description:
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.
'''


class Solution:
    def findAnagrams(self, s: str, p: str):

        indices = []

        p_counter = self.get_frequency(p)
        prev_counter = self.get_frequency(s[:len(p)])

        if p_counter == prev_counter:
            indices.append(0)

        for i in range(1, len(s) - len(p) + 1):

            removed_char = s[i - 1]
            new_char = s[i + len(p) - 1]

            # Update counter
            prev_counter[removed_char] -= 1
            if prev_counter[removed_char] == 0:
                prev_counter.pop(removed_char)

            if new_char in prev_counter:
                prev_counter[new_char] += 1
            else:
                prev_counter[new_char] = 1

            # Is anagram if counter is the same
            if prev_counter == p_counter:
                indices.append(i)

        return indices

    def get_frequency(self, s):

        counter = {}
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        return counter