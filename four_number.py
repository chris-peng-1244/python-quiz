def four_number_sum(array, targetNum):
  big_sums = {}
  result = []

  for i in range(1, len(array)-1):
    for j in range(i+1, len(array)):
      P = array[i] + array[j]
      Q = targetNum - P
      if Q in big_sums:
          for item in big_sums[Q]:
            result.append([array[i], array[j]] + item)

    for k in range(i):
      P = array[k] + array[i]
      if P not in big_sums:
        big_sums[P] = [ [array[k], array[i]] ]
      else:
        big_sums[P].append([array[k], array[i]])

  return result

four_number_sum([1,2,3,4,5,6,7], 10)
