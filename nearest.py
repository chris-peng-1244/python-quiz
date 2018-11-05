def _nearest(arr, i):
    for j in range(1, len(arr)):
        low = i - j
        high = i + j
        if 0 <= low and arr[low] > arr[i]:
            return low
        if high < len(arr) and arr[high] > arr[i]:
            return high

def preprocess(arr):
    cache = [None for _ in range(len(arr))]

    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            cache[j + 1] = j
        elif arr[j + 1] > arr[j]:
            cache[j] = j + 1

    for i, val in enumerate(cache):
        if val is None:
            cache[i] = _nearest(arr, i)

    return cache