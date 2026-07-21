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
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head: ListNode | null, n: number): ListNode {
        const dummy = new ListNode(-1, head)
        let curr: ListNode | null = head

        for (let i = 0; i < n; i++) {
            curr = curr.next
        }

        let prev = dummy
        while (curr) {
            curr = curr.next
            prev = prev.next
        }

        prev.next = prev.next.next

        return dummy.next
    }
}
