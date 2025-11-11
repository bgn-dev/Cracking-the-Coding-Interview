class StackFixedSize:
    """
    Implements multiple stacks with fixed size in a single array.
    Each stack grows from left to right within its allocated space.
    """
    def __init__(self, stack_size, stack_amount):
        self.stack_size = stack_size  # Maximum size of each stack
        self.stack_amount = stack_amount  # Number of stacks
        self.stack_array = [None] * stack_amount * stack_size  # Single array for all stacks
        self.stack_current_size = [stack_size] * stack_amount  # Tracks available space for each stack

    def push(self, stack_id, item):
        """
        Push an item onto the specified stack.
        Time: O(1), Space: O(1)
        Returns True if successful, False if stack is full.
        """
        current_size = self.stack_current_size[stack_id - 1]
        if current_size > 0:
            # Calculate position: start of stack + items already pushed
            new_head = stack_id * self.stack_size - current_size
            self.stack_array[new_head] = item
            self.stack_current_size[stack_id - 1] -= 1  # Decrease available space
            return True
        else:
            self.resize()
            return self.push(stack_id, item)

    def pop(self, stack_id):
        """
        Pop the top item from the specified stack.
        Time: O(1), Space: O(1)
        Returns the item, or None if stack is empty.
        """
        current_size = self.stack_current_size[stack_id - 1]
        if not self.isEmpty(stack_id):
            # Calculate position of current top element
            current_head = stack_id * self.stack_size - current_size - 1
            item = self.stack_array[current_head]
            self.stack_array[current_head] = None
            self.stack_current_size[stack_id - 1] += 1  # Increase available space
            return item
        else:
            return None

    def peek(self, stack_id):
        """
        Return the top item of the specified stack without removing it.
        Time: O(1), Space: O(1)
        Returns None if stack is empty.
        """
        if not self.isEmpty(stack_id):
            current_size = self.stack_current_size[stack_id - 1]
            current_head = stack_id * self.stack_size - current_size - 1
            return self.stack_array[current_head]
        else:
            return None

    def isEmpty(self, stack_id):
        """
        Check if the specified stack is empty.
        Time: O(1), Space: O(1)
        Returns True if empty, False otherwise.
        """
        if self.stack_current_size[stack_id - 1] == self.stack_size:
            return True
        else:
            return False

    def resize(self):
        """
        Resize all stacks by doublin capacity.
        Time: O(n), Space: O(n)
        """
        start_stack_one = 0
        start_stack_two = 1 * self.stack_size
        start_stack_three = 2 * self.stack_size
        self.stack_size *= 2
        start_stack_one_new = 0
        start_stack_two_new = 1 * self.stack_size
        start_stack_three_new = 2 * self.stack_size
        stack_array_length = len(self.stack_array)

        for i in range(self.stack_amount):
            self.stack_current_size[i] +=  self.stack_size // 2

        temp = [None] * self.stack_size * self.stack_amount
        temp[start_stack_one_new:start_stack_one_new + self.stack_size // 2] = self.stack_array[start_stack_one:start_stack_two]
        temp[start_stack_two_new:start_stack_two_new + self.stack_size // 2] = self.stack_array[start_stack_two:start_stack_three]
        temp[start_stack_three_new:start_stack_three_new + self.stack_size // 2] = self.stack_array[start_stack_three:stack_array_length]

        self.stack_array = temp
        
        


if __name__ == '__main__':
    # Stack ID has to be consecutive starting from 1 to stack_amount
    stack_id = 1
    stack_amount = 3
    stack_size = 3
    stack = StackFixedSize(stack_size, stack_amount)
    stack.push(1, 1)
    stack.push(1, 1)
    stack.push(1, 1)
    stack.push(2, 2)
    stack.push(2, 2)
    stack.push(2, 2)
    stack.push(3, 3)
    stack.push(3, 3)
    stack.push(3, 3)
    print(stack.stack_array)
    stack.push(1, 1)
    stack.push(1, 1)
    stack.push(1, 1)
    print(stack.stack_array)