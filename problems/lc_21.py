from common.linked_list import build_linked_list

from common.linked_list import node

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = node(-1)
        current = dummy

        while l1 and l2:
            if l1.value < l2.value:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next =l1
        if l2:
            current.next = l2

        return dummy.next


arr1 = [2,5,8]
lst1 = build_linked_list(arr1)


arr2 = [1,9,10,12]
lst2 = build_linked_list(arr2)

res = Solution().mergeTwoLists(lst1, lst2)

print('a')