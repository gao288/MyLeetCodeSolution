from __future__ import division
class Solution:
    def numberToWords(self, num):
        
        level = ["Billion","Million","Thousand"]
        one = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"] 
        hundred = ["","One Hundred","Two Hundred","Three Hundred","Four Hundred","Five Hundred","Six Hundred","Seven Hundred","Eight Hundred","Nine Hundred"]
        tenth = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        level_choose = [one, tenth, hundred]
        level_counter = 0
        ret = []
        while(num > 0):
            remainder,num = num % 1000, num // 1000
            temp = []
            for i in range(3):
                h_remainder, remainder = remainder % 10, remainder // 10
                temp.insert(0,level_choose[i][h_remainder])
            ret = temp + ret
            if num != 0:
                ret = [level.pop()] + ret
            
        return " ".join(ret)

s = Solution()
print(s.numberToWords(12345))
        