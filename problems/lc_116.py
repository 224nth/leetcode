"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from common.binary_tree import build_binary_tree


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if root is None:
            return root

        odd_level = [root]
        even_level = []
        return_root = root

        odd = True

        while len(odd_level) > 0 and len(even_level) > 0:

            if odd:
                current = odd_level.pop()
                if len(odd_level) > 0:
                    current.next = odd_level[-1]
                else:
                    odd = False
                even_level.append(current.left)
                even_level.append(current.right)
            else:
                current = even_level.pop()
                if len(even_level) > 0:
                    current.next = even_level[-1]
                else:
                    odd = True

                odd_level.append(current.left)
                odd_level.append(current.right)

        return return_root








tree = build_binary_tree([1,2,3,4,5,6,7])
new_node = Solution().connect(tree)
print("done")