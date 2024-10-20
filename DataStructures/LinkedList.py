class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def display(self):
        if not self.head:
            return None
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __delete__(self, data):
        if not self.head:
            return None
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current =current.next