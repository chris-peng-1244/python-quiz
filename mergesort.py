def mergeSort(array):
  return mergeSortHelper(array, 0, len(array)-1)

def mergeSortHelper(array, left, right):
  if left == right:
    return [array[left]]

  mid = (left + right) // 2
  sortedLeft = mergeSortHelper(array, left, mid)
  sortedRight = mergeSortHelper(array, mid+1, right)

  sortedArray = []
  leftIndex = rightIndex = 0
  while leftIndex < len(sortedLeft) and rightIndex < len(sortedRight):
    if sortedLeft[leftIndex] <= sortedRight[rightIndex]:
      sortedArray.append(sortedLeft[leftIndex])
      leftIndex += 1
    else:
      sortedArray.append(sortedRight[rightIndex])
      rightIndex += 1
  
  if leftIndex != len(sortedLeft):
    for i in range(leftIndex, len(sortedLeft)):
      sortedArray.append(sortedLeft[i])

  if rightIndex != len(sortedRight):
    for i in range(rightIndex, len(sortedRight)):
      sortedArray.append(sortedRight[i])
  return sortedArray

def inplaceMergeSort(array):
  aux = list(array)
  inplaceMergeSortHelper(array, aux, 0, len(array) - 1)
  return array

def inplaceMergeSortHelper(array, aux_array, left, right):
  if left >= right:
    return
  mid = (left + right) // 2
  inplaceMergeSortHelper(aux_array, array, left, mid)
  inplaceMergeSortHelper(aux_array, array, mid+1, right)
  merge(array, aux_array, left, right)

def merge(array, aux_array, left, right):
  mid = (left + right) // 2
  i = left
  j = mid+1
  for k in range(left, right+1):
    if i <= mid and j <= right:
      if aux_array[i] <= aux_array[j]:
        array[k] = aux_array[i]
        i += 1
      else:
        array[k] = aux_array[j]
        j += 1
    elif i <= mid:
      array[k] = aux_array[i]
      i += 1
    elif j <= right:
      array[k] = aux_array[j]
      j += 1


print(mergeSort([8, 5, 2, 9, 5, 6, 3]))
print(inplaceMergeSort([8, 5, 2, 9, 5, 6, 3]))