class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        carry = 0

        last = res

        while l1 or l2:
            ans = carry
            if l1:
                ans += l1.val
                l1 = l1.next
            if l2:
                ans += l2.val
                l2 = l2.next

            carry = ans // 10
            ans = ans % 10

            current = ListNode(ans)
            last.next = current

            last = current

        if carry > 0:
            last.next = ListNode(carry)
        return res.next
    