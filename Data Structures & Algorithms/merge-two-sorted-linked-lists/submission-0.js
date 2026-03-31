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
    mergeTwoLists(list1, list2) {
        let dummy = new ListNode()
        let node = dummy

        while (list1 && list2){
            if(list1.val > list2.val){
                dummy.next = list2
                list2 = list2.next
            } else{
                dummy.next = list1
                list1 = list1.next
            }

            dummy = dummy.next
        }

        dummy.next = list1 || list2

        return node.next

    }
}
