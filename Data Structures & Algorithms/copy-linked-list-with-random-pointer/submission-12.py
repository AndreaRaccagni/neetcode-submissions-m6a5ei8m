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
        old = head
        new = dummy

        while old:
            node = Node(old.val)
            oldToNew[old] = node
            new.next = node
            new = new.next
            old = old.next

        for old, new in oldToNew.items():
            if not old.random:
                new.random = None
            else:
                new.random = oldToNew[old.random]

        return dummy.next
