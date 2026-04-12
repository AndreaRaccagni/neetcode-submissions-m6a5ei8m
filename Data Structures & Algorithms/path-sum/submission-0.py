# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        q = deque()

        if root:
            q.append((root, 0))

        while q:
            node, total = q.popleft()
            currTotal = total + node.val

            if not node.left and not node.right:
                if currTotal == targetSum:
                    return True
                continue
            
            if node.left:
                q.append((node.left, currTotal))

            if node.right:
                q.append((node.right, currTotal))

        return False
        