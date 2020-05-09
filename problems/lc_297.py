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

        if not root:
            return ""

        lst = []

        q = queue.Queue()

        q.put(root)
        while not q.empty():
            node = q.get()
            if node is not None:
                lst.append(node.val)
                q.put(node.left)
                q.put(node.right)
            else:
                lst.append(None)


        while True:
            if lst[len(lst)-1] is None:
                lst.pop()
            else:
                break

        ans = ""
        for i in range(len(lst)):
            if i == len(lst) -1:
                ans += str(lst[i])
            else:
                ans += str(lst[i])+","

        return ans



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if data == "":
            return None

        q = queue.Queue()

        # change it back to lst with proper values
        lst = data.split(',')
        for i in range(len(lst)):
            if lst[i] != 'None' and lst[i] != 'null':
                lst[i] = int(lst[i])
            else:
                lst[i] = None


        head = TreeNode(lst[0])
        q.put(head)

        index =1

        def join(node, index, is_left=True):

            if index < len(lst):
                if lst[index] is not None:
                    child = TreeNode(lst[index])
                    if is_left:
                        node.left = child
                    else:
                        node.right = child
                    q.put(child)
                else:
                    q.put(None)
                index += 1

            return index

        while not q.empty():
            root = q.get()
            if root is not None:
                index = join(root, index, is_left=True)
                index = join(root, index, is_left=False)

        return head


# codec = Codec()
#
#
#
# str1 = "-1,0,1"
#
# a = codec.serialize(codec.deserialize(str1))
#
# print('root')
# a = codec.deserialize(codec.serialize(None))
#
# str1 = "2,3,4,None,None,2,4,6"
# root = Codec().deserialize(str1)
#
# str_back = Codec().serialize(root)
#
# print(str1)
# print(str_back)
# assert  str1 == str_back
#




