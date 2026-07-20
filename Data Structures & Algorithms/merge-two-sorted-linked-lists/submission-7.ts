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
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode {
        let p1 = list1
        let p2 = list2
        const dummy = new ListNode(-1)
        let curr = dummy

        while (p1 && p2) {
            if (p1.val > p2.val) {
                curr.next = p2
                p2 = p2.next
            } else {
                curr.next = p1
                p1 = p1.next
            }
            curr = curr.next
        }

        curr.next = p1 || p2

        return dummy.next
    }
}
