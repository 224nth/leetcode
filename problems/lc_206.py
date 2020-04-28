from common.linked_list import build_linked_list

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        prev = head
        current = head.next
        prev.next =None

        while current:
            temp = current.next
            current.next = prev
            prev = current

            current = temp

        return prev


arr = [1,2,3,4]
lst = build_linked_list(arr)
res = Solution().reverseList(lst)
print('asdf')