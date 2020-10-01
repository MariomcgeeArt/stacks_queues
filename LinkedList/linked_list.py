class  Node(object):
    def __init__(self, data):
         """Initialize this node with the given data."""
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        """Initialize this linked list."""
        self.head = None
        self.tail = None

    def append(self, item):

        # Create a new node to hold the given item
        new_node = Node(item)

        # Check if this linked list is empty
        if self.head is None:
            self.head = new_node

        # Otherwise insert new node after tail
        
        else:
            self.tail.next = new_node

        # Update tail to new node regardless
            self.tail = new_node

    def prepend(self, item):
        new_node = Node(item)
        #if empty make head new node
        if self.head is None:
            self.head = new_node
        #otherwise set new node to head
        else:
            new_node.next = self.head
            self.head = new_node

        def delete_from_tail(self):
            current = self.head
            while current != None:
                if current.next = self.tail:
                    break
            current = current.next

            current.next = None
            self.tail = current

        def delete_from_head(self):
            self.head.next = new_head
            self.head = new_head

        def delete_from_head(self):
            self.head = self.head.next


        def print_list(self):
            """ Print everything in this linked list """
            current = self.head
            while current != None:
                print(current.data)
                current = current.next

    


    
      

        
