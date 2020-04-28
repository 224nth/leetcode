from common.linked_list import build_linked_list
from common.linked_list import node

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return
        dummy = node(-1)
        dummy.next =head
        fast = dummy
        slow = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


arr = [2,5,3,4]
lst = build_linked_list(arr)
res = Solution().middleNode(lst)

print('a')