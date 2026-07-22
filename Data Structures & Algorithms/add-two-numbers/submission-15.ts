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
    addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode {
        let p1: ListNode | null = l1
        let p2: ListNode | null = l2
        const dummy = new ListNode(-1)
        let curr = dummy
        let carry = 0

        while (p1 || p2 || carry) {
            const v1 = p1 ? p1.val : 0
            const v2 = p2 ? p2.val : 0
            const total = v1 + v2 + carry
            const node = new ListNode(total % 10)
            carry = Math.floor(total / 10)
            curr.next = node
            curr = curr.next

            p1 = p1 ? p1.next : p1
            p2 = p2 ? p2.next : p2
        }

        return dummy.next
    }
}
