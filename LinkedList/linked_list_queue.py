from linked_list import LinkedList

class LinkedListQueue:
    def __init__(self):
        self.li_queue = LinkedList()

    def enqueue(self, item):
        self.li_queue.append(item)
    
    def dequeue(self):
        self.li_queue.delete_from_head()
    
    def front(self):
        return self.ll_queue.head.data
        