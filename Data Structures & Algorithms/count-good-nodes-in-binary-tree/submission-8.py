# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, maxPrev):
            nonlocal count

            if not node:
                return

            if maxPrev <= node.val:
                count += 1
            
            curr = max(maxPrev, node.val)
            dfs(node.left, curr)
            dfs(node.right, curr)

        dfs(root, float('-inf'))
        return count