from typing import List


class Solution:
    def trap2(self, height: List[int]) -> int:
        if not height:
            return 0
        stack = []


        water = 0

        for i in range(len(height)):
            lh = 0
            while stack:
                item = stack.pop()
                water += (i - item[0]-1) * (min(item[1], height[i]) -lh)
                lh = max(lh, item[1])
                if item[1] >= height[i]:
                    stack.append(item)
                    break
            stack.append([i, height[i]])
        return water

    def trap2(self, arr):
        height, left, right, water = [], 0, 0, 0
        for i in arr:
            left = max(left, i)
            height.append(left)
        height.reverse()
        for n, i in enumerate(reversed(arr)):
            right = max(right, i)
            water += min(height[n], right) - i
        return water

    def trap(self, arr):
        if not arr:
            return 0

        left = right = water = 0
        i, j= 0, len(arr) - 1

        while i <= j:
            left = max(left, arr[i])
            right = max(right, arr[j])

            while i <= j and arr[i] <= left <= right:
                water += left - arr[i]
                i+=1

            while i <=j and arr[j] <= right <= left:
                water += right - arr[j]
                j -=1

        return water






assert Solution().trap([4,2,3]) == 1
assert Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
