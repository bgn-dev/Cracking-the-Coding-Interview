import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ch02_linked_lists.p03_delete_middle_node import delete_middle_node, delete_middle_node_two_step
from ch02_linked_lists.linked_list import Node


def linked_list_to_list(head: Node) -> list:
    """Helper function to convert linked list to Python list for easier testing"""
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    return result


class TestDeleteMiddleNode(unittest.TestCase):
    def test_delete_middle_of_three(self):
        head = Node(1)
        head.insert(2)
        head.insert(3)
        node = head.find_node(2)
        delete_middle_node(node)
        self.assertEqual(linked_list_to_list(head), [1, 3])

    def test_delete_middle_of_five(self):
        head = Node(1)
        head.insert(2)
        head.insert(3)
        head.insert(4)
        head.insert(5)
        node = head.find_node(3)
        delete_middle_node(node)
        self.assertEqual(linked_list_to_list(head), [1, 2, 4, 5])

    def test_delete_second_of_five(self):
        head = Node(1)
        head.insert(2)
        head.insert(3)
        head.insert(4)
        head.insert(5)
        node = head.find_node(2)
        delete_middle_node(node)
        self.assertEqual(linked_list_to_list(head), [1, 3, 4, 5])

    def test_delete_fourth_of_five(self):
        head = Node(1)
        head.insert(2)
        head.insert(3)
        head.insert(4)
        head.insert(5)
        node = head.find_node(4)
        delete_middle_node(node)
        self.assertEqual(linked_list_to_list(head), [1, 2, 3, 5])

    def test_delete_middle_with_duplicates(self):
        head = Node(1)
        head.insert(2)
        head.insert(3)
        head.insert(2)
        head.insert(4)
        node = head.find_node(3)
        delete_middle_node(node)
        self.assertEqual(linked_list_to_list(head), [1, 2, 2, 4])

    def test_delete_from_long_list(self):
        head = Node(1)
        for i in range(2, 11):
            head.insert(i)
        node = head.find_node(5)
        delete_middle_node(node)
        self.assertEqual(linked_list_to_list(head), [1, 2, 3, 4, 6, 7, 8, 9, 10])

    def test_delete_middle_with_negative_numbers(self):
        head = Node(-1)
        head.insert(-2)
        head.insert(-3)
        head.insert(-4)
        node = head.find_node(-2)
        delete_middle_node(node)
        self.assertEqual(linked_list_to_list(head), [-1, -3, -4])

    def test_delete_middle_with_zero(self):
        head = Node(0)
        head.insert(1)
        head.insert(2)
        node = head.find_node(1)
        delete_middle_node(node)
        self.assertEqual(linked_list_to_list(head), [0, 2])

    def test_delete_middle_with_large_numbers(self):
        head = Node(100)
        head.insert(200)
        head.insert(300)
        head.insert(400)
        node = head.find_node(200)
        delete_middle_node(node)
        self.assertEqual(linked_list_to_list(head), [100, 300, 400])

    def test_delete_second_of_four(self):
        head = Node(1)
        head.insert(2)
        head.insert(3)
        head.insert(4)
        node = head.find_node(2)
        delete_middle_node(node)
        self.assertEqual(linked_list_to_list(head), [1, 3, 4])


class TestDeleteMiddleNodeTwoStep(unittest.TestCase):
    def test_delete_middle_of_three(self):
        head = Node(1)
        head.insert(2)
        head.insert(3)
        node = head.find_node(2)
        delete_middle_node_two_step(node)
        self.assertEqual(linked_list_to_list(head), [1, 3])

    def test_delete_middle_of_five(self):
        head = Node(1)
        head.insert(2)
        head.insert(3)
        head.insert(4)
        head.insert(5)
        node = head.find_node(3)
        delete_middle_node_two_step(node)
        self.assertEqual(linked_list_to_list(head), [1, 2, 4, 5])

    def test_delete_second_of_five(self):
        head = Node(1)
        head.insert(2)
        head.insert(3)
        head.insert(4)
        head.insert(5)
        node = head.find_node(2)
        delete_middle_node_two_step(node)
        self.assertEqual(linked_list_to_list(head), [1, 3, 4, 5])

    def test_delete_fourth_of_five(self):
        head = Node(1)
        head.insert(2)
        head.insert(3)
        head.insert(4)
        head.insert(5)
        node = head.find_node(4)
        delete_middle_node_two_step(node)
        self.assertEqual(linked_list_to_list(head), [1, 2, 3, 5])

    def test_delete_middle_with_duplicates(self):
        head = Node(1)
        head.insert(2)
        head.insert(3)
        head.insert(2)
        head.insert(4)
        node = head.find_node(3)
        delete_middle_node_two_step(node)
        self.assertEqual(linked_list_to_list(head), [1, 2, 2, 4])

    def test_delete_from_long_list(self):
        head = Node(1)
        for i in range(2, 11):
            head.insert(i)
        node = head.find_node(5)
        delete_middle_node_two_step(node)
        self.assertEqual(linked_list_to_list(head), [1, 2, 3, 4, 6, 7, 8, 9, 10])

    def test_delete_middle_with_negative_numbers(self):
        head = Node(-1)
        head.insert(-2)
        head.insert(-3)
        head.insert(-4)
        node = head.find_node(-2)
        delete_middle_node_two_step(node)
        self.assertEqual(linked_list_to_list(head), [-1, -3, -4])

    def test_delete_middle_with_zero(self):
        head = Node(0)
        head.insert(1)
        head.insert(2)
        node = head.find_node(1)
        delete_middle_node_two_step(node)
        self.assertEqual(linked_list_to_list(head), [0, 2])

    def test_delete_middle_with_large_numbers(self):
        head = Node(100)
        head.insert(200)
        head.insert(300)
        head.insert(400)
        node = head.find_node(200)
        delete_middle_node_two_step(node)
        self.assertEqual(linked_list_to_list(head), [100, 300, 400])

    def test_delete_second_of_four(self):
        head = Node(1)
        head.insert(2)
        head.insert(3)
        head.insert(4)
        node = head.find_node(2)
        delete_middle_node_two_step(node)
        self.assertEqual(linked_list_to_list(head), [1, 3, 4])


if __name__ == "__main__":
    unittest.main()
