# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fake_node = ListNode()
        curr = fake_node
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0

            total = l1_val + l2_val + carry
            curr.next = ListNode(total % 10)
            carry = total // 10
            
            if l1:
                l1 = l1.next
            else:
                l1 = None

            if l2:
                l2 = l2.next
            else:
                l2 = None

            curr = curr.next
            
        return fake_node.next