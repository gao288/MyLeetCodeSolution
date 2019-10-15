class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic1 = {}
        for s in strings:
            temp_s = []
            offset = s[0]
            for c in s:
                calculate = ord(c) - ord(offset)
                if calculate < 0:
                    calculate += 26
                temp_s.append(calculate)
                
            temp_s = tuple(temp_s)
            if temp_s in dic1:
                dic1[temp_s].append(s)
            else:
                dic1[temp_s]=[s]
                
        ret = []
        for key in dic1.keys():
            ret.append(dic1[key])
            
        return ret

