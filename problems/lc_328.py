from common.linked_list import build_linked_list


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = head.next

        while even.next:
            odd_next = odd.next.next
            even_next = even.next.next

            odd.next = odd_next
            even.next = even_next

            odd = odd.next
            even = even.next

        odd.next = even_head

        return head





lst = [1,2,3,4,5,6]
node = build_linked_list(lst)
res = Solution().oddEvenList(node)

assert(res.next.value ==3)
assert(res.next.next.value ==5)
assert (res.value == 1)
assert(res.next.next.next.value ==2)