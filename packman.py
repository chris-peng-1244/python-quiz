def collect_coins(matrix, r = 0, c = 0, cache=None):
    if cache is None:
        cache = {}

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    is_bottom = r == num_rows - 1
    is_rightmost = c == num_cols - 1

    if (r, c) not in cache:
        if is_bottom and is_rightmost:
            cache[r, c] = matrix[r][c]
        elif is_bottom:
            cache[r, c] = matrix[r][c] + collect_coins(matrix, r, c + 1, cache)
        elif is_rightmost:
            cache[r, c] = matrix[r][c] + collect_coins(matrix, r + 1, c, cache)
        else:
            cache[r, c] = matrix[r][c] + max(collect_coins(matrix, r + 1, c, cache), collect_coins(matrix, r, c + 1, cache))

    return cache[r, c]

print(collect_coins([
    [0, 3, 1, 1],
    [2, 0, 0, 4],
    [1, 5, 3, 1],
]))