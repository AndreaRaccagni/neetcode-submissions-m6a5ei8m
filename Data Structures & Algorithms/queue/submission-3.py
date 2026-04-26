class Node:
    def __init__(self, value = -1, prev = None, nxt = None):
        self.value = value
        self.prev = prev
        self.next = nxt

class Deque:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0
        
    def isEmpty(self) -> bool:
        return self.length == 0

    def append(self, value: int) -> None:
        node = Node(value)
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node
        self.length += 1

    def appendleft(self, value: int) -> None:
        node = Node(value)
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        self.length += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1 

        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        node.next = None
        node.prev = None
        self.length -= 1
        return node.value      

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        node.next = None
        node.prev = None
        self.length -= 1
        return node.value
