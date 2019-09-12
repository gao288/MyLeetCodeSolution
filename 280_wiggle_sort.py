class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums,i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        
        for i,_ in enumerate(nums):
            if i < len(nums) - 1:
                if (i%2 == 0) == (nums[i] > nums[i+1]):
                    swap(nums,i,i+1)
