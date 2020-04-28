from common.linked_list import build_linked_list


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if n <= 0 or not head:
            return head
        end = head

        for i in range(n):
            end = end.next

        current = head
        while end.next:
            current = current.next
            end = end.next

        current.next = current.next.next
        return head


lst = [7,3,10,1,4,8,11]
lnk_lst = build_linked_list(lst)

result = Solution().removeNthFromEnd(lnk_lst, 1)
assert (result.next.next.next.next.next.next is None)

result = Solution().removeNthFromEnd(lnk_lst, 3)
assert (result.next.next.next.next.value == 8)

assert(Solution().removeNthFromEnd(None, 1) == None)

assert(Solution().removeNthFromEnd(lnk_lst, -1) == lnk_lst)
