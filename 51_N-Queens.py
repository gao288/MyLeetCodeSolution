from typing import *
class Solution:
    def __init__(self):
        self.diagonal1 = None
        self.diagonal2 = None
        self.col = None
        self.ret = []
        self.n = 0
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.diagonal1 = set(x for x in range(2*n-1))
        self.diagonal2 = set(x for x in range(2*n-1))
        self.col = set(x for x in range(n))
        self.n = n
        self.solveN(n-1,[])
        return self.ret

    def solveN(self,count,s_array):
        if count== -1:
            self.ret.append(s_array[:])
            return
        row = self.n - count - 1
        for col in range(self.n):
            if (row+col not in self.diagonal1) or (col-row+self.n-1 not in self.diagonal2) or (col not in self.col):
                #can't place the queen here
                continue
            else:
                s_array.append("."*col + "Q" + "."*(self.n-col-1))
                self.diagonal1.remove(row+col)
                self.diagonal2.remove(col-row+self.n-1)
                self.col.remove(col)
                self.solveN(count-1,s_array)
                self.diagonal1.add(row+col)
                self.diagonal2.add(col-row+self.n-1)
                self.col.add(col)
                s_array.pop()
        return


s = Solution()
print(s.solveNQueens(4))