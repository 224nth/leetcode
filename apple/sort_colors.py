from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        start = 0
        end = len(nums) - 1

        index = 0

        while index <= end:
            if nums[index] == 0 and index > start:
                nums[index] = nums[start]
                nums[start] = 0
                start += 1
            elif nums[index] == 2 and index < end:
                nums[index] = nums[end]
                nums[end] = 2
                end -= 1
            else:
                index += 1
        return nums

assert Solution().sortColors([0,1,0]) == [0,0,1]
assert Solution().sortColors([2,0,1]) == [0,1,2]
assert Solution().sortColors([2,0,2]) == [0,2,2]

assert Solution().sortColors([2,0,2,1,1,0]) == [0,0,1,1,2,2]
