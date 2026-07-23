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
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {TreeNode}
     */
    lowestCommonAncestor(
        root: TreeNode | null,
        p: TreeNode | null,
        q: TreeNode | null,
    ) {
        let a = root

        while (true) {
            if (Math.min(p.val, q.val) > a.val) {
                a = a.right
            } else if (Math.max(p.val, q.val) < a.val) {
                a = a.left
            } else {
                return a
            }
        }
    }
}
