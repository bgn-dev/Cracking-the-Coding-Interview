import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ch02_linked_lists.p01_remove_dups import remove_dups_hash_table
from ch02_linked_lists.linked_list import Node, insert


def linked_list_to_list(head: Node) -> list:
    """Helper function to convert linked list to Python list for easier testing"""
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    return result


class TestRemoveDups(unittest.TestCase):
    def test_single_node(self):
        head = Node(1)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [1])

    def test_no_duplicates(self):
        head = Node(1)
        insert(head, 2)
        insert(head, 3)
        insert(head, 4)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [1, 2, 3, 4])

    def test_all_duplicates(self):
        head = Node(5)
        insert(head, 5)
        insert(head, 5)
        insert(head, 5)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [5])

    def test_consecutive_duplicates(self):
        head = Node(1)
        insert(head, 1)
        insert(head, 2)
        insert(head, 2)
        insert(head, 3)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [1, 2, 3])

    def test_non_consecutive_duplicates(self):
        head = Node(1)
        insert(head, 2)
        insert(head, 1)
        insert(head, 3)
        insert(head, 2)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [1, 2, 3])

    def test_mixed_duplicates(self):
        head = Node(10)
        insert(head, 10)
        insert(head, 1)
        insert(head, 1)
        insert(head, 5)
        insert(head, 5)
        insert(head, 2)
        insert(head, 2)
        insert(head, 1)
        insert(head, 5)
        insert(head, 2)
        insert(head, 2)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [10, 1, 5, 2])

    def test_large_numbers(self):
        head = Node(100)
        insert(head, 200)
        insert(head, 100)
        insert(head, 300)
        insert(head, 200)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [100, 200, 300])

    def test_negative_numbers(self):
        head = Node(-1)
        insert(head, -2)
        insert(head, -1)
        insert(head, -3)
        insert(head, -2)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [-1, -2, -3])

    def test_mixed_positive_negative(self):
        head = Node(1)
        insert(head, -1)
        insert(head, 1)
        insert(head, -1)
        insert(head, 0)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [1, -1, 0])

    def test_with_zero(self):
        head = Node(0)
        insert(head, 1)
        insert(head, 0)
        insert(head, 2)
        insert(head, 1)
        remove_dups_hash_table(head)
        self.assertEqual(linked_list_to_list(head), [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
