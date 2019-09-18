class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return
        #bottom up betterthan top down, top down每行开头和最后一个数需要另写判断
        #for loop 从倒数第二行往上直到第一行，步长-1
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]
