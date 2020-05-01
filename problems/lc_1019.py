import sys
from typing import List

from common.linked_list import ListNode, build_linked_list_with_ListNode


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:

        if not head:
            return []

        current = head
        stack = [[current.val, 0]]
        index = 0
        lst = [None]

        while current.next:
            index = index + 1
            lst.append(None)
            while stack and current.next.val > stack[len(stack) - 1][0] and not lst[stack[len(stack) - 1][1]]:
                lst[stack[len(stack) - 1][1]] = current.next.val
                stack.pop()

            stack.append([current.next.val, index])
            current = current.next

        while stack:
            a = stack.pop()
            lst[a[1]] = 0
        return lst

node1 = build_linked_list_with_ListNode([2,7,4,3,5])

final = Solution().nextLargerNodes(node1)
print(final)



node1 = build_linked_list_with_ListNode([1,7,5,1,9,2,5,1])

final = Solution().nextLargerNodes(node1)
print(final)

