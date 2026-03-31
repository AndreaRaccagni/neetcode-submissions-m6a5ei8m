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
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2





