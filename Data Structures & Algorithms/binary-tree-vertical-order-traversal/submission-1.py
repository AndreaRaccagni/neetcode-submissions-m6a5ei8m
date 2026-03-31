# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        q = deque()
        hashMap = {}

        if root:
            q.append((root, 0))

        while q:
            for i in range(len(q)):
                node, i = q.popleft()
                column = hashMap.get(i, [])
                column.append(node.val)
                hashMap[i] = column
                if node.left:
                    q.append((node.left, i - 1))
                if node.right:
                    q.append((node.right, i + 1))

        minCol = float('inf')
        maxCol = float('-inf')

        for k in hashMap.keys():
            minCol = min(minCol, k)
            maxCol = max(maxCol, k)

        res = []

        for i in range(minCol, maxCol + 1):
            res.append(hashMap[i])

        return res