try:
    from ch02_linked_lists.linked_list import Node, insert, traverse_linked_list
except ImportError:
    from linked_list import Node, insert, traverse_linked_list

def hash_function(data: int, table_size) -> int:
    return data % table_size

def hash_table(table_size) -> list:
    return [[] for _ in range(table_size)]

def remove_dups_hash_table(head: Node) -> Node:
    table_size = 100
    tables = hash_table(table_size)
    n = head

    # Add the head to the hash table
    key = hash_function(n.data,table_size)
    tables[key].append(n.data)

    while n.next != None:
        dup = False
        key = hash_function(n.next.data,table_size)
        # Loop trough all elements with the same key in the hash table
        for elem in tables[key]:
            # If duplicate remove the node
            # Dup is negated, so the next of n is not updated, since we removed the next which was a duplicate
            if elem == n.next.data:
                n.next = n.next.next
                dup = not dup
                break
        # If next not duplicate move on
        if not dup:
            tables[key].append(n.next.data)
            n = n.next
    return head

def remove_dups_two_pointer(head: Node) -> Node:
    n = head

    while n != None:
        runner = n
        while runner.next != None:
            # Remove duplicate within the linked list
            if n.data == runner.next.data:
                runner.next = runner.next.next
            # If not a duplicate, move on with the runner
            else:
                runner = runner.next
        n = n.next
    return head
    

if __name__ == '__main__':
    head = Node(10)
    insert(head,10)
    insert(head,1)
    insert(head,1)
    insert(head,5)
    insert(head,5)
    insert(head,2)
    insert(head,2)
    insert(head,1)
    insert(head,5)
    insert(head,2)
    insert(head,2)


    print("Linked list: ", end='')
    traverse_linked_list(head)
    print("Removed duplciates: ", end='')
    remove_dups_two_pointer(head)
    traverse_linked_list(head)