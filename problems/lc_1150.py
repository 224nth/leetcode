
from typing import List
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        c = nums.count(target)
        if c > len(nums)/2:
            return True
        return False

