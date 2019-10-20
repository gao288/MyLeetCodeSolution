
class Solution:
    def lengthOfLongestSubstring(self, s):
        has_seen = set()
        i = 0
        j = 0
        ret = 0
        while(j < len(s)):
            c = s[j]
            if c in has_seen:
                has_seen.remove(s[i])
                i += 1
            else:
                has_seen.add(c)
                ret = max(j-i+1,ret)
                j+=1
        return ret

s = Solution()
print(s.lengthOfLongestSubstring("abc"))
