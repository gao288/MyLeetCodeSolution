class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) ==0 :
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        ret = []
        nums += [float('-inf')]
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                if nums[i-1] == start:
                    ret.append(str(start))
                else:
                    ret.append(str(start)+"->"+str(nums[i-1]))
                    
                start = nums[i]
                
        return ret
                
            