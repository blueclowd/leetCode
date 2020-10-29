'''
Description:
Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
'''

from collections import defaultdict


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        counter = defaultdict(int)

        for word in words:
            counter[word] += 1

        counter2 = defaultdict(list)

        for key, value in counter.items():
            counter2[value].append(key)

        output_words = []

        for key, words in sorted(counter2.items(), key=lambda c: c[0], reverse=True):

            sorted_words = sorted(words)

            for word in sorted_words:
                output_words.append(word)

        return output_words[:k]
