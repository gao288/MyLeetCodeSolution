class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = 0
        longest = ""
        for i in range(len(s)):
            temp = self.getPalindrome(s,i,i)
            if ret < temp[0]:
                longest = temp[1]
                ret = temp[0]
            temp = self.getPalindrome(s,i,i+1)
            if ret < temp[0]:
                longest = temp[1]
                ret = temp[0]
            
            
        return longest
    def getPalindrome(self, s,left,right):
        while(left>=0 and right < len(s)):
            if s[left] == s[right]:
                left -=1
                right +=1
            else:
                break
        return (right - left + 1 - 2,s[left+1:right])