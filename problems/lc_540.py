class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return self.__singleNonDuplicate(nums, 0, len(nums)-1)

    def __singleNonDuplicate(self, nums, start, end):

        mid = (end-start) / 2
        if nums[mid] < nums[mid+1] and nums[mid] > nums[mid-1]:
            return nums[mid]

        if nums[mid] == nums[mid-1]:
            return self.__singleNonDuplicate(nums, 0, mid - 1)

        if nums[mid] == nums[mid + 1]:
            return self.__singleNonDuplicate(nums, mid + 1, len(nums) - 1)




arr =[1,1,2,3,3,4,4,8,8]
assert (Solution().singleNonDuplicate(arr) == 2)

arr = [3,3,7,7,10,11,11]
assert (Solution().singleNonDuplicate(arr) == 10)