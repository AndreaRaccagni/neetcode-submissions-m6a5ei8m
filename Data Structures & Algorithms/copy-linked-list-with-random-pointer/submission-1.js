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

        const mapper = new Map();
        const dummy = new Node(-1);
        let newCurr = dummy;
        let curr = head;

        while (curr) {
            const node = new Node(curr.val)
            newCurr.next = node
            mapper.set(curr, node)
            newCurr = newCurr.next
            curr = curr.next
        }

        mapper.forEach((newNode, oldNode) => {
            newNode.random = mapper.get(oldNode.random) || null;
        });

        return dummy.next
    }
}
