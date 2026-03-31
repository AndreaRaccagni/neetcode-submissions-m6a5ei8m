/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1, l2) {
        const dummy = new ListNode()
        let curr = dummy
        let carry = 0

        while (l1 || l2 || carry) {
            const a1 = l1 ? l1.val : 0
            const a2 = l2 ? l2.val : 0
            
            const total = a1 + a2 + carry
            const newVal = total % 10 
            carry = Math.floor(total / 10)

            curr.next = new ListNode(newVal)
            curr = curr.next

            l1 = l1 ? l1.next : null
            l2 = l2 ? l2.next : null
        }

        return dummy.next
    }
}
