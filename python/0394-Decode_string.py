'''
Description:
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
'''


class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for i, char in enumerate(s):

            if char == "]":

                enclosed_string = ''

                popped = ''
                while popped != "[":
                    enclosed_string += popped[::-1]
                    popped = stack.pop()

                time = stack.pop()
                while len(stack) > 0 and stack[-1].isdigit():
                    time += stack.pop()

                time = int(time[::-1])

                enclosed_string = enclosed_string * int(time)

                stack.append(enclosed_string[::-1])

            else:
                stack.append(char)

        return "".join(stack)
