'''
Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''


class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 2:
            return False

        parentheses_map = {")": "(", "}": "{", "]": "["}

        stack = []

        for char in s:

            if char in ["(", "[", "{"]:

                stack.append(char)

            else:

                if len(stack) == 0:
                    return False

                left_parenthese = stack.pop()

                if left_parenthese != parentheses_map[char]:
                    return False

        return len(stack) == 0