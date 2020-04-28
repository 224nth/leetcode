class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left_height = [0] * len(height)
        right_height = [0] * len(height)

        left_height[0] = height[0]
        for i in range(1, len(height)):
            left_height[i] = max(left_height[i-1], height[i])

        right_height[len(height) -1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            right_height[i] = max(height[i], right_height[i+1])

        result = 0
        for i in range(len(height)):
            result += min(right_height[i], left_height[i]) - height[i]

        return result
        # Driver program


assert (Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6)
