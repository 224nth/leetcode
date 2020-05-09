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

        stack = [root]

        ans = []

        while len(stack) > 0:
            root = stack[-1]

            if root and root.left:
                stack.append(root.left)
                root.left = None
            elif root:
                ans.append(root.val)
                stack.pop()
                if root.right:
                    stack.append(root.right)
            else:
                stack.pop()

        return ans



codec = Codec()


root = codec.deserialize("1,None,2,3")

assert Solution().inorderTraversal(root) == [1,3,2]