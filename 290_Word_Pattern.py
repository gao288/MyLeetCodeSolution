class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m = {}
        
        _set = set()
        s_array = s.split()
        
        if len(pattern) != len(s_array):
            return False
        for i,c in enumerate(pattern):
            if c in m:
                if m[c] != s_array[i]:
                    return False
                    
                
            else:
                if s_array[i] in _set:
                    return False
                m[c] = s_array[i]
                _set.add(s_array[i])
        return True 


s = Solution()
s.wordPattern("abba","dog cat cat dog")