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
    copyRandomList(head: Node | null): Node | null {
        const oldToNew = new Map<Node, Node>()
        const dummy = new Node(-1)
        let p: Node | null = head
        let q: Node = dummy

        while (p) {
            const node = new Node(p.val)
            q.next = node
            oldToNew.set(p, node)
            p = p.next
            q = q.next
        }

        for (const [o, n] of oldToNew) {
            n.random = o.random ? oldToNew.get(o.random)! : null
        }
        
        return dummy.next
    }
}
