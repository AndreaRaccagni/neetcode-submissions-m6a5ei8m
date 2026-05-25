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
    rightSideView(root) {
        const q = []
        const res = []
        let level = 0

        if (root) {
            q.push(root)
        }

        while (q.length) {
            const n = q.length
            for (let i = 0; i < n; i++) {
                const node = q.shift()
                if (level === res.length) {
                    res.push(node.val)
                }
                if (node.right) {
                    q.push(node.right)
                }
                if (node.left) {
                    q.push(node.left)
                }
            }
            level++
        }
        return res
    }
}
