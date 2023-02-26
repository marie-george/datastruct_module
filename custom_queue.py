class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Queue:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

# queue = Queue()
# queue.enqueue('data1')
# queue.enqueue('data2')
# queue.enqueue('data3')
#
# print(queue.head.data)
# print(queue.head.next_node.data)
# print(queue.tail.data)
# print(queue.tail.next_node)
# print(queue.tail.next_node.data)

