# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(p, q):
            if not p and not q:
                return None
            
            val1 = p.val if p else 0
            val2 = q.val if q else 0

            node = TreeNode(val1 + val2)
            
            node.left = dfs(p.left if p else None, q.left if q else None)
            node.right = dfs(p.right if p else None, q.right if q else None)

            return node

        return dfs(root1, root2)

        
