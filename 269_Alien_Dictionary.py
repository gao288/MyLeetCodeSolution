class Solution:
    def alienOrder(self, words):
        graph = {}
        indegree = {}
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set() 
                    indegree[c] = 0
        prev_word = words[0]
        for i in range(1,len(words)):
            curr_word = words[i]
            for i in range(min(len(prev_word),len(curr_word))):
                prev_char = prev_word[i]
                curr_char = curr_word[i]
                if prev_char != curr_char: 
                    if curr_char not in graph[prev_char]:
                        graph[prev_char].add(curr_char)
                        indegree[curr_char] += 1
                    break
            prev_word = curr_word
        ret_str = self.topo_sort(indegree,graph)
        return "".join(ret_str) if len(indegree) == len(ret_str) else ""

    def topo_sort(self,indegree,graph):
        q = []
        for c in indegree.keys():
            if indegree[c] == 0:
                q.append(c)
        ret = []
        while(len(q) > 0):
            node = q.pop(0)
            ret.append(node)
            for go_to_node in graph[node]:
                val = indegree[go_to_node] - 1
                if val == 0:
                    q.append(go_to_node)
                indegree[go_to_node] = val

        return ret

s = Solution()
print(s.alienOrder(["wrt","wrf","er","ett","rftt","te"]))