from common.linked_list import build_linked_list


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        root, _ = self._rotateRight(head, head, k)
        return root

    def _rotateRight(self, node, head, k):
        if not node.next:
            node.next = head
            return node, k-1

        res, r = self._rotateRight(node.next, head, k)
        if r == 0:
            new_head = node.next
            node.next = None
            return new_head, r-1
        elif r < 0:
            return res, -1

        return node, r - 1




lst = [7,3,10,1,4,8,11]
lnk_lst = build_linked_list(lst)

result = Solution().rotateRight(lnk_lst, 1)
assert(result.value == 11)
assert(result.next.value == 7)

lnk_lst = build_linked_list(lst)
result = Solution().rotateRight(lnk_lst, 2)
assert(result.value == 8)
assert(result.next.value == 11)
assert(result.next.next.value == 7)
print('end')
#assert (result.next.next.next.next.next.next is None)