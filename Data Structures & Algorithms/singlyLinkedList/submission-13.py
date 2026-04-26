class Node:
    def __init__(self, value, nxt = None):
        self.value = value
        self.next = nxt

class LinkedList:
    
    def __init__(self):
        self.dummy = Node(-1)
        self.length = 0
        self.tail = self.dummy
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        curr = self.dummy.next

        for i in range(index):
            if not curr:
                return -1
            curr = curr.next

        return curr.value

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.dummy.next
        self.dummy.next = node
        if not self.length:
            self.tail = self.tail.next
        self.length += 1
        
    def insertTail(self, val: int) -> None:
        node = Node(val)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False

        prev = self.dummy
        for _ in range(index):
            prev = prev.next

        node = prev.next
        prev.next = node.next

        if node == self.tail:
            self.tail = prev

        node.next = None
        self.length -= 1
        return True
            

    def getValues(self) -> List[int]:
        curr = self.dummy.next
        res = []
        
        while curr:
            res.append(curr.value)
            curr = curr.next

        return res
