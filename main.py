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


n1 = Node(5, None)
n2 = Node('a', n1)
print(n1.data)
print(n2.data)
print(n1)
print(n2.next_node)

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.head.data)
print(stack.head.next_node.data)
print(stack.head.next_node.next_node.data)
print(stack.head.next_node.next_node.next_node.data)