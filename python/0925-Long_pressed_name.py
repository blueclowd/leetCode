'''
Description:
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
'''


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        name_freq = self.get_frequency(name)
        typed_freq = self.get_frequency(typed)

        if len(name_freq) != len(typed_freq):
            return False

        for name_sub, typed_sub in zip(name_freq, typed_freq):

            key_1, freq_1 = name_sub
            key_2, freq_2 = typed_sub

            if key_1 != key_2:
                return False

            if freq_1 > freq_2:
                return False

        return True

    def get_frequency(self, name):

        pre_char = '0'
        frequency = 0

        name_freq = []
        name += '0'

        for index in range(len(name)):

            if name[index] == pre_char:
                frequency += 1

            else:
                name_freq.append((pre_char, frequency))

                frequency = 1

            pre_char = name[index]

        name_freq = name_freq[1:]

        return name_freq