import queue


class node:
    value = None
    right = None
    left = None

    def __init__(self, value):
        self.value = value


def build_binary_tree(lst= []):
    if not lst:
        return

    q = queue.Queue()
    root = node(lst[0])
    q.put(root)

    for i in range(1,len(lst)-1,2):
        parent = q.get()
        left = node(lst[i])
        right = node(lst[i+1])
        parent.left = left
        parent.right = right

        q.put(left)
        q.put(right)

    return root
