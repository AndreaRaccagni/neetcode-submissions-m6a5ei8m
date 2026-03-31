
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummyNode = Node(-1)
        head2 = dummyNode
        refMap = {}

        while head:
            node = Node(head.val)
            head2.next = node
            head2 = head2.next
            refMap[head] = head2
            head = head.next
        
        for node1, node2 in refMap.items():
            node2.random = refMap.get(node1.random)
        
        return dummyNode.next


        


