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
        const mapper = new Map();
        let dummy = new Node(-1);
        let old_curr = head;
        let new_curr = dummy;

        while (old_curr) {
            const node = new Node(old_curr.val);
            new_curr.next = node;
            mapper.set(old_curr, node);
            old_curr = old_curr.next;
            new_curr = new_curr.next;
        }

        mapper.forEach((new_node, old_node) => {
            new_node.random = mapper.get(old_node.random) || null
        })

        return dummy.next
    }
}
