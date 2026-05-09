# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr = float('-inf')
        
        def inorder(node):
            nonlocal curr

            if not node:
                return True
            
            left = inorder(node.left)
            if not left:
                return False
            
            if node.val <= curr:
                return False
            curr = node.val

            return inorder(node.right)

        return inorder(root)