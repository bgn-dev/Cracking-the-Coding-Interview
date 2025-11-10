try:
    from ch02_linked_lists.linked_list import Node
except ImportError:
    from linked_list import Node

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
    head.insert(2)
    head.insert(3)
    head.insert(4)
    head.insert(5)
    head.insert(6)
    node = head.find_node(5)
    delete_middle_node_two_step(node)
    head.traverse_linked_list()