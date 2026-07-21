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
     * @param {ListNode} head
     * @return {void}
     */
    reorderList(head: ListNode | null): void {
        const dummy = new ListNode(-1, head)
        let slow: ListNode = dummy
        let fast: ListNode | null = dummy

        while (fast && fast.next) {
            slow = slow.next!
            fast = fast.next.next
        }

        let curr = slow.next
        let prev = null
        slow.next = null

        while (curr) {
            const tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        }

        let p1 = dummy.next
        let p2 = prev

        while (p1 && p2) {
            const tmp1 = p1.next
            const tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2
        }
    }
}
