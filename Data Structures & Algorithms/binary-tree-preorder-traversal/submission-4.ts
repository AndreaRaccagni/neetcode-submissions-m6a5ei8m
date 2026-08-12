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
    preorderTraversal(root: TreeNode | null): number[] {
        const res = []
        this.preorder(root, res)
        return res
    }

    preorder(node: TreeNode | null, res: number[]): void {
        if (!node) return

        res.push(node.val)
        this.preorder(node.left, res)
        this.preorder(node.right, res)
    } 
}
