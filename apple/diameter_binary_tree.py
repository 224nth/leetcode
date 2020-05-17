from problems.lc_297 import Codec


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        if not root:
            return 0

        def get_height(root):
            if not root:
                return 0

            return 1+ max(get_height(root.left), get_height(root.right))


        lh = get_height(root.left)
        rh = get_height(root.right)
        rdd = lh+rh


        ld = self.diameterOfBinaryTree(root.left)
        rd = self.diameterOfBinaryTree(root.right)

        return max(rdd, max(ld, rd))

c = Codec()
root = c.deserialize("1,2,3,4,5")
print(Solution().diameterOfBinaryTree(root))
