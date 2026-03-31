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
        nodes = {}
        dummy = Node(-1)
        newCurr = dummy
        curr = head

        while curr:
            node = Node(curr.val)
            newCurr.next = node
            nodes[curr] = node
            newCurr = newCurr.next
            curr = curr.next

        for old, new in nodes.items():
            new.random = nodes.get(old.random)

        return dummy.next




