from typing import *
class Solution:
    def __init__(self):
        self.graph = []
        self.v = []
        self.order = []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = [[] for x in range(numCourses)]
        self.v = [0] * numCourses
        for p in prerequisites:
            self.graph[p[0]].append(p[1])
        for i in range(numCourses):
            if self.dfs(i):
                return []

        return self.order

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
        self.order.append(i)
        return False

s = Solution()
print(s.findOrder(2,[[1,0]]))