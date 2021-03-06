
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from common.binary_tree import build_binary_tree


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return []

        odd = True

        lst_even = []
        lst_odd = [root]

        while len(lst_even) > 0 or len(lst_odd) > 0:
            if odd:
                current_lst = lst_odd
                next_lst = lst_even
            else:
                current_lst = lst_even
                next_lst = lst_odd

            element = current_lst.pop(0)
            if element and element.left:
                next_lst.append(element.left)
            if element and element.right:
                next_lst.append(element.right)

            if len(current_lst) == 0:
                element.next = None
                odd = not odd
            else:
                element.next = current_lst[0]

        return root








tree = build_binary_tree([1,2,3,4,5,6,7], Node)
new_node = Solution().connect(tree)
print("done")