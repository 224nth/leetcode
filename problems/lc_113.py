# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common.binary_tree import build_binary_tree


class Solution(object):
    def hasPathSum(self, root, sum):
        self._hasPathSum(root, sum, [])



    def _hasPathSum(self, root, sum, path):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if sum ==0 and root is None:
            print(path)
            return
        elif sum > 0 and root is None:
            return
        elif sum < 0 or root is None:
            return

        path.append(root.value)
        self._hasPathSum(root.right, sum-root.value, path)
        self._hasPathSum(root.left, sum -root.value, path)
        path.pop()





tree = build_binary_tree([5,4,8,11,None, 13,4,7,2, None,None,None,1])

print(Solution().hasPathSum(tree, 22))