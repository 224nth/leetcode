import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

        closest = 2**31

        for i in range(0, len(nums)):

            a = nums[i]
            s = i + 1
            l = len(nums) - 1

            while s < l:
                b = nums[s]
                c = nums[l]

                if abs(target - (a + b + c)) < abs(target - closest):
                    closest = a+b+c

                if target > a + b + c:
                    s += 1
                else:
                    l -= 1

        return closest



assert  Solution().threeSumClosest([0,2,1,-3], 1) == 0
nums = [-1, 2, 1, -4]
target = 1

assert Solution().threeSumClosest(nums, target) == 2


nums =[1,1,1,0]
target =100
assert Solution().threeSumClosest(nums, target) == 3