from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def search(nums, target, s_index, e_index):

            if s_index == e_index and nums[s_index] == target:
                return s_index
            elif s_index >= e_index:
                return -1

            m_index = s_index + int((e_index - s_index) / 2)

            if nums[m_index] == target:
                return m_index

            if nums[s_index] <= nums[m_index]:
                if target >= nums[s_index] and target <= nums[m_index]:
                    return search(nums, target, s_index, m_index)
                else:
                    return search(nums, target, m_index+1, e_index)
            else:
                if target >= nums[m_index+1] and target <= nums[e_index]:
                    return search(nums, target, m_index+1, e_index)
                else:
                    return search(nums, target, s_index, m_index)

        return search(nums, target, 0, len(nums)-1)

assert Solution().search([5,1,3], 5) == 0

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print (Solution().search(nums, target))
assert Solution().search(nums, target) == 4


nums = [4,5,6,7,0,1,2]
target = 3
assert Solution().search(nums, target) == -1