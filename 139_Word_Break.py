class Solution:
    def wordBreak(self, s, wordDict):
        wordsdic = set(wordDict)
        dp = {"":True}
        return self.wordB(s,wordsdic,dp)

    def wordB(self,s,wordsdic,dp):
        if s in dp:
            return dp[s]
        ret = False
        for i in range(len(s)):
            temp = self.wordB(s[:i],wordsdic,dp) and (s[i:] in wordsdic)
            ret = ret or temp
        
        dp[s] = ret

        return ret



s = Solution()
st = "applepenapple"
wordDict = ["apple","pen"]
print(s.wordBreak(st,wordDict))
