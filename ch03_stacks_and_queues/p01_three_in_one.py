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
            return False

    def pop(self, stack_id):
        """
        Pop the top item from the specified stack.
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
        Returns True if empty, False otherwise.
        """
        if self.stack_current_size[stack_id - 1] == self.stack_size:
            return True
        else:
            return False



if __name__ == '__main__':
    # Stack ID has to be consecutive starting from 1 to stack_amount
    stack_id = 1
    stack_amount = 1
    stack_size = 1
    stack = StackFixedSize(stack_size, stack_amount)
    stack.push(1, 1)
    print(stack.pop(1))