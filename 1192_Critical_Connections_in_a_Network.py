#similar to Tarjan SSC(strongly connected components) but for finding bridges there is no need for a stack
from typing import *
from collections import defaultdict
# class Node:
#     def __init__(self,id):
#         self.id = id
#         self.link = []
#         self.visit = 0
#         self.lowlink = id
#     def add_links(self,l):
#         self.link.append(l)
    

class Solution:
    def __init__(self):
        self.lowlink = None
        self.visited = None
        self.dic = None
        self.rank = 0
        self.ranks = 0
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.lowlink = [0] * n 
        self.visited = [0] * n
        self.dic = defaultdict(lambda: [])
        self.ranks = [0] * n
        for c in connections:
            v0,v1 = c
            self.dic[v0].append(v1)
            self.dic[v1].append(v0)


        self.dfs(-1,0)
    
      
        ret = []
        for c in connections:
            _from , _to = c
            if self.ranks[_from] < self.lowlink[_to] or self.ranks[_to] < self.lowlink[_from]:
                ret.append(c)
        
        return ret
            
        
    def dfs(self,prenode,curr_node):

        if self.visited[curr_node] == 1:
            return self.lowlink[curr_node] 
        self.lowlink[curr_node] = self.rank
        self.ranks[curr_node] = self.rank
        self.rank += 1
        self.visited[curr_node] = 1
        for e in self.dic[curr_node]:
            if e != prenode:
                self.lowlink[curr_node] = min(self.lowlink[curr_node],self.dfs(curr_node,e))

        return self.lowlink[curr_node]

       

       


s = Solution()
# n = 9
# edges = [[1,6],[1,8],[6,8],[4,8],[4,3],[2,8],[2,5],[2,7],[7,0],[5,0]]
# for p in edges:
#     p[0]-=1
#     p[1]-=1
n = 4
edges = [[0,1],[1,2],[2,0],[1,3]]

print(s.criticalConnections(n,edges))