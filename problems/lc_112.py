# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common.binary_tree import build_binary_tree


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if sum == 0 and root is None:
            return True
        elif sum > 0 and root is None:
            return False
        elif sum < 0:
            return False

        if root.value:
            is_right = self.hasPathSum(root.right, sum - root.value)
            is_left = self.hasPathSum(root.left, sum - root.value)
            return  is_left or is_right
        return False




tree = build_binary_tree([5,4,8,11,None, 13,4,7,2, None,None,None,1])

print(Solution().hasPathSum(tree, 22))