'''
Description:
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:
Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operand_stack = []

        for token in tokens:

            if token in ["+", "-", "*", "/"]:

                right_operand = operand_stack.pop()
                left_operand = operand_stack.pop()

                if token == "+":
                    operand_stack.append(left_operand + right_operand)

                elif token == "-":
                    operand_stack.append(left_operand - right_operand)

                elif token == "*":
                    operand_stack.append(left_operand * right_operand)

                elif token == "/":

                    operand_stack.append(int(left_operand / right_operand))

            else:

                operand_stack.append(int(token))

        return operand_stack.pop()