class Node:

    def __init__(self, val, p = None):
        self.val = val
        self.next = p
        

class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.length = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value)

        if self.isEmpty():
            self.head = node
            self.tail = node
            node.next = node
        else:
            self.tail.next = node
            node.next = self.head
            self.tail = node

        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

        self.length -= 1
        return True

    def Front(self) -> int:
        return self.head.val if self.head else -1

    def Rear(self) -> int:
        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()