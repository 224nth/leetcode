from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children




class Solution:

    res = []

    def postorder(self, root: 'Node') -> List[int]:

        if root is None:
            return
        if root.children:
            for child in root.children:
                self.postorder(child)

        self.res.append(root.val)

        return self.res


one = Node(1)

three = Node(3)
two = Node(2)
four = Node(4)
one.children = [three, two, four]
five = Node(5)
six = Node(6)

three.children = [five, six]



print(Solution().postorder(one))