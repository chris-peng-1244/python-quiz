def longest_common_subsequence(str1, str2):
  matrix = initLCSMatrix(str1, str2)
  for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
          diagnal = matrix[i][j]
          matrix[i+1][j+1] = diagnal + str1[i]
        else:
          left = matrix[i+1][j]
          upper = matrix[i][j+1]
          matrix[i+1][j+1] = left if len(left) > len(upper) else upper
  
  return list(matrix[-1][-1])


def initLCSMatrix(str1, str2):
  matrix = [
    ["" for _ in range(len(str2)+1)] for _ in range(len(str1)+1)
  ]
  return matrix

def longest_common_subsequence_faster(str1, str2):
  lengthMatrix = initLengthMatrix(str1, str2)
  for row in range(1, len(lengthMatrix)):
    for col in range(1, len(lengthMatrix[0])):
      if str1[row-1] == str2[col-1]:
        lengthMatrix[row][col] = lengthMatrix[row-1][col-1] + 1
      else:
        lengthMatrix[row][col] = max(lengthMatrix[row-1][col], lengthMatrix[row][col-1])

  return buildLCS(lengthMatrix, str1, str2)

def initLengthMatrix(str1, str2):
  return [
    [0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)
  ]

def buildLCS(matrix, str1, str2):
  row = len(matrix)-1
  col = len(matrix[0])-1

  reversedLCS = []
  while row > 0 and col > 0:
    if matrix[row][col] == matrix[row-1][col]:
      row -= 1
    elif matrix[row][col] == matrix[row][col-1]:
      col -= 1
    else:
      reversedLCS.append(str1[row-1])
      row -= 1
      col -= 1
  return list(reversed(reversedLCS))

print(longest_common_subsequence_faster("zxvvyzw", "xkykzpw"))
