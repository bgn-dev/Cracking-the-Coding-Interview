import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ch03_stacks_and_queues.p01_three_in_one import StackFixedSize

class TestStackFixedSize(unittest.TestCase):
    def test_stack_push(self):
        stack_amount = 1
        stack_size = 1
        stack = StackFixedSize(stack_size, stack_amount)
        stack.push(1, 1)
        self.assertEqual(stack.stack_array, [1])

    def test_stack_pop(self):
        stack_amount = 1
        stack_size = 1
        stack = StackFixedSize(stack_size, stack_amount)
        stack.push(1, 1)
        stack.pop(1)
        self.assertEqual(stack.stack_array, [None])

    def test_stack_peek(self):
        stack_amount = 1
        stack_size = 1
        stack = StackFixedSize(stack_size, stack_amount)
        stack.push(1, 1)
        stack.peek(1)
        self.assertEqual(stack.stack_array, [1])

    def test_stack_is_empty(self):
        stack_amount = 1
        stack_size = 1
        stack = StackFixedSize(stack_size, stack_amount)
        result = stack.isEmpty(1)
        self.assertEqual(result, True)

    def test_stack_each_full(self):
        stack_amount = 3
        stack_size = 3
        stack = StackFixedSize(stack_size, stack_amount)
        stack.push(1, 1)
        stack.push(1, 2)
        stack.push(1, 3)
        stack.push(2, 1)
        stack.push(2, 2)
        stack.push(2, 3)
        stack.push(3, 1)
        stack.push(3, 2)
        stack.push(3, 3)
        self.assertEqual(stack.stack_array, [1,2,3] * 3)

    def test_stack_full(self):
        stack_amount = 3
        stack_size = 3
        stack = StackFixedSize(stack_size, stack_amount)
        stack.push(1, 1)
        stack.push(1, 2)
        stack.push(1, 3)
        stack.push(1, 4)
        self.assertEqual(stack.stack_array, [1,2,3] + [None] * 6)

    def test_stack_pop_and_push(self):
        stack_amount = 3
        stack_size = 3
        stack = StackFixedSize(stack_size, stack_amount)
        stack.push(1, 1)
        stack.push(1, 2)
        stack.push(1, 3)
        stack.pop(1)
        stack.push(1, 4)
        self.assertEqual(stack.stack_array, [1,2,4] + [None] * 6)

    def test_stack_pop_is_empty(self):
        stack_amount = 3
        stack_size = 3
        stack = StackFixedSize(stack_size, stack_amount)
        stack.push(1, 1)
        stack.push(1, 2)
        stack.push(1, 3)
        stack.push(2, 1)
        stack.push(2, 2)
        stack.push(2, 3)
        stack.push(3, 1)
        stack.push(3, 2)
        stack.push(3, 3)
        stack.pop(1)
        stack.pop(1)
        stack.pop(1)
        stack.pop(2)
        stack.pop(2)
        stack.pop(2)
        stack.pop(3)
        stack.pop(3)
        stack.pop(3)
        self.assertEqual(stack.stack_array, [None] * 9)
