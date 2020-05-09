from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def preorder(self, root: 'Node') -> List[int]:


        ans = []

        def preorder(root):
            if not root:
                return

            ans.append(root.val)
            for n in root.children:
                preorder(n)

        preorder(root)
        return ans


