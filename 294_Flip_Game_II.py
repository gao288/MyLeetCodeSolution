# DFS with memorization
class Solution:
    def __init__(self):
        self.m = {}
    def canWin(self, s: str) -> bool:
        if s in self.m and self.m[s]:
            return True
        for i in range(0,len(s)-1):
            if s[i:i+2] == "++":
                temp = s[0:i] + "--" + s[i+2:]
                if (not self.canWin(temp)):
                    self.m[temp] = False
                    return True
                
                else:
                    self.m[temp] = True
                    
        return False
                