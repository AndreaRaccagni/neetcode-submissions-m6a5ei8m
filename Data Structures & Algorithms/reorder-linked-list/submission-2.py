# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # find the mid of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half
        curr = slow.next
        prev = None
        slow.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # merge the lists
        curr1 = head
        curr2 = prev

        while curr1 and curr2:
            tmp = curr1.next
            curr1.next = curr2
            curr1 = curr1.next
            curr2 = tmp



