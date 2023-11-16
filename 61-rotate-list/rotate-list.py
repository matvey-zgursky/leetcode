# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        fast = slow = head
        
        count = 0
        for i in range(k):
            count += 1
            if not fast.next:
                fast = slow
                break
            
            fast = fast.next 
        
        for i in range(k%count):
            fast = fast.next
        
        if fast == slow:
            return fast
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        temp = slow.next
        slow.next = None
        fast.next = head
        
        return temp