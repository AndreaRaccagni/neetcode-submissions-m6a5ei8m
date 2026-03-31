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

        for old, new in oldToNew.items():
            new.random = oldToNew.get(old.random) 

        return dummy.next

        