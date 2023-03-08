class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:

    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return
        value = self.head.data
        self.head = self.head.next_node
        return value





