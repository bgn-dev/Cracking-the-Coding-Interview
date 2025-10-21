class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert(head: Node, data):
    while head.next != None:
        head = head.next
    head.next = Node(data)

def delete(head: Node, data) -> Node:
    n = head
    if n.data == data:
        return(head.next)
    
    while n.next != None:
        if n.next.data == data:
            n.next = n.next.next
            return head
        n = n.next


def traverse_linked_list(head: Node):
    while head != None:
        print(head.data)
        head = head.next
        

if __name__ == '__main__':
    head = Node(5)
    insert(head, 6)
    insert(head, 9)
    insert(head, 1)
    insert(head, 23)
    
    traverse_linked_list(delete(head, 6))
