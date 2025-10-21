import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ch01_arrays_and_strings.p03_urlify import urlify_brute_force


class TestURLify(unittest.TestCase):
    def test_empty_strings(self):
        result = urlify_brute_force("",len(""))
        self.assertEqual(result,"")

    def test_single_space(self):
        result = urlify_brute_force(" ",len(" "))
        self.assertEqual(result,"%20")
    
    def test_double_space(self):
        result = urlify_brute_force("  ",len("  "))
        self.assertEqual(result,"%20%20")
    
    def test_space_at_start(self):
        result = urlify_brute_force(" MrJohnSmith",len(" MrJohnSmith"))
        self.assertEqual(result,"%20MrJohnSmith")

    def test_space_at_start(self):
        result = urlify_brute_force("MrJohnSmith ",len("MrJohnSmith "))
        self.assertEqual(result,"MrJohnSmith%20")

    def test_random(self):
        result = urlify_brute_force(" Mr John  Smith  ", len(" Mr John  Smith  "))   
        self.assertEqual(result,"%20Mr%20John%20%20Smith%20%20") 

if __name__ == "__main__":
    unittest.main()