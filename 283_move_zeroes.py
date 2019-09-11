class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        curr = 0
        while curr < len(nums):
            if nums[curr] != 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                
                p0 += 1
            
            curr += 1
        return 
