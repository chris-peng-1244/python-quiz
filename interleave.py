from queue import Queue
import math

def interleave(stack):
    size = len(stack)
    queue = Queue()

    while stack:
        queue.put(stack.pop())

    for _ in range(int(size / 2)):
        queue.put(queue.get())

    for _ in range(int(math.ceil(size / 2.0))):
        stack.append(queue.get())

    for _ in range(int(size / 2)):
        queue.put(stack.pop())
        queue.put(queue.get())
    if stack:
        queue.put(stack.pop())

    while not queue.empty():
        stack.append(queue.get())
    return stack

interleave([1,2,3,4,5])