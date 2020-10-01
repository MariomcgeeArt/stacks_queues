from Queue import Queue


my_queue = Queue()

my_queue.enqueue("A")
#["A"]
my_queue.enqueue("B")
#["A", "B"]
my_queue.enqueue("C")
#["A", "B", "C"]

my_queue.dequeue("A")

print(my_queue.front())