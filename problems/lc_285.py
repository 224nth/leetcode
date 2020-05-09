from problems.lc_297 import Codec


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':



        def find(root, p, parent):
            if p is None or root is None:
                return None

            if root.val == p.val:
                if root.right:
                    c = root.right
                    while c.left:
                        c = c.left

                    return c
                elif parent is not None:
                    return parent
                else:
                    return None

            a = find(root.left, p, root)
            if a is not None:
                return a

            b = find(root.right, p, parent)
            if b is not None:
                return b

        return find(root, p, None)






codec = Codec()

root = codec.deserialize("6,2,8,0,4,7,9,null,null,3,5")
assert  Solution().inorderSuccessor(root,TreeNode(2)).val == 3


root = codec.deserialize("5,3,6,1,4,null,null,null,2")
assert  Solution().inorderSuccessor(root,TreeNode(4)).val == 5


root = codec.deserialize("2,1,3")
assert  Solution().inorderSuccessor(root,TreeNode(1)).val == 2


root = codec.deserialize("5,3,6,2,4,null,null,1")
assert Solution().inorderSuccessor(root,TreeNode(6)) == None