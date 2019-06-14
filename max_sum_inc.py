def max_sum_increseing_subsequence(array):
  max_sums = [ float("inf") for _ in array ]
  sequences = [ None for _ in array ]
  max_sums[0] = array[0]

  for i in range(1, len(array)):
    max_sum = array[i]
    for j in range(i):
      if array[j] < array[i]:
        if array[i] + max_sums[j] > max_sum:
          sequences[i] = j
          max_sum = array[i] + max_sums[j]
    max_sums[i] = max_sum
  result = max(max_sums)
  index = max_sums.index(result)
  result_seq = [array[index]]
  while True:
    if sequences[index] == None:
      break
    index = sequences[index]
    result_seq.append(array[index])
  
  return [result, list(reversed(result_seq))]


print(max_sum_increseing_subsequence([10, 70, 20, 30, 50, 11, 30]))
print(max_sum_increseing_subsequence([5,4,3,2,1]))
print(max_sum_increseing_subsequence([-5,-4,-3,-2,-1]))
