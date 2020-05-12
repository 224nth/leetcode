


# Definition for a binary tree node.
from problems.lc_297 import Codec


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> TreeNode:



        def getnum(str):

            sign = 1
            if str[0] == "-":
                sign =-1




codec = Codec()
node = codec.deserialize("4,2,3,1,6,5")
assert Solution().str2tree("4(2(3)(1))(6(5))") == node
