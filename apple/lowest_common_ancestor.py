# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root or not q or not p:
            return None

        def findPath(root, node, lst):

            if not root:
                return False
            if root and node and root.val == node.val:
                lst.append(root)
                return True

            if findPath(root.left, node, lst) or findPath(root.right, node, lst):
                lst.append(root)
                return True

            return False

        lst1 = []
        lst2 = []

        findPath(root, p,lst1)
        findPath(root, q, lst2)


        last_common = None
        for i in range(min(len(lst1), len(lst2))):
            if lst1[len(lst1) -1 - i].val == lst2[len(lst2) -1 -i].val:
                last_common = lst1[len(lst1) -1 - i]
            else:
                break

        return last_common





from common.binary_tree import build_binary_tree_T
a = build_binary_tree_T([1,2,3])
b = build_binary_tree_T([2])
c = build_binary_tree_T([3])

# p = Solution().lowestCommonAncestor(a,b, c)

fo = TreeNode(4)
sn = TreeNode(7)
e = TreeNode(8)
z = TreeNode(0)
s = TreeNode(6)
o = TreeNode(1)
f = TreeNode(5)
t = TreeNode(3)
tw = TreeNode(2)

tw.left = sn
tw.right =fo
f.left =s
f.right = tw
o.left =z
o.right=e
t.left =f
t.right =o

p = Solution().lowestCommonAncestor(t,f, fo)
assert p == f