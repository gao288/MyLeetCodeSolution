class Solution:
    def calculate(self, s: str) -> int:
        val = 0
        sign = '+'
        stack = []
       
        for i,c in enumerate(s):
            if c.isdigit():
                val = val * 10 + int(c)
            
            if (not c.isdigit() and c != ' ') or i == len(s)-1:
                
                if sign == '+':
                    stack.append(val)
                elif sign == '-':
                    stack.append(-val)
                elif sign == '*':
                    stack.append(stack.pop()*val)
                elif sign == '/':
                    stack.append(int(stack.pop()/val))
                sign = c
                val = 0
                
        return sum(stack)
                
                
                
                
                
