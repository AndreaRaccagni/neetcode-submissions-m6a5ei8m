# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxParent):
            if not node:
                return 0

            count = 1 if node.val >= maxParent else 0

            maxParent = max(maxParent, node.val)

            count += dfs(node.left, maxParent)
            count += dfs(node.right, maxParent)

            return count
        
        return dfs(root, -float('infinity'))
        

