'''
Description:
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.
'''


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        total_length = 0

        char_counter = self.get_frequency(chars)

        for word in words:

            word_counter = self.get_frequency(word)

            is_good_string = True
            for char, frequency in word_counter.items():

                if char not in char_counter:
                    is_good_string = False
                    break
                else:
                    if frequency > char_counter[char]:
                        is_good_string = False

            if is_good_string:
                total_length += len(word)

        return total_length

    def get_frequency(self, s):

        table = {}

        for char in s:
            if char in table:
                table[char] += 1
            else:
                table[char] = 1

        return table