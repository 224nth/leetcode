

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        map = {}

        def cloneG(node):
            if not node:
                return None

            if node in map:
                return map[node]


            clone_node = Node(node.val)
            map[node] = clone_node

            for n in node.neighbors:
                clone_node.neighbors.append(cloneG(n))

            return clone_node

        return cloneG(node)




o = Node(1)
t = Node(2)
th = Node(3)
f = Node(4)

o.neighbors = [t, f]
t.neighbors = [o, th]
th.neighbors= [t,f]
f.neighbors =[o, t]

b = Solution().cloneGraph(o)
print('done')




