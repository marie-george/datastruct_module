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



