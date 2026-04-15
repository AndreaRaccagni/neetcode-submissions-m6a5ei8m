# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        dummy = ListNode(-1, head)
        slow = dummy
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        p1 = head
        p2 = prev

        while p2:
            tmp = p1.next
            p1.next = p2
            p1 = p2
            p2 = tmp

        return