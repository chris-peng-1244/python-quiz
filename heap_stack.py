from time import time
import heapq

class Stack:
    def __init__(self):
        self.max_heap = MaxHeap()

    def push(self, item):
        t = time()
        self.max_heap.push(item, t)

    def pop(self):
        item, _ = self.max_heap.pop()
        return item

class MaxHeap:
    def __init__(self):
        self._heap = []
    
    def push(self, item, priority):
        heapq.heappush(self._heap, (-priority, item))

    def pop(self):
        _, item = heapq.heappop(self._heap) 
        return item

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())