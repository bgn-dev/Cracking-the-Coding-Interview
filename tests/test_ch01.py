import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ch01_arrays_and_strings.p01_is_unique import is_unique_brute_force, is_unique_hash_table


class TestIsUnique(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_unique_brute_force(""))
        self.assertTrue(is_unique_hash_table(""))
        
    def test_single_character(self):
        self.assertTrue(is_unique_brute_force("a"))
        self.assertTrue(is_unique_hash_table("a"))
                
    def test_unique_characters(self):
        self.assertTrue(is_unique_brute_force("abcdef"))
        self.assertTrue(is_unique_hash_table("abcdef"))
        
    def test_duplicate_characters(self):
        self.assertFalse(is_unique_brute_force("hello"))
        self.assertFalse(is_unique_hash_table("hello"))
        

if __name__ == "__main__":
    unittest.main()