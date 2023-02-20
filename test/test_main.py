import unittest

from main import Node, Stack


class TestNode(unittest.TestCase):

    def test_node_init(self):
        n1 = Node(5, None)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)


class TestStack(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        self.assertEqual(stack.push('data1'), None)
        self.assertEqual(stack.head.data, 'data1')

