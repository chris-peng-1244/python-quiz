def floodfill(matrix, coord, color, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(coord)

    r, c = coord
    prior_color = matrix[r][c]
    matrix[r][c] = color

    coords = [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]

    for new_coord in coords:
        new_r, new_c = new_coord
        if (new_coord not in visited
        and in_matrix(matrix, new_coord)
        and matrix[new_r][new_c] == prior_color):
            visited.add(new_coord)
            floodfill(matrix, new_coord, color, visited)

def in_matrix(matrix, coord):
    rows = len(matrix)
    cols = len(matrix[0])

    r, c = coord
    return 0 <= r < rows and 0 <= c < cols

matrix = [
        ['B', 'B', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['B', 'B', 'B'],
    ]
floodfill(
    matrix,
    (2, 2),
    'G'
)

print(matrix)