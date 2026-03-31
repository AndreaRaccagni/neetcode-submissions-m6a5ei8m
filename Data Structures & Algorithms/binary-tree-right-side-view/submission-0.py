# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []

        if root:
            q.append(root)
        
        while q:
            addedToRes = False
            for _ in range(len(q)):
                node = q.popleft()

                if not addedToRes:
                    res.append(node.val)
                    addedToRes = True

                if node.right:
                    q.append(node.right)

                if node.left:
                    q.append(node.left)

        return res