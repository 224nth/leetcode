import queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return

        lst = data.split(",")

        if not lst:
            return

        q = queue.Queue()
        root = TreeNode(lst[0])
        q.put(root)

        for i in range(1, len(lst) - 1, 2):
            parent = q.get()
            left = None
            right = None

            if lst[i] != 'None':
                left = TreeNode(lst[i])
                q.put(left)
            if lst[i+1] != 'None':
                right = TreeNode(lst[i + 1])
                q.put(right)
            parent.left = left
            parent.right = right




        return root
