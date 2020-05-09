"""
# Definition for a Node.
"""
from problems.lc_297 import Codec


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        head = None
        last = None

        def inorder(root):
            nonlocal head
            nonlocal last

            if root is None:
                return

            inorder(root.left)

            node = Node(root.val)
            node.left = last
            if head is None:
                head = node

            if last is not None:
                last.right = node

            last = node


            inorder(root.right)



        inorder(root)
        if last:
            last.right = head
        if head:
            head.left = last
        return head




codec = Codec()

root = codec.deserialize("4,2,5,1,3")
val =  Solution().treeToDoublyList(root)


root = codec.deserialize("4,2,5,1,3")
val =  Solution().treeToDoublyList(root)

print("done")