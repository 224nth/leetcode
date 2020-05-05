# Definition for a binary tree node.
from common.binary_tree import build_binary_tree_T


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(1+self.maxDepth(root.left), 1+ self.maxDepth(root.right))


a = build_binary_tree_T([1,2,3,4])
b = build_binary_tree_T([])
c = build_binary_tree_T([1,2,3,5,6,7,8])
assert Solution().maxDepth(a) == 2
assert Solution().maxDepth(b) == 0
assert Solution().maxDepth(c) == 3