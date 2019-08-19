def numberOfBinaryTreeTopologies(n):
  num = [1, 1, 2]
  for i in range(3, n + 1):
    total = 0
    for l in range(i):
      r = i - 1 - l
      total += num[l] * num[r]
    num.append(total)
  return num[-1]

print(numberOfBinaryTreeTopologies(3))
print(numberOfBinaryTreeTopologies(4))