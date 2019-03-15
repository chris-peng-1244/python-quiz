def max_path_weight(arrays, level = 0, index = 0):
  if level == len(arrays) - 1:
    return arrays[level][index]
  else:
    return arrays[level][index] + max(
      max_path_weight(arrays, level + 1, index), 
      max_path_weight(arrays, level + 1, index + 1)
    )

def max_path_weight_dp(arrays):
  for level in range(len(arrays) -2 , -1, -1):
    for index in range(level + 1):
      arrays[level][index] += max(arrays[level + 1][index], arrays[level + 1][index + 1])
  return arrays[0][0]