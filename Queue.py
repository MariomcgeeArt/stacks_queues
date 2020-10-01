class Queue:
    def __init__(self):
        self.my_queue = []



    def enque(self, item):
        self.my_queue.append(item)
    #note the implementtion of this function is not using pop function because of the way
    #we are setting up the que with the front being on one end vs the back
    def dequeue(self, item):
        self.my_queue.pop(0)
    
    def front(self):
        return self.my_queue[0]
