def min_number_of_jumps(array):
  min_jumps = [0 for _ in array]

  for i in range(1, len(array)):
    min_jump = float("inf")
    for j in range(i):
      if j + array[j] >= i:
        min_jump = min(min_jump, min_jumps[j] + 1)
    min_jumps[i] = min_jump
  
  return min_jumps[1]

min_number_of_jumps([3,4,2,1,2,3,7,1,1,1,3,2,6,2,1,1,1])