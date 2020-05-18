from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        cc =0
        for i in range(len(nums)):
            if cc ==0:
                ce = nums[i]
                cc=1
            elif nums[i] != ce:
                cc -=1
            else:
                cc +=1

        return ce


assert Solution().majorityElement([6,5,5]) == 5
assert Solution().majorityElement([3,2,3]) == 3
assert Solution().majorityElement([2,2,1,1,1,2,2])  == 2