"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next            
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
                
            curr = curr.next.next

        new_head = head.next
        curr_old = head
        curr_new = new_head
        while curr_old:
            curr_old.next = curr_old.next.next
            if curr_new.next:
                curr_new.next = curr_new.next.next
            else:
                curr_new.next = None
                
            curr_old = curr_old.next
            curr_new = curr_new.next
        
        return new_head