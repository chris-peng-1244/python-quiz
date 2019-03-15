def largest_divisible_subset(nums):
  if not nums:
    return []

  nums.sort()

  # Keep track of the number of divisors of each element, and where to find
  # its last divisor.
  num_divisors = [1 for _ in range(len(nums))]
  prev_divisor_index = [-1 for _ in range(len(nums))]

  # Also track the index of the last element in the best subset solution so far.
  max_index = 0

  # For each element, check if a previous element divides it. If so, and if adding
  # the element will result in a larger subset, update its number of divisors
  # and where to find its last divisor.
  for i in range(len(nums)):
    for j in range(i):
      if (nums[i] % nums[j] == 0) and (num_divisors[i] < num_divisors[j] + 1):
        num_divisors[i] = num_divisors[j] + 1
        prev_divisor_index[i] = j
      
    if num_divisors[max_index] < num_divisors[i]:
      max_index = i

  # Finally, go back through the chain of divisors and get all the subset elements
  result = []
  i = max_index
  while i >= 0:
    result.append(nums[i])
    i = prev_divisor_index[i]
  
  return result

largest_divisible_subset([3, 5, 10, 20, 21])