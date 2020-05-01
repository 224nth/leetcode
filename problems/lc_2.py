# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from common.linked_list import build_linked_list, node


class Solution:
    def addTwoNumbers(self, l1: node, l2: node) -> node:

        res = node(-1)
        carry =0

        last = res

        while l1 or l2:
            ans = carry
            if l1:
                ans += l1.value
                l1 = l1.next
            if l2:
                ans += l2.value
                l2 = l2.next

            carry = ans // 10
            ans = ans % 10

            current = node(ans)
            last.next = current

            last = current

        if carry > 0:
            last.next = node(carry)
        return res.next




lst1 = build_linked_list([2,4,3])
lst2 = build_linked_list([5,6,4])

a = Solution().addTwoNumbers(lst1, lst2)


print("done")