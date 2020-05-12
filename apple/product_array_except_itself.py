from typing import  List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        preLst =[[1] for i in range(len(nums))]
        postLst = [[1] for i in range(len(nums))]
        lst = [[1] for i in range(len(nums))]

        st = 1
        for i in range(0, len(nums)):
            preLst[i] = st
            st = st * nums[i]

        st = 1
        for i in range(len(nums)-1,-1,-1):
            postLst[i] = st
            st = st * nums[i]


        for i in range(0, len(nums)):
            lst[i] = preLst[i] *postLst[i]

        return lst


assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]

