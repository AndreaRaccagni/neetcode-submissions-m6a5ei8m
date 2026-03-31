class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())

        front = self.stack2.pop()

        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

        return front

    def peek(self) -> int:
        if self.stack1:
            return self.stack1[0]
        return None

    def empty(self) -> bool:
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()