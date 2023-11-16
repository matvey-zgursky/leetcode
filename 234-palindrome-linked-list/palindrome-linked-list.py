# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Найти среднюю точку списка
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Перевернуть вторую часть списка
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Проверить равны ли две половины списка
        pointer_one = head
        pointer_two = prev
        while pointer_two:
            if pointer_one.val != pointer_two.val:
                return False
            
            pointer_one = pointer_one.next
            pointer_two = pointer_two.next

        return True