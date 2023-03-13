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

    def to_list(self):
        """возвращает список с данными, содержащимися в односвязном списке"""
        list_of_contents = []
        current = self.head
        while current is not None:
            list_of_contents.append(current.data)
            current = current.next
        return list_of_contents

    def get_data_by_id(self, id):
        """возвращает первый найденный в LinkedList словарь с ключом id, значение которого равно переданному в метод значению"""
        list_of_contents = self.to_list()
        for item in list_of_contents:
            try:
                if type(item) == dict:
                    if item['id'] == id:
                        return item
                else:
                    raise Exception
            except Exception:
                print('Данные не являются словарем или в словаре нет id')


ll = LinkedList()
ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
ll.insert_at_end('idusername')
ll.insert_at_end([1, 2, 3])
ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

user_data = ll.get_data_by_id(2)
print(user_data)

