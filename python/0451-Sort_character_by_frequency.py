'''
Description:
Given a string, sort it in decreasing order based on the frequency of characters.
'''

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:

        frequencies = Counter(s)

        sorted_frequencies = self.insertion_sort(frequencies)

        result = ''

        for char, frequency in sorted_frequencies:

            for i in range(frequency):
                result += char

        return result

    def insertion_sort(self, frequencies):

        sorted_frequencies = [('dummy', 0)]

        for char, frequency in frequencies.items():

            if frequency >= sorted_frequencies[-1][1]:
                sorted_frequencies.append((char, frequency))

            for i, (c, f) in enumerate(sorted_frequencies):

                if frequency < f:
                    sorted_frequencies = sorted_frequencies[:i] + [(char, frequency)] + sorted_frequencies[i:]

                    break

        return list(reversed(sorted_frequencies))