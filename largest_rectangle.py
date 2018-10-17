def largest_rectangle_brute(matrix):
    n, m = len(matrix), len(matrix[0])
    max_so_far = 0
    for top_left_row in range(n):
        for top_left_col in range(m):
            for bottom_right_row in range(n, top_left_row, -1):
                for bottom_right_col in range(m, top_left_col, -1):
                    if is_valid(matrix,
                        top_left_row,
                        top_left_col,
                        bottom_right_row,
                        bottom_right_col):
                        max_so_far = max(max_so_far, area(
                            top_left_row,
                            top_left_col,
                            bottom_right_row,
                            bottom_right_col
                        ))
    return max_so_far


def is_valid(matrix, top_left_row, top_left_col, bottom_right_row, bottom_right_col):
    for i in range(top_left_row, bottom_right_row):
        for j in range(top_left_col, bottom_right_col):
            if matrix[i][j] == 0:
                return False
    return True


def area(top_left_row, top_left_col, bottom_right_row, bottom_right_col):
    return (bottom_right_row - top_left_row) * (bottom_right_col - top_left_col)


def largest_rectangle(matrix):
    m = len(matrix[0])
    max_so_far = 0

    cache = [0 for _ in range(m)]
    for row in matrix:
        for i, val in enumerate(row):
            if val == 0:
                cache[i] = 0
            elif val == 1:
                cache[i] += 1
        max_so_far = max(max_so_far, infer_area(cache))

    return max_so_far

def infer_area(cache):
    max_area = 0
    for i in range(len(cache)):
        for j in range(i + 1, len(cache) + 1):
            current_rectangle = min(cache[i:j]) * (j - i)
            max_area = max(max_area, current_rectangle)
    return max_area