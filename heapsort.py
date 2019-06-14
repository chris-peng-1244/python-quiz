def heap_sort(array):
  # start heap from 1 make calculation easier
  array = [0] + array
  build_max_heap(array)
  lastIndex = len(array) - 1
  while lastIndex > 1:
    array[1], array[lastIndex] = array[lastIndex], array[1]
    lastIndex -= 1
    max_heapify(array, 1, lastIndex)
  return array[1:]

def left_child(i):
  return i * 2

def right_child(i):
  return i * 2 + 1

def max_heapify(array, i, heap_size):
  left = left_child(i)
  right = right_child(i)
  if left <= heap_size and array[left] > array[i]:
    largest = left
  else:
    largest = i
  if right <= heap_size and array[right] > array[largest]:
    largest = right
  if largest != i:
    array[largest], array[i] = array[i], array[largest]
    max_heapify(array, largest, heap_size)

def build_max_heap(array):
  startIndex = len(array) // 2
  while startIndex > 0:
    max_heapify(array, startIndex, len(array) - 1)
    startIndex -= 1

heap_sort([5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1])