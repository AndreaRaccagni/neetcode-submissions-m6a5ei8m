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
     * @return {number[]}
     */
    inorderTraversal(root: TreeNode | null): number[] {
        const res = []
        this.inorder(root, res)
        return res
    }

    inorder(node: TreeNode | null, res: number[]): void {
        if (!node) return

        this.inorder(node.left, res)
        res.push(node.val)
        this.inorder(node.right, res)
    }   
}
