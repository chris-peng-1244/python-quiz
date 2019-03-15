def counting_sort(array, digit, base = 10):
  counts = [[] for _ in range(base)]

  for num in array:
    d = (num // base ** digit) % base
    counts[d].append(num)

  result = []
  for bucket in counts:
    result.extend(bucket)

  return result

def radix_sort(array, digits = 10):
  for digit in range(digits):
    array = counting_sort(array, digit)

  return array


radix_sort([4, 100, 54, 537, 2, 89])