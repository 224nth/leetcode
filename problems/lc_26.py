class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return
        i = 1
        pos = 0

        while i < len(nums):
            if nums[pos] < nums[i]:
                pos = pos+1
                nums[pos] = nums[i]
            i = i + 1
        return pos+1

nums = [2,4,5,6,6,6,7,8,9]
pos = Solution().removeDuplicates(nums)
print(pos)
