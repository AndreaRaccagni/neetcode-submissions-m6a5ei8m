# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = -1
        
        def inorder(node):
            nonlocal count
            nonlocal res

            if not node:
                return False

            if inorder(node.left):
                return True

            count += 1
            if count == k:
                res = node.val
            
            if inorder(node.right):
                return True

            return False

        inorder(root)

        return res