from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        a = len(nums)
        n = a

        sum = n*(n+1)//2

        msum = 0
        for i in nums:
            msum += i

        return sum -msum


print(Solution().missingNumber([3,0,1]))

print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))

