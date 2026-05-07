class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.nodes = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        value = node.val
        self._remove(key)
        self._insert(key, value)

        return value


    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self._remove(key)

        if self.size == self.capacity:
            self._remove(self.head.next.key)

        self._insert(key, value)
    

    def _insert(self, key, value) -> None:
        node = Node(key,value)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

        if key not in self.nodes:
            self.size += 1

        self.nodes[key] = node


    def _remove(self, key: int) -> bool:
        if key not in self.nodes:
            return False

        node = self.nodes[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

        self.size -= 1
        del self.nodes[key]
        
        return True
