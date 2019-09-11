from typing import *
class Solution:                 #using dp
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if (len(nums) < 2):
            return len(nums)
        high = 1
        low = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                high=low+1
            elif nums[i] < nums[i-1]:
                low=high+1
                
        return max(high,low)
            
        
