import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

        closest = sys.maxsize

        for i in range(0, len(nums)):

            a = nums[i]
            s = i + 1
            l = len(nums) - 1

            while s < l:
                b = nums[s]
                c = nums[l]

                if  abs(target - (a + b + c)) < abs(target - closest):
                    closest = a+b+c
                    l -= 1
                    s += 1


                elif a + b + c > 0:
                    l -= 1
                else:
                    s += 1

        return closest


nums = [-1, 2, 1, -4]
target = 1

print(Solution().threeSumClosest(nums, target))


nums =[1,1,1,0]
target =100
print(Solution().threeSumClosest(nums, target))