# Definition for a binary tree node.
from problems.lc_297 import Codec


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        stack = [root]

        ans = []

        while len(stack) > 0:
            root = stack[-1]

            if root and root.left:
                stack.append(root.left)
                root.left = None
            elif root:
                ans.append(root.val)
                if k == len(ans):
                    return ans[-1]
                stack.pop()
                if root.right:
                    stack.append(root.right)
            else:
                stack.pop()





codec = Codec()

root = codec.deserialize("41,37,44,24,39,42,48,1,35,38,40,null,43,46,49,0,2,30,36,null,null,null,null,null,null,45,47,null,null,null,null,null,4,29,32,null,null,null,null,null,null,3,9,26,null,31,34,null,null,7,11,25,27,null,null,33,null,6,8,10,16,null,null,null,28,null,null,5,null,null,null,null,null,15,19,null,null,null,null,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23")
assert(Solution().kthSmallest(root,25) == 24)

root = codec.deserialize("1")
assert(Solution().kthSmallest(root,1) == 1)

root = codec.deserialize("3,1,4,None,2")
assert(Solution().kthSmallest(root,1) == 1)

root = codec.deserialize("5,3,6,2,4,None,None,1")
assert(Solution().kthSmallest(root, 3) == 3)
