import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        def sort_around_pivot(nums, rand_pivot, start, end):

            val = nums[rand_pivot]
            swap(nums, rand_pivot, start)
            pivot_post = start
            start += 1
            index = start

            while index <= end:

                if nums[index] < val:
                    swap (nums, index, start)
                    start += 1

                index += 1
            swap(nums, start-1, pivot_post)
            return start-1


        def findElement(nums, start, end):
            rand_pivot = random.randint(start, end)

            pivot = sort_around_pivot(nums, rand_pivot, start, end)
            return pivot


        find_index = len(nums) - k
        start = 0
        end = len(nums)-1
        while True:

            pivot = findElement(nums, start, end)

            if find_index  < pivot:
                end = pivot -1
            elif find_index > pivot:
                start = pivot + 1
            else:
                break

        return nums[find_index]


assert Solution().findKthLargest([3,2,1,5], k = 3) == 2

#print(Solution().findKthLargest([3,2,1,5,6,4], k = 2))
assert Solution().findKthLargest([3,2,1,5,4], k = 2) == 4
#assert Solution().findKthLargest([3,2,3,1,2,4,5,5,6], k = 4) == 4

