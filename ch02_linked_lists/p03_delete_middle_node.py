try:
    from ch02_linked_lists.linked_list import Node, insert, traverse_linked_list, find_node
except ImportError:
    from linked_list import Node, insert, traverse_linked_list, find_node

def delete_middle_node(node: Node):
    """
    Walk trough the remaining list starting from node and replace its successor data with the current node data
    Disclaimer: The algorithm does expect the input node not to be first or last within the linked list
    """
    while node.next != None:
        node.data = node.next.data
        # When we moved the linked list by 1 to the left, we stop at node.next
        if node.next.next == None:
            node.next = None
            break
        node = node.next

def delete_middle_node_two_step(node: Node):
    """
    First step: Copy the content of successor node to current node
    Second step: Set the pointer of current node to the successor of node.next
    """
    if node.next != None:
        node.data = node.next.data
        node.next = node.next.next

if __name__ == '__main__':
    head = Node(1)
    insert(head, 2)
    insert(head, 3)
    insert(head, 4)
    insert(head, 5)
    insert(head, 6)
    node = find_node(head, 5)
    delete_middle_node_two_step(node)
    traverse_linked_list(head)