

# Definition for a binary tree node.
from typing import List

from problems.lc_297 import Codec


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        res = []
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
                res.append(element.val)
                odd = not odd
        return res


codec = Codec()
# str1= "1,2,3,None,5,None,4"
# node = codec.deserialize(str1)
# print(Solution().rightSideView(node))


str1= "1,2,3,4"
node = codec.deserialize(str1)
print(Solution().rightSideView(node))

print("done")