from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:


        stack = []
        res = [0 for _ in range(len(T))]

        for i in range(len(T)):

            while stack and stack[-1][0] < T[i]:
                i_top = stack.pop()[1]
                res[i_top] = i - i_top

            stack.append([T[i], i])

        return res



assert Solution().dailyTemperatures([55,38,53,81,61,93,97,32,43,78]) == [3,1,1,2,1,1,0,1,1,0]
#assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
#assert Solution().dailyTemperatures([89,62,70,58,47,47,46,76,100,70]) == [8,1,5,4,3,2,1,1,0,0]