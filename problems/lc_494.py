
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        memo = {}

        def find(nums, s, index):

            if s == 0 and index == len(nums):
                return 1
            elif index >= len(nums):
                return 0

            key = str(s) +"#"+ str(index)
            if key in memo:
                return memo[key]
            else:

                num1 = find(nums, s+nums[index], index+1)
                num2 = find(nums, s-nums[index], index+1)
                memo[key] = num1+num2
                return num1 + num2

        return find(nums, S, 0)

#print(Solution().findTargetSumWays([1],1))
assert Solution().findTargetSumWays([1],1) == 1


print(Solution().findTargetSumWays([1, 1, 1],1))
assert Solution().findTargetSumWays([1, 1, 1],1) == 3

print(Solution().findTargetSumWays([1, 1, 1, 1, 1],3))
assert Solution().findTargetSumWays([1, 1, 1, 1, 1],3) == 5
