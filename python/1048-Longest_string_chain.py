'''
Description:
Given a list of words, each word consists of English lowercase letters.
Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".
A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
Return the longest possible length of a word chain with words chosen from the given list of words.
'''


class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        sorted_words = sorted(words, key=lambda k: len(k))

        n_words = len(words)

        dp = [1] * n_words

        for i in range(n_words):
            for j in range(i + 1, n_words):

                if len(sorted_words[j]) > len(sorted_words[i]) + 1:
                    break

                if self.predecessor(sorted_words[i], sorted_words[j]):
                    dp[j] = max(dp[i] + 1, dp[j])

        return max(dp)

    def predecessor(self, word_1, word_2):

        is_predecessor = False

        for idx, char in enumerate(word_2):

            if word_1 == word_2[:idx] + word_2[idx + 1:]:
                is_predecessor = True

        return is_predecessor
