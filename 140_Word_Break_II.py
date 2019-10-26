class Solution:
    def wordBreak(self,s,wordDict):
        words = set(wordDict)
        mem = {}
        def wordB(s):
            if s in mem:
                return mem[s]
            ans = []
            if s in words:
                ans.append(s)
            for i in range(1,len(s)):
                right_part = s[i:]
                if right_part not in words:
                    continue
                ans += [w + " " + right_part for w in wordB(s[0:i])]
            mem[s] = ans
            return mem[s]
        return wordB(s)
s = Solution()
# st = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
st = "aa"
wordDict = ["a"]
print(s.wordBreak(st,wordDict))


        
    