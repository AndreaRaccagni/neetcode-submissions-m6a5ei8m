# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = deque([root])
        h = 0

        while stack:
            l = len(stack)
            for _ in range(l):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            
            h += 1

        return h
                
