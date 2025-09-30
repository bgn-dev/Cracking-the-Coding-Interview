import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ch01_arrays_and_strings.p02_check_permutation import check_permutation_sort


class TestCheckPermutation(unittest.TestCase):
    def test_empty_strings(self):
        self.assertTrue(check_permutation_sort("", ""))

    def test_empty_and_non_empty(self):
        self.assertFalse(check_permutation_sort("", "a"))
        self.assertFalse(check_permutation_sort("a", ""))

    def test_single_character_match(self):
        self.assertTrue(check_permutation_sort("a", "a"))

    def test_single_character_no_match(self):
        self.assertFalse(check_permutation_sort("a", "b"))

    def test_basic_permutations(self):
        self.assertTrue(check_permutation_sort("abc", "bca"))
        self.assertTrue(check_permutation_sort("abc", "cab"))
        self.assertTrue(check_permutation_sort("abc", "cba"))

    def test_not_permutations(self):
        self.assertFalse(check_permutation_sort("abc", "def"))
        self.assertFalse(check_permutation_sort("abc", "aac"))
        self.assertFalse(check_permutation_sort("abc", "abd"))

    def test_different_lengths(self):
        self.assertFalse(check_permutation_sort("abc", "abcd"))
        self.assertFalse(check_permutation_sort("abcd", "abc"))
        self.assertFalse(check_permutation_sort("a", "ab"))

    def test_duplicate_characters(self):
        self.assertTrue(check_permutation_sort("aabbcc", "abcabc"))
        self.assertTrue(check_permutation_sort("aabbcc", "cabcab"))
        self.assertFalse(check_permutation_sort("aabbcc", "abcccc"))
        self.assertFalse(check_permutation_sort("aaa", "aab"))

    def test_case_sensitivity(self):
        self.assertFalse(check_permutation_sort("Abc", "abc"))
        self.assertTrue(check_permutation_sort("Abc", "cbA"))
        self.assertTrue(check_permutation_sort("ABC", "CAB"))

    def test_whitespace(self):
        self.assertTrue(check_permutation_sort("a b c", "c b a"))
        self.assertFalse(check_permutation_sort("abc", "a bc"))
        self.assertTrue(check_permutation_sort("  ", "  "))
        self.assertFalse(check_permutation_sort(" ", "  "))

    def test_special_characters(self):
        self.assertTrue(check_permutation_sort("a@b#c", "c#b@a"))
        self.assertTrue(check_permutation_sort("!@#$%", "%$#@!"))
        self.assertFalse(check_permutation_sort("!@#", "!@$"))

    def test_numbers_as_strings(self):
        self.assertTrue(check_permutation_sort("123", "321"))
        self.assertFalse(check_permutation_sort("123", "124"))
        self.assertTrue(check_permutation_sort("1122", "2211"))

    def test_mixed_alphanumeric(self):
        self.assertTrue(check_permutation_sort("abc123", "321cba"))
        self.assertFalse(check_permutation_sort("abc123", "abc124"))

    def test_long_strings(self):
        self.assertTrue(check_permutation_sort("abcdefghijklmnop", "ponmlkjihgfedcba"))

    def test_repeated_characters(self):
        self.assertTrue(check_permutation_sort("aaa", "aaa"))
        self.assertFalse(check_permutation_sort("aaa", "aaaa"))
        self.assertTrue(check_permutation_sort("aaabbbccc", "abcabcabc"))

    def test_unicode_characters(self):
        self.assertTrue(check_permutation_sort("café", "éfac"))
        self.assertTrue(check_permutation_sort("🎉🎊🎈", "🎈🎊🎉"))


if __name__ == "__main__":
    unittest.main()