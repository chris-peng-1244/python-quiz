class MinHeap:
    def __init__(self, array):
        self.buildHeap(array)

    def buildHeap(self, array):
        self.heap = array
        parent = self.parent(len(array)-1)
        for i in reversed(range(parent + 1)):
            self.siftDown(i)
        
    def parent(self, index):
        if index < 1:
            return None
        return (index - 1) // 2

    def leftChild(self, index):
        left = index * 2 + 1
        return left if left < len(self.heap) else -1

    def rightChild(self, index):
        right = index * 2 + 2
        return right if right < len(self.heap) else -1

    def siftDown(self, index):
        while index < len(self.heap):
            left = self.leftChild(index)
            if left == -1:
                return
            right = self.rightChild(index)
            if right > -1 and self.heap[left] < self.heap[right]:
                indexSwap = left
            else:
                indexSwap = right
            if self.heap[indexSwap] < self.heap[index]:
                self.heap[index], self.heap[indexSwap] = self.heap[indexSwap], self.heap[index]
                index = indexSwap
            else:
                return

    def siftUp(self):
        index = len(self.heap) - 1
        parent = self.parent(index)
        while parent is not None:
            if self.heap[parent] > self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            else:
                return

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.siftDown(0)

    def insert(self, value):
        self.heap.append(value)
        self.siftUp()


minheap = MinHeap([48,12,24,7,8,-5,24,391,24,56,2,6,8,41])
print(minheap.heap)
