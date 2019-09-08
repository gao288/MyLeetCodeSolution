from typing import *
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        left_product = 1
        right_product = 1
        max_product = float('-inf')
        for i in range(l):
            left_product *= nums[i]
            right_product *= nums[l-i-1]
            max_product = max(max_product,left_product)
            max_product = max(max_product,right_product)
            if left_product == 0:
                left_product = 1
            if right_product == 0:
                right_product = 1
        

        return max_product

S = Solution()
print(S.maxProduct([1,6,5,-3,0,9]))
