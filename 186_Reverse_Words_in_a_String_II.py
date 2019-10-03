from tpying import *
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s,0,len(s)-1)
        
        s.append(" ")
        start = 0
        for i in range(len(s)):
            if s[i] == " ":
                self.reverse(s,start,i-1)
                start = i+1 
        
        s.pop()
        
    def reverse(self,s,i,j):
        while(i < j):
            temp = s[i]        
            s[i] = s[j]
            s[j] = temp
            i+=1
            j-=1
        