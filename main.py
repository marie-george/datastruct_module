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


