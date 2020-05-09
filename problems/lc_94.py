# Definition for a binary tree node.
from typing import List

from problems.lc_297 import Codec


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        stack = []

        ans = []

        if root:
            stack.append(root)
        while len(stack) > 0:

            current = stack.pop()

            ans.append(current.val)

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

        return ans



codec = Codec()


root = codec.deserialize("1,None,2,3")

assert Solution().preorderTraversal(root) == [1,2,3]