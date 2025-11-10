import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ch02_linked_lists.p01_remove_dups import remove_dups_hash_table, remove_dups_two_pointer
from ch02_linked_lists.linked_list import Node


def linked_list_to_list(head: Node) -> list:
    """Helper function to convert linked list to Python list for easier testing"""
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    return result


class TestRemoveDupsHashTable(unittest.TestCase):
    def test_single_node(self):
        head = Node(1)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [1])

    def test_no_duplicates(self):
        head = Node(1)
        head.insert(2)
        head.insert(3)
        head.insert(4)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [1, 2, 3, 4])

    def test_all_duplicates(self):
        head = Node(5)
        head.insert(5)
        head.insert(5)
        head.insert(5)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [5])

    def test_consecutive_duplicates(self):
        head = Node(1)
        head.insert(1)
        head.insert(2)
        head.insert(2)
        head.insert(3)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [1, 2, 3])

    def test_non_consecutive_duplicates(self):
        head = Node(1)
        head.insert(2)
        head.insert(1)
        head.insert(3)
        head.insert(2)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [1, 2, 3])

    def test_mixed_duplicates(self):
        head = Node(10)
        head.insert(10)
        head.insert(1)
        head.insert(1)
        head.insert(5)
        head.insert(5)
        head.insert(2)
        head.insert(2)
        head.insert(1)
        head.insert(5)
        head.insert(2)
        head.insert(2)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [10, 1, 5, 2])

    def test_large_numbers(self):
        head = Node(100)
        head.insert(200)
        head.insert(100)
        head.insert(300)
        head.insert(200)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [100, 200, 300])

    def test_negative_numbers(self):
        head = Node(-1)
        head.insert(-2)
        head.insert(-1)
        head.insert(-3)
        head.insert(-2)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [-1, -2, -3])

    def test_mixed_positive_negative(self):
        head = Node(1)
        head.insert(-1)
        head.insert(1)
        head.insert(-1)
        head.insert(0)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [1, -1, 0])

    def test_with_zero(self):
        head = Node(0)
        head.insert(1)
        head.insert(0)
        head.insert(2)
        head.insert(1)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [0, 1, 2])


class TestRemoveDupsTwoPointer(unittest.TestCase):
    def test_single_node(self):
        head = Node(1)
        remove_dups_two_pointer(head)
        self.assertEqual(linked_list_to_list(head), [1])

    def test_no_duplicates(self):
        head = Node(1)
        head.insert(2)
        head.insert(3)
        head.insert(4)
        remove_dups_two_pointer(head)
        self.assertEqual(linked_list_to_list(head), [1, 2, 3, 4])

    def test_all_duplicates(self):
        head = Node(5)
        head.insert(5)
        head.insert(5)
        head.insert(5)
        remove_dups_two_pointer(head)
        self.assertEqual(linked_list_to_list(head), [5])

    def test_consecutive_duplicates(self):
        head = Node(1)
        head.insert(1)
        head.insert(2)
        head.insert(2)
        head.insert(3)
        remove_dups_two_pointer(head)
        self.assertEqual(linked_list_to_list(head), [1, 2, 3])

    def test_non_consecutive_duplicates(self):
        head = Node(1)
        head.insert(2)
        head.insert(1)
        head.insert(3)
        head.insert(2)
        remove_dups_two_pointer(head)
        self.assertEqual(linked_list_to_list(head), [1, 2, 3])

    def test_mixed_duplicates(self):
        head = Node(10)
        head.insert(10)
        head.insert(1)
        head.insert(1)
        head.insert(5)
        head.insert(5)
        head.insert(2)
        head.insert(2)
        head.insert(1)
        head.insert(5)
        head.insert(2)
        head.insert(2)
        remove_dups_two_pointer(head)
        self.assertEqual(linked_list_to_list(head), [10, 1, 5, 2])

    def test_large_numbers(self):
        head = Node(100)
        head.insert(200)
        head.insert(100)
        head.insert(300)
        head.insert(200)
        remove_dups_two_pointer(head)
        self.assertEqual(linked_list_to_list(head), [100, 200, 300])

    def test_negative_numbers(self):
        head = Node(-1)
        head.insert(-2)
        head.insert(-1)
        head.insert(-3)
        head.insert(-2)
        remove_dups_two_pointer(head)
        self.assertEqual(linked_list_to_list(head), [-1, -2, -3])

    def test_mixed_positive_negative(self):
        head = Node(1)
        head.insert(-1)
        head.insert(1)
        head.insert(-1)
        head.insert(0)
        remove_dups_two_pointer(head)
        self.assertEqual(linked_list_to_list(head), [1, -1, 0])

    def test_with_zero(self):
        head = Node(0)
        head.insert(1)
        head.insert(0)
        head.insert(2)
        head.insert(1)
        remove_dups_two_pointer(head)
        self.assertEqual(linked_list_to_list(head), [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
