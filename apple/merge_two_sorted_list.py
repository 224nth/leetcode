from common.linked_list import build_linked_list_with_ListNode, ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:


        stack = []

        while l1 or l2:
            if l1 and l2 and l1.val < l2.val:
                stack.append(l1)
                l1 = l1.next
            elif l1 and l2:
                stack.append(l2)
                l2 = l2.next
            elif l1:
                stack.append(l1)
                l1 = l1.next
            else:
                stack.append(l2)
                l2 =l2.next

        current = None
        if len(stack) > 0:
            stack[len(stack)-1].next = None

        while stack:
            current = stack.pop()
            if stack:
                stack[len(stack)-1].next = current

        return current








node1 =build_linked_list_with_ListNode([1,3,5])

node2 = build_linked_list_with_ListNode([2, 4, 5])

a =Solution().mergeTwoLists(node1, node2)

print("done")
