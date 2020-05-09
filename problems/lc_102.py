
from typing import List

from problems.lc_297 import Codec


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        current= [root]
        ans =[]

        while len(current) > 0:
            future = []

            temp = []
            for i in range(len(current)):

                node = current[i]
                if node:
                    temp.append(node.val)

                    future.append(node.left)
                    future.append(node.right)

            if temp:
                ans.append(temp)

            current = future

        return ans


codec = Codec()


root = codec.deserialize("3,9,20,None,None,15,7")

assert Solution().levelOrder(root) == [[3],[9,20],[15,7]]