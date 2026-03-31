# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        #find the half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse the second half
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        #merge the two lists
        cur1 = head
        cur2 = prev
        while cur2:
            tmp = cur1.next
            cur1.next = cur2
            cur1 = cur2
            cur2 = tmp
        