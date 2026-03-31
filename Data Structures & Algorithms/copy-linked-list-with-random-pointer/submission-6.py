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
        p1 = head
        oldToNew = {}
        dummy = Node(-1)
        p2 = dummy
        
        while p1:
            node = Node(p1.val)
            oldToNew[p1] = node
            p2.next = node
            p1 = p1.next
            p2 = p2.next

        p1 = head
        p2 = dummy.next

        while p1:
            p2.random = oldToNew[p1.random] if p1.random else None
            p1 = p1.next
            p2 = p2.next

        return dummy.next

        