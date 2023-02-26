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


# stack = Stack()
# stack.push('data1')
# data = stack.pop()
#
# # стэк стал пустой
# print(stack.head)
#
# # # pop() удаляет элемент и возвращает данные удаленного элемента
# print(data)
#
# stack = Stack()
# stack.push('data1')
# stack.push('data2')
# data = stack.pop()
#
# # теперь последний элемента содержит данные data1
# print(stack.head.data)
#
#
# # данные удаленного элемента
# print(data)
# 'data2'





