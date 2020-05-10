import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:



        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp



        return nums[k]



#assert Solution().findKthLargest([3,2,1,5,6,4], k = 2) == 5
assert Solution().findKthLargest([3,2,3,1,2,4,5,5,6], k = 4) == 4

