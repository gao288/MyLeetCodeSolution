from typing import *
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower-1] + nums + [upper+1]
        ret = []
        for n1, n2 in zip(nums,nums[1:]):
            if n1 >= n2 - 1:
                continue
            elif n1 == n2 - 2:
                ret.append(f"{n1+1}")
            else:
                ret.append(f"{n1+1}->{n2-1}")
        return ret