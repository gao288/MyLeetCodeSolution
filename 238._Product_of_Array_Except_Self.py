class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) ==0:
            return 0
        
        length = len(nums)
        l = [1] * length
        r = [1] * length
        for i in range(1,length):
            l[i] = nums[i-1] * l[i-1]
            r[length-i-1] = nums[length-i] * r[length-i]

        for i in range(0,length):
            l[i] *= r[i]

        return l
