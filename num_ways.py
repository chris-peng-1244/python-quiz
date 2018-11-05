EMPTY = 0
WALL = 1

def num_ways(matrix):
    m, n = len(matrix), len(matrix[0])
    num_ways_matrix = [[0 for j in range(n)] for i in range(m)]

    # Fill first row
    for j in range(n):
        if matrix[0][j] == WALL:
            break
        num_ways_matrix[0][j] = 1

    #Fill first col
    for i in range(m):
        if matrix[i][0] == WALL:
            break
        num_ways_matrix[i][0] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            from_top = num_ways_matrix[i-1][j] if matrix[i-1][j] != WALL else 0
            from_left = num_ways_matrix[i][j-1] if matrix[i][j-1] != WALL else 0

            num_ways_matrix[i][j] = from_top + from_left

    return num_ways_matrix[m-1][n-1]

print(num_ways([
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0]
]))