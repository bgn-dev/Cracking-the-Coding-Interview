class Node:
    """Node in a singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def insert(self, data):
        """Insert a new node at the end of the linked list"""
        n = self
        while n.next != None:
            n = n.next
        n.next = Node(data)

    def delete(self, data):
        """Delete first node with matching data. Returns new head."""
        if self.data == data:
            return self.next

        n = self
        while n.next != None:
            if n.next.data == data:
                n.next = n.next.next
                return self
            n = n.next
        return self

    def find_node(self, data):
        """Find and return first node with matching data, or None if not found"""
        n = self
        while n != None:
            if n.data == data:
                return n
            n = n.next
        return None

    def traverse_linked_list(self):
        """Print the linked list in format: data1->data2->data3"""
        n = self
        while n != None:
            if n.next == None:
                print(n.data)
            else:
                print(n.data, end='->')
            n = n.next
        

if __name__ == '__main__':
    head = Node(1)
    head.insert(5)
    head.insert(2)
    head.insert(13)
    head.insert(7)
    head.insert(3)    
    head.delete(5)
    head.traverse_linked_list()
