"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapNodes = {}

        def dfs(node):
            if not node:
                return

            if node in mapNodes:
                return mapNodes[node]

            newNode = Node(node.val)
            mapNodes[node] = newNode
            
            newNode.neighbors = []
            
            for n in node.neighbors:
                newNode.neighbors.append(dfs(n))

            return newNode

        return dfs(node)


         