class CustomStack:

    stack = []

    def __init__(self, maxSize: int):
        self.maxsize = maxSize
        self.stack = []

    def push(self, x: int) -> None:

        if len(self.stack) < self.maxsize:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if len(self.stack) >0 else -1

    def increment(self, k: int, val: int) -> None:

        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(2)
obj.push(34)
print(obj.pop())

obj.push(2)
obj.push(3)
obj.push(4)
obj.increment(5, 100)
obj.increment(2, 100)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
# param_2 = obj.pop()
# obj.increment(k,val)