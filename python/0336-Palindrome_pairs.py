'''
Description:
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.
'''


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        table = {}

        results = []

        for i, word in enumerate(words):
            table[word] = i

        for j, word in enumerate(words):

            # Case 1
            if "" in table and self.is_palindrome(word):
                if table[""] != j:
                    results.append([table[""], j])
                    results.append([j, table[""]])
            # Case 2
            if word[::-1] in table:
                if table[word[::-1]] != j:
                    results.append([table[word[::-1]], j])
                    # results.append([j, table[word[::-1]]])
            # Case 3
            for k in range(1, len(word)):
                left, right = word[:k], word[k:]

                if self.is_palindrome(left) and right[::-1] in table:
                    results.append([table[right[::-1]], j])

                if self.is_palindrome(right) and left[::-1] in table:
                    results.append([j, table[left[::-1]]])

        return results

    def is_palindrome(self, word):

        return word == word[::-1]