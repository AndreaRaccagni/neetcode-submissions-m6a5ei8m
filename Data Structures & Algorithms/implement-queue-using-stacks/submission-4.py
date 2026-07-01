class MyQueue:

    def __init__(self):
        self.stack = []
        self.p = 0

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1

        tmp = self.stack[self.p]
        self.p += 1
        return tmp

    def peek(self) -> int:
        return self.stack[self.p]

    def empty(self) -> bool:
        return len(self.stack) == self.p


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()