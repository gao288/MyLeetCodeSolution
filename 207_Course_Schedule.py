from typing import *
class Solution:
    def __init__(self):
        self.graph = []
        self.v = []

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = [[] for x in range(numCourses)]
        for p in prerequisites:
            self.graph[p[0]].append(p[1])

        # 0 - not visited,  1 -- visiting , 2 -- visited
        self.v = [0] * numCourses

        for i in range(numCourses):
            if self.dfs(i):
                return False

        return True

    def dfs(self, i):
        if self.v[i] == 2:
            return False
        if self.v[i] == 1:
            return True
        self.v[i] = 1
        for e in self.graph[i]:
            if self.dfs(e):
                return True

        self.v[i] = 2
        return False
s = Solution()
print(s.canFinish(2,[[1,0],[0,1]]))
