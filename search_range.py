def searchForRange(array, target):
  left = 0
  right = len(array) - 1

  while left <= right:
    mid = (left + right) // 2
    if array[mid] > target:
      right = mid - 1
    elif array[mid] < target:
      left = mid + 1
    else:
      return [ findLeftRange(array, target, mid), findRightRange(array, target, mid) ]
  return [-1, -1]

def findLeftRange(array, target, mid):
  if mid == 0 or array[mid-1] != target:
    return mid
  left = 0
  right = mid - 1
  while left < right:
    mid = (left + right) // 2
    if array[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return left if array[left] == target else left + 1

def findRightRange(array, target, mid):
  if mid == len(array) - 1 or array[mid + 1] != target:
    return mid
  left = mid + 1
  right = len(array) - 1
  while left < right:
    mid = (left + right) // 2
    if array[mid] > target:
      right = mid -1
    else:
      left = mid + 1
  return left if array[left] == target else left - 1

print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))
print(searchForRange([5, 7, 7, 8, 8, 10], 5))
print(searchForRange([5, 7, 7, 8, 8, 10], 7))
print(searchForRange([5, 7, 7, 8, 8, 10], 8))
print(searchForRange([5, 7, 7, 8, 8, 10], 10))
print(searchForRange([5, 7, 7, 8, 8, 10], 9))
print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 47))
print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], -1))
print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 45, 45, 45], 45))