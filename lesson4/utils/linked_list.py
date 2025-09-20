class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    head: Node | None
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node # type: ignore

    def search(self, value):
        idx = 0
        current = self.head
        while current:
            if current.value == value:
                return idx
            idx += 1
            current = current.next
        return -1
    
    def insert(self, value, idx: int):
        if idx < 0:
            return
        if idx == 0:
            new_node = Node(value)
            new_node.next = self.head # type: ignore
            self.head = new_node
            return

        current = self.head
        next_idx = 1

        while next_idx < idx:
            current = current.next # type: ignore
            next_idx += 1

        if not current:
            return

        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node # type: ignore

    def length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def delete(self, value):
        if not self.head:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next