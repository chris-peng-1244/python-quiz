from math import inf

def non_overlapping_intervals(intervals):
  current_end = -inf
  overlapping = 0

  for start, end in sorted(intervals, key = lambda i: i[1]):
    if start >= current_end:
      current_end = end
    else:
      overlapping += 1

  return overlapping

non_overlapping_intervals([(7, 9), (2, 4), (5, 8)])