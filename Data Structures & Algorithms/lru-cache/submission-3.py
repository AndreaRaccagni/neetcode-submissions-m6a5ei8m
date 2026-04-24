class Node:

    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def _insert(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.cache[node.key] = node 


    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        del self.cache[node.key]
        return node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self._remove(self.cache[key])
        self._insert(node)

        return self.cache[key].val


    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self._insert(node)

        if len(self.cache) > self.capacity:
            self._remove(self.head.next)


            