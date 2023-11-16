# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast_pointer = head
        slow_pointer = head
        
        for i in range(n):
            fast_pointer = fast_pointer.next
            
        if not fast_pointer:
            return head.next
        
        while fast_pointer.next:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
            
        slow_pointer.next = slow_pointer.next.next
        return head
                