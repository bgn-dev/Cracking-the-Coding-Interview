try:
    from ch02_linked_lists.linked_list import Node
except ImportError:
    from linked_list import Node

def kth_to_last_two_pass(head: Node, kth_index) -> int:
    n_runner = head
    n = head
    linked_list_length = 0

    # Count elements in linked list
    while n_runner != None:
        linked_list_length += 1
        n_runner = n_runner.next

    # If requested kth index is less than 1 or greater than the length of the list return None
    if kth_index > linked_list_length or kth_index < 1:
        return None

    # Find the kth to the last element
    for i in range(linked_list_length-kth_index):
        n = n.next

    return n.data

def kth_to_last_two_pointer(head: Node, kth_index) -> int:
    """
    This method does not account for kth_index's which are less than 1 or greater than the size of the linked list 
    """
    n = head
    runner = head

    while runner.next != None:
        # Once the runner reached the kth element, move the second pointer, which points at the head at first if execution
        if kth_index <= 1:
            n = n.next
        runner = runner.next
        kth_index -= 1
    
    return n.data
        

if __name__ == '__main__':
    head = Node(8)
    head.insert(10)
    head.insert(3)
    head.insert(4)
    head.insert(5)

    kth_index = 6
    result = kth_to_last_two_pointer(head,kth_index)
    print(result)    