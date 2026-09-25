class ListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}

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
        return node.value


    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        
        if node:
            self._remove(node)
        
        newNode = ListNode(key, value)
        self._add(newNode)

        if self.size > self.capacity:
            last = self.head.next
            self._remove(last)
            

    def _add(self, node: ListNode) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node

        self.cache[node.key] = node
        self.size += 1


    def _remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

        del self.cache[node.key]
        self.size -= 1
