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

if __name__ == '__main__':
    head = Node(1)
    insert(head, 6)
    node = find_node(head, 1)
    delete_middle_node(node)
    traverse_linked_list(head)