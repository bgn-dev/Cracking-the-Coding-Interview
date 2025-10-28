import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ch02_linked_lists.p02_kth_to_last import kth_to_last_two_pass, kth_to_last_two_pointer
from ch02_linked_lists.linked_list import Node, insert

def linked_list_to_list(head: Node) -> list:
    """Helper function to convert linked list to Python list for easier testing"""
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    return result

class TestKthToLastTwoPass(unittest.TestCase):
    def test_single_node(self):
        kth_index = 1
        head = Node(8)
        result = kth_to_last_two_pass(head,kth_index)
        self.assertEqual(result, 8)

    def test_kth_index_less_than_1(self):
        kth_index = 0
        head = Node(8)
        result = kth_to_last_two_pass(head,kth_index)
        self.assertEqual(result, None)
    
    def test_kth_index_greater_than_linked_list_length(self):
        kth_index = 6
        head = Node(8)
        insert(head,10)
        insert(head,3)
        insert(head,4)
        insert(head,5)
        result = kth_to_last_two_pass(head,kth_index)
        self.assertEqual(result, None)

    def test_normal_linked_list(self):
        kth_index = 4
        head = Node(8)
        insert(head,10)
        insert(head,3)
        insert(head,4)
        insert(head,5)
        result = kth_to_last_two_pass(head,kth_index)
        self.assertEqual(result, 10)
    
    def test_kth_index_equals_list_length(self):
        kth_index = 5
        head = Node(8)
        insert(head, 10)
        insert(head, 3)
        insert(head, 4)
        insert(head, 5)
        result = kth_to_last_two_pass(head, kth_index)
        self.assertEqual(result, 8)

    def test_kth_index_1(self):
        kth_index = 1
        head = Node(8)
        insert(head, 10)
        insert(head, 3)
        insert(head, 4)
        insert(head, 5)
        result = kth_to_last_two_pass(head, kth_index)
        self.assertEqual(result, 5)

class TestKthToLastTwoPointer(unittest.TestCase):
    def test_single_node(self):
        kth_index = 1
        head = Node(8)
        result = kth_to_last_two_pointer(head,kth_index)
        self.assertEqual(result, 8)

    def test_normal_linked_list(self):
        kth_index = 4
        head = Node(8)
        insert(head,10)
        insert(head,3)
        insert(head,4)
        insert(head,5)
        result = kth_to_last_two_pointer(head,kth_index)
        self.assertEqual(result, 10)
    
    def test_kth_index_equals_list_length(self):
        kth_index = 5
        head = Node(8)
        insert(head, 10)
        insert(head, 3)
        insert(head, 4)
        insert(head, 5)
        result = kth_to_last_two_pointer(head, kth_index)
        self.assertEqual(result, 8)

    def test_kth_index_1(self):
        kth_index = 1
        head = Node(8)
        insert(head, 10)
        insert(head, 3)
        insert(head, 4)
        insert(head, 5)
        result = kth_to_last_two_pointer(head, kth_index)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()