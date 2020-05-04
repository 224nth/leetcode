import sys


class MinStack:

    min_so_far = sys.maxsize

    stack = []

    def __init__(self):
        """
        initialize your data structure here.
        """

    def push(self, x: int) -> None:

        if x < self.min_so_far:
            self.min_so_far = x

        self.stack.append([x, self.min_so_far])


    def pop(self) -> None:
        if self.stack:
            v =  self.stack.pop()
            if v[1] == self.min_so_far and self.stack:
                self.min_so_far = self.stack[len(self.stack)-1][1]


    def top(self) -> int:
        if self.stack:
            return self.stack[len(self.stack) -1][0]


    def getMin(self) -> int:
        return self.min_so_far

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)

param_4 = obj.getMin()
print(param_4)
obj.pop();
print(obj.top())
print(obj.getMin())