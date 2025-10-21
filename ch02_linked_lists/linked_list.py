class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Insert a new node at the end of the linked list
def insert(head: Node, data):
    while head.next != None:
        head = head.next
    head.next = Node(data)

# Delete first node found with the same data
def delete(head: Node, data) -> Node:
    n = head
    if n.data == data:
        return(head.next)
    
    while n.next != None:
        if n.next.data == data:
            n.next = n.next.next
            return head
        n = n.next

# Print the linked list in it's row
def traverse_linked_list(head: Node):
    while head != None:
        print(head.data)
        head = head.next
        

if __name__ == '__main__':
    head = Node(1)
    insert(head,5)
    insert(head,2)
    insert(head,13)
    insert(head,7)
    insert(head,3)    
    traverse_linked_list(delete(head,5))
