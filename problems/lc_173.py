# Definition for a binary tree node.
from problems.lc_297 import Codec


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    lst = []

    def __init__(self, root: TreeNode):

        def itr(root):
            if not root:
                return
            itr(root.left)
            self.lst.append(root.val)
            itr(root.right)

        itr(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.lst.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.lst) > 0


root = Codec().deserialize("7,3,15,None,None,9,20")

# Your BSTIterator object will be instantiated and called as such:
obj = BSTIterator(root)
v = []
while obj.hasNext(): v.append(obj.next())

assert(v == [3,7,9,15,20])