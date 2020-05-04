
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()

        for j in range(len(nums)-3):
            d = nums[j]
            for i in range(j+1, len(nums)-2):
                a = nums[i]
                s = i + 1
                l = len(nums) - 1
                while s < l:
                    b = nums[s]
                    c = nums[l]
                    if a + b + c + d == target:
                        ans.add((d, a, b, c))
                        l -= 1
                        s += 1
                    elif a + b + c+d > target:
                        l -= 1
                    else:
                        s += 1

        return list(ans)

nums = [-3,-2,-1,0,0,1,2,3]
print(Solution().fourSum(nums, 0))