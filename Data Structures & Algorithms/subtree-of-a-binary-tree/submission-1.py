# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s_root = self.serialize(root)
        s_subRoot = self.serialize(subRoot)

        if (s_subRoot in s_root):
            return True
        
        return False

    def serialize(self, root):
        if not root:
            return "$#"
        
        return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))