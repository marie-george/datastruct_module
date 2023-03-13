import unittest

from linked_list import Node, LinkedList


class TestNode(unittest.TestCase):

    def test_node_init(self):
        n1 = Node(5)
        self.assertEqual(n1.data, 5)


class TestLinkedList(unittest.TestCase):

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.print_ll(), " {'id': 0} -> {'id': 1} ->None")

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        self.assertEqual(ll.print_ll(), " {'id': 2} -> {'id': 3} ->None")

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        lst = ll.to_list()
        self.assertEqual(len(lst), 4)
        self.assertEqual(lst[0]['id'], 0)
        self.assertEqual(lst[3]['id'], 3)

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
        self.assertEqual(ll.get_data_by_id(2), {'id': 2, 'username': 'mosh_s'})
        self.assertEqual(ll.get_data_by_id(3), None)





