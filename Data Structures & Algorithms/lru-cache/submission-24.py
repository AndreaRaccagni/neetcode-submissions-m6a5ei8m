class ListNode:

    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add(node)
            return
        
        newNode = ListNode(key, value)
        self.cache[key] = newNode
        self._add(newNode)

        if len(self.cache) > self.capacity:
            nodeToRemove = self.tail.prev
            self._remove(nodeToRemove)
            del self.cache[nodeToRemove.key]

    def _add(self, node: ListNode) -> None:
        nxt = self.head.next
        node.next = nxt
        node.prev = nxt.prev
        self.head.next = node
        nxt.prev = node
        
    def _remove(self, node: ListNode) -> None:
        prev = node.prev
        nxt = node.next
        prev.next = node.next
        nxt.prev = node.prev