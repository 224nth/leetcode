
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
