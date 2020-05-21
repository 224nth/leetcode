class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def stretch(self, root, val):
        if not root:
            return

        def _stretch(root, val, is_left=True):
            if not root or not root.val:
                return

            res = root.val // val
            root.val = res
            temp_left = root.left
            temp_right = root.right

            if is_left:
                root.right = None
            else:
                root.left = None

            prev = root
            for i in range(1, val):
                next_node = TreeNode(res)
                if is_left:
                    prev.left = next_node
                else:
                    prev.right = next_node

                prev = next_node

            prev.left = temp_left
            prev.right = temp_right

            _stretch(temp_left, val, True)
            _stretch(temp_right, val, False)

        _stretch(root, val, True)


root = TreeNode(12)
eight_one = TreeNode(81)
root.left = eight_one
eight_one.right = TreeNode(56)

three_four = TreeNode(34)
three_four.left = TreeNode(19)
three_four.right = TreeNode(6)
root.right = three_four

Solution().stretch(root, 3)
print("done")


