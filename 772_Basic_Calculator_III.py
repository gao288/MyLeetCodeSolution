from typing import *
class Solution:
    def calculate(self, s: str) -> int:
        s += ' '
        val = 0
        sign = '+'
        stack = []

        for i, c in enumerate(s):
            if c.isdigit():
                val = val * 10 + int(c)

            elif c == '(':
                stack.append(sign)
                stack.append('(')
                val = 0
                sign = '+'

            if (not c.isdigit() and c != ' ' and c != '(') or c == ')' or i == len(s) - 1:
                if sign == '+':
                    stack.append(val)
                    sign = c
                elif sign == '-':
                    stack.append(-val)
                    sign = c
                elif sign == '*':
                    stack.append(stack.pop() * val)
                    sign = c
                elif sign == '/':
                    stack.append(int(stack.pop() / val))
                    sign = c
                val = 0

                if c == ')':
                    while len(stack) > 0:
                        temp = stack.pop()
                        if temp == '(':
                            sign = stack.pop()
                            break
                        else:
                            val += temp
        return sum(stack)


s = Solution()
print(s.calculate("1-(-7)"))