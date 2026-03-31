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
    maxDepth(root) {
        const queue = new Queue();
        if (root !== null) {
            queue.push(root);
        }
        let depth = 0;

        while (queue.size()) {
            const size = queue.size();

            for (let i = 0; i < size; i++) {
                const item = queue.pop();
                if (item.left) {
                    queue.push(item.left);
                }
                if (item.right) {
                    queue.push(item.right);
                }
            }

            depth++;
        }
        return depth
    }
}
