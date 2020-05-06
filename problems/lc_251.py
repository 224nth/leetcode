from typing import List


class Vector2D:
    i = 0
    j = 0
    def __init__(self, v: List[List[int]]):
        self.v = v

    def next(self) -> int:
        a = self.v[self.i][self.j]
        self.j += 1
        if self.j == len(self.v[self.i]):
            self.i += 1
            self.j = 0
        return a


    def hasNext(self) -> bool:
        if self.i < (len(self.v) -1)  or (self.i == len(self.v)-1 and self.j < len(self.v[len(self.v)-1])):
            return True
        return False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()

iterator = Vector2D([[1,2],[3],[4]]);
v = []
while iterator.hasNext(): v.append(iterator.next())

assert v == [1,2,3,4]
