# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        p = dummy

        for _ in range(n):
            p = p.next

        prev = dummy
        while p.next:
            p = p.next
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next