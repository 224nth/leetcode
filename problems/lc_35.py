class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:

        if not nums or target < nums[0]:
            return 0

        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)


print(Solution().searchInsert([1,3,5,6], 5))
print(Solution().searchInsert([1,3,5,6], 2))
print(Solution().searchInsert([1,3,5,6], 7))
print(Solution().searchInsert([1,3,5,6], 0))