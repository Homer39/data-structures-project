"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestNode(unittest.TestCase):

    def test_node_init(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n2.next_node, n1)

    def test_stack_push(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')
        self.assertEqual(stack.top.next_node.next_node.next_node, None)
        with self.assertRaises(AttributeError):
            stack.top.next_node.next_node.next_node.data

    def test_pop_1(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual(stack.pop(), 'data1')
        self.assertEqual(stack.top, None)


    def test_pop_2(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.pop(), 'data2')
        self.assertEqual(stack.top.data, 'data1')


if __name__ == '__main__':
    unittest.main()
