# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prevVal = -1001
        
        def inorder(node):
            nonlocal prevVal
            if not node:
                return True
            
            left = inorder(node.left)
            if not left:
                return False

            if node.val <= prevVal:
                return False
            prevVal = node.val
 
            return inorder(node.right)
        
        return inorder(root)

        