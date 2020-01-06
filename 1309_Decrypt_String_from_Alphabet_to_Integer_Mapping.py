class Solution:
    def freqAlphabets(self, s: str) -> str:
        l = len(s)
        output = ""
        i = 0
        while i < l: 
            if i+2 < l and s[i+2] == "#":
                output += self.convert(int(s[i:i+2])) 
                i+=3
            else:
                output += self.convert(int(s[i])) 
                i+=1
        return output
    def convert(self,i):
        return chr(i+ord('a')-1)

test = Solution()
s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
print(test.freqAlphabets(s))
    