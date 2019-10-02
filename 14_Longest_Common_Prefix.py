class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        ret = strs[0]
        j = len(ret)
        for s in strs[1:]:
            for i in range(min(len(s),j)):
                if s[i] != ret[i]:
                    j = i
                    break
            j = min(len(s),j)        
        return ret[:j]