class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list_with_ListNode(lst= []):

    if not lst:
        return

    start = ListNode(lst[0])
    current = start
    for i in lst[1:]:
        temp = ListNode(i)
        current.next = temp

        current = temp

    return start

class node:
    value = None
    next = None

    def __init__(self, value):
        self.value = value


def build_linked_list(lst= []):

    if not lst:
        return

    start = node(lst[0])
    current = start
    for i in lst[1:]:
        temp = node(i)
        current.next = temp

        current = temp

    return start
