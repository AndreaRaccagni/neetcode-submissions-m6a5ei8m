# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root

        i = root

        while True:
            if max(p.val, q.val) < i.val:
                i = i.left
            elif min(p.val, q.val) > i.val:
                i = i.right
            else:
                return i
