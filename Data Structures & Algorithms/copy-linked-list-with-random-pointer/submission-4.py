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
        dummy = Node(-1)
        cur_new = dummy
        cur = head
        nodesMap = {}

        while cur:
            node = Node(cur.val)
            cur_new.next = node
            cur_new = cur_new.next
            nodesMap[cur] = cur_new
            cur = cur.next

        for old, new in nodesMap.items():
            new.random = nodesMap.get(old.random)

        return dummy.next