import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ch01_arrays_and_strings.p01_is_unique import is_unique_brute_force, is_unique_hash_table, is_unique_bit_vector, is_unique_sort_and_compare


class TestIsUnique(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_unique_brute_force(""))
        self.assertTrue(is_unique_hash_table(""))
        self.assertTrue(is_unique_bit_vector(""))
        self.assertTrue(is_unique_sort_and_compare(""))
        
    def test_single_character(self):
        self.assertTrue(is_unique_brute_force("a"))
        self.assertTrue(is_unique_hash_table("a"))
        self.assertTrue(is_unique_bit_vector("a"))
        self.assertTrue(is_unique_sort_and_compare("a"))
                
    def test_unique_characters(self):
        self.assertTrue(is_unique_brute_force("abcdef"))
        self.assertTrue(is_unique_hash_table("abcdef"))
        self.assertTrue(is_unique_bit_vector("abcdef"))
        self.assertTrue(is_unique_sort_and_compare("abcdef"))
        
    def test_duplicate_characters(self):
        self.assertFalse(is_unique_brute_force("hello"))
        self.assertFalse(is_unique_hash_table("hello"))
        self.assertFalse(is_unique_bit_vector("hello"))
        self.assertFalse(is_unique_sort_and_compare("hello"))

    def test_numbers_and_symbols(self):
        self.assertTrue(is_unique_brute_force("123!@#"))
        self.assertFalse(is_unique_brute_force("123!1"))
        self.assertTrue(is_unique_hash_table("123!@#"))
        self.assertFalse(is_unique_hash_table("123!1"))
        self.assertTrue(is_unique_bit_vector("123!@#"))
        self.assertFalse(is_unique_bit_vector("123!1"))
        self.assertTrue(is_unique_sort_and_compare("123!@#"))
        self.assertFalse(is_unique_sort_and_compare("123!1"))

    def test_mixed_alphanumeric(self):
        self.assertTrue(is_unique_brute_force("abc123"))
        self.assertFalse(is_unique_brute_force("abc1a"))
        self.assertTrue(is_unique_hash_table("abc123"))
        self.assertFalse(is_unique_hash_table("abc1a"))
        self.assertTrue(is_unique_bit_vector("abc123"))
        self.assertFalse(is_unique_bit_vector("abc1a"))
        self.assertTrue(is_unique_sort_and_compare("abc123"))
        self.assertFalse(is_unique_sort_and_compare("abc1a"))

    def test_case_sensitivity(self):
        # Assuming case-sensitive implementation
        self.assertTrue(is_unique_brute_force("Aa"))
        self.assertTrue(is_unique_hash_table("Aa"))
        self.assertTrue(is_unique_bit_vector("Aa"))
        self.assertTrue(is_unique_sort_and_compare("Aa"))

    def test_whitespace(self):
        self.assertFalse(is_unique_brute_force("a b c"))
        self.assertFalse(is_unique_brute_force("a  b"))  # two spaces
        self.assertFalse(is_unique_brute_force("a\tb\ta"))  # tabs
        self.assertFalse(is_unique_hash_table("a b c"))
        self.assertFalse(is_unique_hash_table("a  b"))  # two spaces
        self.assertFalse(is_unique_hash_table("a\tb\ta"))  # tabs
        self.assertFalse(is_unique_bit_vector("a b c"))
        self.assertFalse(is_unique_bit_vector("a  b"))  # two spaces
        self.assertFalse(is_unique_bit_vector("a\tb\ta"))  # tabs
        self.assertFalse(is_unique_sort_and_compare("a b c"))
        self.assertFalse(is_unique_sort_and_compare("a  b"))  # two spaces
        self.assertFalse(is_unique_sort_and_compare("a\tb\ta"))  # tabs

    def test_extended_ascii(self):
        # Test characters beyond basic ASCII if your bit vector supports them
        self.assertTrue(is_unique_brute_force("café"))  # accented characters
    
    def test_maximum_unique_string(self):
        # For ASCII: 95 printable characters
        import string
        all_printable = string.printable.replace('\n\r\t\v\f', '')  # remove duplicates
        self.assertTrue(is_unique_bit_vector(all_printable))
        

if __name__ == "__main__":
    unittest.main()