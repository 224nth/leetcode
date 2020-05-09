import sys

from common.binary_tree import build_binary_tree
from problems.lc_297 import Codec


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


codec = Codec()

root = codec.deserialize("7,3,10,1,4,8,11")
assert(Solution().isValidBST(root) == True)

tree = build_binary_tree("2,1,1,1")
assert(Solution().isValidBST(tree) == False)