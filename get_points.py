from itertools import combinations

def get_points_naive(intervals):
  points = set([element for pair in intervals for element in pair])

  subsets = []
  for size in range(1, len(points)):
    subsets.extend(list(combinations(points, size)))

  for start, end in intervals:
    for subset in subsets:
      # Is there any point that is between the start and end of all intervals?
      if all(any(start <= point <= end for point in subset)
      for start, end in intervals):
        return subset


def get_points(intervals):
  intervals.sort(key=lambda x: (x[1], x[0]))

  points = []
  latest_endpoint = None

  for start, end in intervals:
    if start <= latest_endpoint:
      continue
    else:
      points.append(end)
      latest_endpoint = end
  
  return points


get_points([(1, 4), (4, 5), (7, 9), (9, 12)])