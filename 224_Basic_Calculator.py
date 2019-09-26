class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        sign = 1 
        res = 0
        for c in s:
            if c.isdigit():
                operand = operand * 10 + int(c)
            elif c == '-':
                res = res + sign * operand
                operand = 0
                sign = -1
            elif c == '+':
                res = res + sign * operand
                sign = 1
                operand = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                operand = 0
                sign = 1
            elif c == ')':
                res = res + sign * operand
                operand = 0
                res *= stack.pop()
                res += stack.pop()
                
                
        return res + sign * operand
                     
