import random
from typing import  List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def Merge(arr1, arr2):
            ans = []
            i = 0
            j = 0

            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    ans.append(arr1[i])
                    i += 1
                else:
                    ans.append(arr2[j])
                    j += 1

            while i < len(arr1):
                ans.append(arr1[i])
                i += 1

            while j < len(arr2):
                ans.append(arr2[j])
                j += 1

            return ans

        def MergeSort(arr):

            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            return Merge(MergeSort(arr[:mid]), MergeSort(arr[mid:]))



assert Solution().sortArray([5,2,3,1]) == [1,2,3,5]
assert Solution().sortArray([5,1,1,2,0,0]) == [0,0,1,1,2,5]