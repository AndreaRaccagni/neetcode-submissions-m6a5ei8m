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
    reorderList(head) {
        let slow = head
        let fast = head.next

        while (fast && fast.next) {
            slow = slow.next
            fast = fast.next.next
        }

        let curr = slow.next
        slow.next = null
        slow = null

        while (curr) {
            let tmp = curr.next
            curr.next = slow
            slow = curr
            curr = tmp
        }

        let tmp1 = head
        curr = slow

        while (curr) {
            let tmp2 = tmp1.next
            tmp1.next = curr
            tmp1 = curr
            curr = tmp2
        }




        
    
    }
}
