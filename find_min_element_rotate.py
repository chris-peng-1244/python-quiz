def helper(arr, low, high):
  if high == low:
    return arr[low]

  mid = (high + low) / 2
  if arr[mid] < arr[high]:
    high = mid
  else:
    low = mid + 1
  return helper(arr, low, high)

def find_min_element(arr):
  low, high = 0, len(arr) - 1
  return helper(arr, low, high)