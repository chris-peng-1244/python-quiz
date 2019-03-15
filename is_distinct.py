def is_distinct(arr):
  d = {}
  for e in arr:
    if e in d:
      return False
    d[e] = True
  return True

def distinct_subarray_naive(arr):
  max_distinct_subarray = []
  for i in range(len(arr)):
    for j in range(i + 1, len(arr) + 1):
      subarray = arr[i:j]
      if is_distinct(subarray) and len(subarray) > len(max_distinct_subarray):
        max_distinct_subarray = subarray
  return len(max_distinct_subarray)

def distinct_subarray(arr):
  d = {} # most recent occurences of each element

  result = 0
  longest_distinct_subarray_start_index = 0
  for i, e in enumerate(arr):
    if e in d:
      # If d[e] appears in the middle of the current longest distinct subarray
      if d[e] >= longest_distinct_subarray_start_index:
        result = max(result, i - longest_distinct_subarray_start_index)
        longest_distinct_subarray_start_index = d[e] + 1
    d[e] = i

  return max(result, len(arr) - longest_distinct_subarray_start_index)

distinct_subarray([5, 1, 3, 5, 2, 3, 4, 1])