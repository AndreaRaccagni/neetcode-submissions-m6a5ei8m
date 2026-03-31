# Singly Linked List Node
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        if node.next == None:
            self.tail = node
        
    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        self.tail.next = node
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1
        
        if not curr or not curr.next:
            return False
        
        if curr.next.next == None:
            self.tail = curr

        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.head.next
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values