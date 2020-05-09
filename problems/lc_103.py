
from typing import List

from problems.lc_297 import Codec


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        current = [root]
        ans = []
        level = 0

        while len(current) > 0:
            future = []

            temp = []
            for i in range(len(current)):

                node = current[i]
                if node:
                    temp.append(node.val)

                    future.append(node.left)
                    future.append(node.right)

            if temp and level %2 ==0:
                ans.append(temp)
            elif temp and level%2 ==1:
                ans.append((temp[-1::-1]))

            current = future
            level += 1

        return ans


codec = Codec()


root = codec.deserialize("3,9,20,None,None,15,7")

assert Solution().zigzagLevelOrder(root) == [[3],[20,9],[15,7]]