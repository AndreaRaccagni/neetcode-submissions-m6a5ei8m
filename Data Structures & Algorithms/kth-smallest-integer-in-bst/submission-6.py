# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        val = 0

        def inorder(node):
            nonlocal count
            nonlocal val

            if not node:
                return False
            
            if inorder(node.left):
                return True

            count += 1
            if count == k:
                val = node.val

            if inorder(node.right):
                return True

        inorder(root)
        return val

