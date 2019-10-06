from typing import *
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(n):
            matrix.append([0]*n)

        x = 0
        y = 0
        num = 1
        while n > 0:
            num = self.fill_in_matrix(matrix,x,y,n,num)
            x+=1
            y+=1
            n-=2
    
       # self.fill_in_matrix(matrix,x,y,n,num)
  

        return matrix
        
    def fill_in_matrix(self,matrix,start_x,start_y,n,num):
        #fill the top row
        if n == 1:
            matrix[start_x][start_y] = num
        x = start_x
        y = start_y
        for _x,_y in [[0,1],[1,0],[0,-1],[-1,0]]:
            for i in range(0,n-1):
                matrix[x][y] = num
                num+=1
                x+=_x
                y+=_y

        return num
        

s = Solution()
print(s.generateMatrix(5))
        



    #    1  2  3  4
    #    12 13 14 5
    #    11 16 15 6
    #    10 9  8  7