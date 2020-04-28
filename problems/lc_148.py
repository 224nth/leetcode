from common.linked_list import build_linked_list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """





arr = [2,5,3,1]
lst = build_linked_list(arr)
res = Solution().reorderList(lst)

print('a')