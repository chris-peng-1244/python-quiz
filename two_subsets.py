from math import inf
from itertools import combinations

def two_subsets(nums):
  smallest_diff = inf

  result = None
  for subset1, subset2 in subset_pairs(nums):
    diff = abs(sum(subset1) - sum(subset2))
    if diff < smallest_diff:
      smallest_diff = diff
      result = (subset1, subset2)
    return result

def subset_pairs(nums):
  n = len(nums)
  for r in range(n + 1):
    for indices in combinations(range(n), r):
      subset1 = [nums[i] for i in indices]
      subset2 = [nums[i] for i in set(range(n)) - set(indices)]
      yield subset1, subset2