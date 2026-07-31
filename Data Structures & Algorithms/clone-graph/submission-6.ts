/**
 * // Definition for a Node.
 * class Node {
 *     constructor(val = 0, neighbors = []) {
 *       this.val = val;
 *       this.neighbors = neighbors;
 *     }
 * }
 */

class Solution {
    /**
     * @param {Node} node
     * @return {Node}
     */
    cloneGraph(node: Node | null): Node {
        const oldToNew = new Map<Node, Node>()

        function dfs(node: Node) {
            if (!node) return null

            if(oldToNew.has(node)) {
                return oldToNew.get(node)
            }

            const newNode = new Node(node.val)
            oldToNew.set(node, newNode)

            for (const n of node.neighbors) {
                newNode.neighbors.push(dfs(n))
            }
            return newNode
        }
        return dfs(node)
    }
}
