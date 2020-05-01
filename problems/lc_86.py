from typing import List

from common.linked_list import ListNode, build_linked_list_with_ListNode
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        if not head:
            return None

        less =[]
        more = []

        while head:
            if head.val < x:
                less.append(head)
            else:
                more.append(head)
            head = head.next

        new_lst = ListNode(-1)
        temp = new_lst

        for i, v in enumerate(less+more):
            temp.next = v
            temp = v

        temp.next = None

        return new_lst.next





node1 = build_linked_list_with_ListNode([1,4,3,2,5,2])
final = Solution().partition(node1, 3)
print(final)