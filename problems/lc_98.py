from common.binary_tree import build_binary_tree


class Solution(object):
    def isValidBST(self, node):
        if not node:
            return True

        if node.left and node.left.value > node.value:
            return False
        if node.right and node.right.value < node.value:
            return False

        return self.isValidBST(node.left) and self.isValidBST(node.right)

lst = [7,3,10,1,4,8,11]
tree = build_binary_tree(lst)
assert(Solution().isValidBST(tree) == True)

lst = [2,1,1,1]
tree = build_binary_tree(lst)
assert(Solution().isValidBST(tree) == False)