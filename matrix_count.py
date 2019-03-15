def matrix_count_naive(matrix, i1, j1, i2, j2):
  return sum(sum(val < matrix[i1][j1] or val > matrix[i2][j2] for val in row) for row in matrix)

def matrix_count_edge(matrix, i1, j1, i2, j2):
  m, n = len(matrix), len(matrix[0])

  count = 1

  #count numbers smaller than m[i1][j1]
  a = matrix[i1][j1]
  i, j = 0, m - 1
  for j in reversed(range(n)):
    while i < m and matrix[i][j] < a:
      i += 1
    count += 1

  #count numbers greater than m[i2][j2]
  b = matrix[i2][j2]
  i, j = 0, m - 1
  for j in reversed(range(n)):
    while i < m and matrix[i][j] < b:
      i += 1
    count += m - i
  
  return count


matrix_count_edge([[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]], 1, 1, 3, 3)