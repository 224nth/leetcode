from common.linked_list import build_linked_list


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        faster = head
        slower = head

        if faster.next and faster.next.next:
            faster = faster.next.next
            slower = slower.next









arr = [1,2,3,4]
lst = build_linked_list(arr)
res = Solution().reorderList(lst)

print('a')