// class Node {
//   constructor(val, next = null, random = null) {
//       this.val = val;
//       this.next = next;
//       this.random = random;
//   }
// }

class Solution {
    /**
     * @param {Node} head
     * @return {Node}
     */
    copyRandomList(head) {
        if (!head) return null

        const nodes = new Map()
        nodes.set(null, null)
        let curr = head

        while (curr) {
            const newNode = new Node(curr.val)
            nodes.set(curr, newNode)
            curr = curr.next
        }
        curr = head

        while (curr) {
            const newNode = nodes.get(curr)
            newNode.next = nodes.get(curr.next)
            newNode.random = nodes.get(curr.random)
            curr = curr.next
        }

        return nodes.get(head)
    }
}
