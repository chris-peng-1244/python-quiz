def numbersInPi(pi, numbers):
  cache = {}
  minSpace = getMinSpace(pi, numbers, cache, 0)
  return -1 if minSpace == float("inf") else minSpace

def getMinSpace(string, numbers, cache, index):
  if index == len(string):
    return -1
  if index in cache:
    return cache[index]

  minSpace = float("inf")
  for i in range(index, len(string)):
    prefix = string[index:i+1]
    if prefix in numbers:
      minSpace = min(minSpace, 1+getMinSpace(string, numbers, cache, i+1))
  cache[index] = minSpace
  return cache[index]


print(numbersInPi("314159", ["3141", "5", "31", "2", "4159", "9", "42"]))