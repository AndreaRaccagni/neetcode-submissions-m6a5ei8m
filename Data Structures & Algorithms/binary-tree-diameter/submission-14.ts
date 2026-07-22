/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    diameterOfBinaryTree(root: TreeNode | null): number {
        let maxDiam = 0

        function maxDepth(node: TreeNode | null) {
            if (!node) return 0

            const left = maxDepth(node.left)
            const right = maxDepth(node.right)

            maxDiam = Math.max(maxDiam, left + right)

            return 1 + Math.max(left, right)
        }

        maxDepth(root)
        return maxDiam
    }
}
