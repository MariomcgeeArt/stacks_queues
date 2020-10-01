from Stack import Stack

#CREATE
my_stack = Stack()

my_stack.enstack("A")
#["A"]
my_stack.enstack("B")
#["A", "B"]
my_stack.enstack("C")
#["A", "B", "C"]

print(my_stack.front())