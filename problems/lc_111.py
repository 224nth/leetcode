# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        if root.left is None or root.right is None:
            return 1 + max(self.minDepth(root.left, self.minDepth(root.right)))

        return 1 + min(self.minDepth(root.left) , self.minDepth(root.right))
