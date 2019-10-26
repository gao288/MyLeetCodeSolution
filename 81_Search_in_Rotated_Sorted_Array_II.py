class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return False
        left = 0
        right = len(nums) - 1
        while(left < right):
            mid = (right + left) // 2
            if nums[mid] == nums[right]:
                if nums[mid] == target:
                    return True
                else:
                    right-=1
                    continue
            if nums[mid] >= nums[left]:  # left part is non-roated
                if target <= nums[mid] and target >= nums[left]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
                
                    
                
                
        return True if nums[left] == target else False