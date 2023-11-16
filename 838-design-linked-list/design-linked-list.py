class Node:
    def __init__(self, val):
        self.val = val
        self.next_node = None

class MyLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        prev = self.head
        for i in range(index + 1):
            prev = prev.next_node

        return prev.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        prev = self.head
        for i in range(index):
            prev = prev.next_node

        new_node = Node(val)
        new_node.next_node = prev.next_node
        prev.next_node = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        prev = self.head
        for i in range(index):
            prev = prev.next_node

        prev.next_node = prev.next_node.next_node

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)