# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0
        
        def maxDepth(node):
            nonlocal maxDiam
            if not node:
                return 0

            left = maxDepth(node.left)
            right = maxDepth(node.right)

            maxDiam = max(left + right, maxDiam)
            return 1 + max(left, right)

        maxDepth(root)
        return maxDiam