try:
    from ch02_linked_lists.linked_list import Node
except ImportError:
    from linked_list import Node

def delete_middle_node(node: Node):
    """
    Delete node by shifting all subsequent data left. Time: O(n), Space: O(1)
    Note: Assumes node is not first or last in the list
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
    Delete node by copying next node's data and removing next node. Time: O(1), Space: O(1)
    Note: Assumes node is not first or last in the list
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