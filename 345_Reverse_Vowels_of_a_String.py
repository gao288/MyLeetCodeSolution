class Solution:
    def reverseVowels(self, s: str) -> str:
        m = set(["a","e","i","o","u","A","E","I","O","U"])
        ret1 = []
        ret2 = []
        i = 0
        j = len(s) - 1
        
        while(i <= j):
            if i == j:
                ret1.append(s[i])
                break
            if s[i] not in m:
                ret1.append(s[i])
                i+= 1
                
            elif s[j] not in m:
                ret2.append(s[j])
                j-= 1
                
            elif s[i] in m and s[j] in m:
                ret1.append(s[j])
                ret2.append(s[i])
                i+=1
                j-=1
            
        return "".join(ret1 + ret2[::-1]) 
                