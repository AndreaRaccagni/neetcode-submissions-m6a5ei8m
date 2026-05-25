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
     * @return {number[][]}
     */
    levelOrder(root) {
        const q = []
        const result = []

        if (root) {
            q.push(root)
        }

        while (q.length) {
            const n = q.length
            const currLevel = []
            for (let i = 0; i < n; i++) {
                const node = q.shift()
                currLevel.push(node.val)

                if (node.left) {
                    q.push(node.left)
                }
                if (node.right) {
                    q.push(node.right)
                }
            }
            result.push(currLevel)
        }
        return result
    }
}
