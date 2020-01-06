class Solution:
    def findNumbers(self,nums):
        total = 0
        for n in nums:
            d = True
            while n > 0:
                n //= 10
                d = not d
            if d:
                total += 1
        return total

s = Solution()
print(s.findNumbers([555,901,482,1771]))
