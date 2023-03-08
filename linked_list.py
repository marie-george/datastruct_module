class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_beginning(self, data):
        """принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        n = Node(data)
        if self.size == 0:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head = n
        self.size += 1

    def insert_at_end(self, data):
        """принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        n = Node(data)
        if self.size == 0:
            self.head = n
            self.tail = n
        else:
            temp = self.tail
            self.tail = n
            temp.next = self.tail
        self.size += 1

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next

        ll_string += 'None'
        print(ll_string)
        return ll_string


ll = LinkedList()
ll.insert_beginning({'id': 1})
ll.insert_at_end({'id': 2})
ll.insert_at_end({'id': 3})
ll.insert_beginning({'id': 0})
ll.print_ll()

