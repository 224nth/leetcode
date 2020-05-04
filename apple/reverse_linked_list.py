


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from common.linked_list import build_linked_list_with_ListNode, ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        stack = []

        while head:
            stack.append(head)
            head = head.next

        newhead = ListNode(-1)
        last = newhead
        while stack:
            current =stack.pop()
            last.next = current
            current.next = None
            last = current


        return newhead.next







node =build_linked_list_with_ListNode([1,2,3,4,5])
a =Solution().reverseList(node)

print('done')