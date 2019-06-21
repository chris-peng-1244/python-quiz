class ContinuousMedianHandler:
  def __init__(self):
    self.median = None
    self.lower_half = MinHeap()
    self.higher_half = MinHeap()

  def insert(self, number):
    if self.lower_half.size() == 0:
      self.lower_half.push(-1 * number)
      self.median = number
    else:
      max_of_lower = -1 * self.lower_half.peek()
      if number > max_of_lower:
        self.higher_half.push(number)
      else:
        self.lower_half.push(-1 * number)
        
      self.rebalanceHeap()
      self.updateMedian()

  def rebalanceHeap(self):
    if self.lower_half.size() - self.higher_half.size() == 2:
      lower_max = -1 * self.lower_half.pop()
      self.higher_half.push(lower_max)
    elif self.higher_half.size() - self.lower_half.size() == 2:
      higher_min = self.higher_half.pop()
      self.lower_half.push(-1 * higher_min)

  def updateMedian(self):
    lower_max = -1 * self.lower_half.peek()
    higher_min = self.higher_half.peek()
    if self.lower_half.size() == self.higher_half.size():
      self.median = (lower_max + higher_min) / 2
    elif self.lower_half.size() > self.higher_half.size():
      self.median = lower_max
    else:
      self.median = higher_min

  def getMedian(self):
    return self.median
     
class MinHeap:
  def __init__(self):
    self.list = []

  def push(self, value):
    self.list.append(value)
    self._siftUp(len(self.list) - 1)

  def pop(self):
    min_value = self.list[0]
    self.list[0] = self.list[-1]
    self.list.pop()
    self._siftDown(0)
    return min_value

  def peek(self):
    return self.list[0]

  def size(self):
    return len(self.list)

  def _siftUp(self, index):
    if index == 0:
      return
    parent = (index-1) // 2
    if self.list[parent] > self.list[index]:
      self.list[parent], self.list[index] = self.list[index], self.list[parent]
      self._siftUp(parent)

  def _siftDown(self, index):
    left = (index + 1) * 2 -1
    right = (index + 1) * 2
    size = len(self.list)
    if left >= size:
      return 
    indexToSwap = left
    if right < size and self.list[right] < self.list[left]:
      indexToSwap = right

    if self.list[indexToSwap] < self.list[index]:
      self.list[indexToSwap], self.list[index] = self.list[index], self.list[indexToSwap]
      self._siftDown(indexToSwap)
    # elif size > right and self.list[right] < self.list[index]:
    #   self.list[right], self.list[index] = self.list[index], self.list[right]
    #   self._siftDown(right)


handler = ContinuousMedianHandler()
handler.insert(5)
print(handler.getMedian())
handler.insert(10)
print(handler.getMedian())
handler.insert(100)
print(handler.getMedian())
handler.insert(200)
print(handler.getMedian())
handler.insert(6)
print(handler.getMedian())
handler.insert(13)
print(handler.getMedian())
handler.insert(14)
print(handler.getMedian())
handler.insert(50)
handler.insert(51)
handler.insert(52)
handler.insert(1000)
handler.insert(10_000)
handler.insert(10_001)
handler.insert(10_002)
handler.insert(10_003)
handler.insert(10_004)