"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}
        dummy = Node(-1)
        new = dummy
        old = head

        while old:
            node = Node(old.val)
            oldToNew[old] = node
            new.next = node
            new = new.next
            old = old.next

        for old, new in oldToNew.items():
            new.random = oldToNew[old.random] if old.random else None

        return dummy.next
        