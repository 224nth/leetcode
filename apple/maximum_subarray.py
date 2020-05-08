from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        currentMax = nums[0]
        maxMax = nums[0]
        for i in range(1, len(nums)):
            currentMax = max(currentMax + nums[i], nums[i])
            maxMax = max(maxMax, currentMax)
        return maxMax


    def maxSubArrayV2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = nums.copy()
        for i in range(1, len(dp)):
            dp[i] = max(dp[i], dp[i-1]+dp[i])
        return max(dp)


assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert Solution().maxSubArrayV2([-2,1,-3,4,-1,2,1,-5,4]) == 6