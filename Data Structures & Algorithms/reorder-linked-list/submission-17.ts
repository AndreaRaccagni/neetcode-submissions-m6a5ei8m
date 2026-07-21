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
        if (!head || !head.next) return

        let slow: ListNode = head
        let fast: ListNode | null = head

        while (fast.next && fast.next.next) {
            slow = slow.next!
            fast = fast.next.next
        }

        let curr = slow.next
        slow.next = null
        let prev: ListNode | null = null

        while (curr) {
            const next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        }

        let p1: ListNode | null = head
        let p2: ListNode | null = prev

        while (p2) {
            const next1 = p1!.next
            const next2 = p2.next
            p1!.next = p2
            p2.next = next1
            p1 = next1
            p2 = next2
        }
    }
}
