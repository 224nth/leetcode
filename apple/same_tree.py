from common.binary_tree import build_binary_tree_T


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        elif q and not p:
            return False
        elif p and not q:
            return False

        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True

        return False



a = build_binary_tree_T([1,2,3,4])
b = build_binary_tree_T([])
c = build_binary_tree_T([1,2,3,5])
# assert Solution().isSameTree(a,a) == True
# assert Solution().isSameTree(a,b) == False
assert Solution().isSameTree(a,c) == False
