class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:   # Slide Window
        if len(nums) == 0:
            return 0
        
        ptr1 = 0
        ptr2 = 0 
        _sum = nums[0]
        ret = float('inf')
        l = len(nums)
        while ptr2 < l:
            if _sum >= s:
                ret = min(ret,ptr2-ptr1+1)
                if ptr1 < ptr2:
                    _sum -= nums[ptr1]
                    ptr1 += 1 
                else:
                    ptr2 += 1
                    ptr1 = ptr2
                    if ptr2 < l:
                        _sum = nums[ptr2]
                        
            else:
                ptr2+=1
                if ptr2 < l:
                    _sum += nums[ptr2]
                 
            
        return 0 if ret == float('inf') else ret
            