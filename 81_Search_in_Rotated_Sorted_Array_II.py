class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def find_start_i(l,r):
            while l < r:
                m = (l + r) // 2 
                if(nums[m] > nums[r]):
                    l = m + 1
                elif(nums[m] < nums[r]):
                    r = m
                else:
                    if nums[r-1] > nums[r]:
                        l = r
                        break;
                    r -=1
                    
            return l
        def bs(l,r):
            while(l <= r):
                m = (l+r)//2
                if nums[m] == target:
                    return True
                else:
                    if target < nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
            return False     

        if len(nums) == 0:
            return False
        if len(nums) == 1:
            if nums[0] == target:
            
                return True
            else:
                return False
        index = find_start_i(0,len(nums)-1)
        if(target<= nums[len(nums)-1]): 
            return bs(index,len(nums)-1)
        else:
            return bs(0,index)
