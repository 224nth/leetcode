# Definition for a binary tree node.
from common.binary_tree import build_binary_tree_T


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        pass


a = build_binary_tree_T([1,2,3,4])
b = build_binary_tree_T([])
c = build_binary_tree_T([1,2,3,5,6,7,8])
assert Solution().maxDepth(a) == 2
assert Solution().isSameTree(a) == 0
assert Solution().isSameTree(c) == 3