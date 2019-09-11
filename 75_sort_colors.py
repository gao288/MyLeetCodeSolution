class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1
        curr = 0
        while(curr <= p2):
            if nums[curr] == 1:
                curr+=1
            elif nums[curr] == 2:
                self.swap(nums,curr,p2)
                #curr+=1
                p2-=1
            elif nums[curr] == 0:
                self.swap(nums,curr,p0)
                curr += 1
                p0 +=1
                
    def swap(self, nums,x,y):
        temp = nums[x]
        nums[x] = nums[y]
        nums[y] = temp
