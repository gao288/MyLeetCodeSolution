#
# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#
from typing import *
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ret = []
        for i in range(1,k+1):
            ret = max(ret, self.maxNumber2(self.maxNumber1(nums1,i),self.maxNumber1(nums2,k-i)))
        
        return ret

    def maxNumber1(self,nums: List[int],k: int) -> List[int]:
        ret = []
        to_pop = len(nums) - k
        for n in nums:
            if len(ret) == 0:
                ret.append(n)
            else:
                while(to_pop > 0 and len(ret) > 0 and n > ret[-1]):
                    ret.remove(ret[-1])
                    to_pop-=1
                ret.append(n)
        return ret[:k]
    def maxNumber2(self,nums1:List[int],nums2:List[int]):
        ret = []
        while len(nums1) > 0 or len(nums2) > 0:
            if len(nums1) <= 0:
                ret.append(nums2)




s = Solution()
print(s.maxNumber1([4,6,2,3,1,1,1,7,8,4,1,1,1],4))
