class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0

        def inorder(node):
            nonlocal counter
            if not node:
                return None

            left = inorder(node.left)
            if left is not None:
                return left

            counter += 1
            if counter == k:
                return node.val

            return inorder(node.right)

        return inorder(root)