from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.index1 = 0
        self.index2 = 0
        self.turn_odd = True

    def next(self) -> int:
        if self.turn_odd and self.index1 < len(self.v1):
            v = self.v1[self.index1]
            self.index1 += 1

        elif not self.turn_odd and self.index2 < len(self.v2):
            v = self.v2[self.index2]
            self.index2 += 1
        elif self.index2 < len(self.v2):
            v = self.v2[self.index2]
            self.index2 += 1
        else:
            v = self.v1[self.index1]
            self.index1 += 1

        self.turn_odd = not self.turn_odd
        return v

    def hasNext(self) -> bool:
        if self.index1 < len(self.v1) or self.index2 < len(self.v2):
            return True

        return False



v1 = [1,2]
v2 = [3,4,5,6]
i, v = ZigzagIterator(v1, v2), []
while i.hasNext(): v.append(i.next())
assert v == [1,3,2,4,5,6]
