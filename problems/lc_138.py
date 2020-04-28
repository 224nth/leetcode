from common.linked_list import build_linked_list



class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """


        if not head:
            return None

        store = {}

        new_current = Node(head.val, None, None)
        new_head = new_current
        old_current = head

        store[old_current]= new_current

        while old_current.next:

            new_next = Node(old_current.next.val, None, None)
            new_current.next = new_next

            store[old_current.next] = new_next

            new_current = new_next
            old_current = old_current.next

        new_current = new_head

        while head:
            if head.random:
                new_current.random = store[head.random]
            head = head.next
            new_current = new_current.next

        return new_head




head = [[7,None],[13,0],[11,4],[10,2],[1,0]]

node0 = Node(7, None, None)
node1= Node(13, None, None)
node2= Node(11, None, None)
node3= Node(10, None, None)
node4= Node(1, None, None)

node0.next= node1
node1.next = node2
node2.next = node3
node3.next=node4
node1.random = node0
node2.random=node4
node3.random =node2
node4.random =node0


res = Solution().copyRandomList(node0)
assert (head == res)
