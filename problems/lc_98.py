import sys

from common.binary_tree import build_binary_tree


class Solution(object):




    def isValidBST(self, node):
        return self._isValidBST(node, sys.maxsize, - sys.maxsize -1)

    def _isValidBST(self, node, l, u):
        if not node:
            return True

        if node.left and not self._checkbound(node.left.value, l, node.value):
            return False
        if node.right and not self._checkbound(node.right.value, node.value, u):
            return False

        if not self.isValidBST(node.left) or not self.isValidBST(node.right):
            return False
        return True


    def _checkbound(self, n, l, u):
        if l <= n and n <= u:
            return True

        return False

lst = [7,3,10,1,4,8,11]
tree = build_binary_tree(lst)
assert(Solution().isValidBST(tree) == True)

lst = [2,1,1,1]
tree = build_binary_tree(lst)
assert(Solution().isValidBST(tree) == False)