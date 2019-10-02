# this solution uses KMP algorithm.
from typing import *;
class Solution:
    def strStr(self, haystack: str, needle: str)-> int:
        if len(needle) == 0:
            return 0
        
        ips = self.produce_ips_array(needle)
        i = 0
        j = 0
        while(i < len(haystack)):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
                if j == len(needle):
                    return i-j
            else:
                if j > 0:
                    j = ips[j-1]
                else:
                    i+=1



        return -1;
    def produce_ips_array(self,s):
        l = len(s)
        prefix = 0
        ips = [0]* l
        i = 1
        while(i<l):
            if s[i] == s[prefix]:
                prefix += 1
                ips[i] = prefix 
                i += 1
            else:
                if prefix != 0:
                    prefix = ips[prefix - 1]
                else:
                    ips[i] = 0
                    i+=1

        return ips




s = Solution()

print(s.strStr("hello","bc"))
# abababababc
# abababc
# 0012120