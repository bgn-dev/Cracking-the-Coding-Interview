class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # Insert a new node at the end of the linked list
    def insert(self, data):
        while self.next != None:
            self = self.next
        self.next = Node(data)

    # Delete first node found with the same data
    def delete(self, data):
        n = self
        if n.data == data:
            return(self.next)
        
        while n.next != None:
            if n.next.data == data:
                n.next = n.next.next
                return self
            n = n.next

    # Find specific node within the linked list
    def find_node(self, data):
        n = self
        while n != None:
            if n.data == data:
                return n
            n = n.next
        return None

    # Print the linked list in it's row
    def traverse_linked_list(self):
        while self != None:
            if self.next == None:
                print(self.data)
            else:
                print(self.data, end='->')
            self = self.next
        

if __name__ == '__main__':
    head = Node(1)
    head.insert(5)
    head.insert(2)
    head.insert(13)
    head.insert(7)
    head.insert(3)    
    head.delete(5)
    head.traverse_linked_list()
