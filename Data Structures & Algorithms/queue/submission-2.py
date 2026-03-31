class ListNode:
    
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        node = ListNode(value)
        last = self.tail.prev

        node.prev = last
        node.next = self.tail
        last.next = node
        self.tail.prev = node

    def appendleft(self, value: int) -> None:
        node = ListNode(value)
        first = self.head.next

        node.prev = self.head
        node.next = first
        first.prev = node
        self.head.next = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        last = self.tail.prev
        last.prev.next = self.tail
        self.tail.prev = last.prev
        return last.val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        first = self.head.next
        self.head.next = first.next
        first.next.prev = self.head
        return first.val
