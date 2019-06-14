def palindromePartitioningMinCuts(string):
  isPalindromeMatrix = buildIsPalindromeMatrix2(string)
  cuts = [ 0 for _ in range(len(string)) ]
  for i in range(len(string)):
    if isPalindromeMatrix[0][i] == True:
      continue
    minCut = cuts[i-1] + 1
    j = 0
    while j < i:
      if isPalindromeMatrix[j+1][i] == True:
        minCut = min(minCut, cuts[j] + 1)
      j += 1
    cuts[i] = minCut
  return cuts[-1]

def buildIsPalindromeMatrix(string):
  matrix = [
    [ False for _ in range(len(string)) ] for _ in range(len(string))
  ]
  for i in range(len(string)):
    for j in range(i, len(string)):
      matrix[i][j] = isPalindrome(string[i:j+1])
  return matrix

def buildIsPalindromeMatrix2(string):
  matrix = [
    [ False for _ in range(len(string)) ] for _ in range(len(string))
  ]
  for i in range(len(string)):
    matrix[i][i] = True
  for length in range(2, len(string) + 1):
    for i in range(len(string) - length + 1):
      j = i + length - 1
      if length == 2:
        matrix[i][j] = string[i] == string[j]
      else:
        matrix[i][j] = string[i] == string[j] and matrix[i+1][j-1]
  return matrix


def isPalindrome(string):
  return string == string[::-1]

palindromePartitioningMinCuts("noonabbad")