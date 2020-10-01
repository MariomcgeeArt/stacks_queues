class Stack:
    def __init__(self):
        #CREATE AN EMPTY stack
        #put the front at index 0
         #back at index n - 1
        self.my_stack = []

    def enstack(self, item):
        self.my_stack.append(item)

    def destack(self, item):
        self.my_stack.pop(0)

    def peek(self, item):
        return self.my_stack[0]