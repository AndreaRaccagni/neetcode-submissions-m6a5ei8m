# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        for _ in range(n):
            curr = curr.next

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        while curr:
            curr = curr.next
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next
        