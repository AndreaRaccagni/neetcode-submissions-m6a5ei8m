# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        for _ in range(n):
            curr = curr.next

        dummy = ListNode(-1, head)
        prev = dummy

        while curr:
            prev = prev.next
            curr = curr.next

        prev.next = prev.next.next

        return dummy.next
        

