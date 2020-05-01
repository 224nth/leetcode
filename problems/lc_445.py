from common.linked_list import ListNode, build_linked_list_with_ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        lst1 = []
        while l1:
            lst1.append(l1)
            l1= l1.next

        lst2 = []
        while l2:
            lst2.append(l2)
            l2 = l2.next

        last = None
        carry = 0

        while lst1 or lst2:
            result = carry
            if lst1:
                result += lst1.pop().val

            if lst2:
                result += lst2.pop().val


            carry = result // 10
            current = ListNode(result % 10)
            current.next = last
            last = current

        if carry:
            current = ListNode(carry)
            current.next = last
            last = current

        return last






node1 = build_linked_list_with_ListNode([7,2,4,3])
node2 = build_linked_list_with_ListNode([5,6,4])

final = Solution().addTwoNumbers(node1, node2)
print('done')