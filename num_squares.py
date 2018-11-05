from math import inf

def num_squares_naive(n):
    if n == 0:
        return 0
    
    min_num_squares = inf

    i = 1
    while n - i * i >= 0:
        min_num_squares = min(min_num_squares, num_squares_naive(n - i*i) + 1)
        i += 1

    return min_num_squares

def num_squares(n):
    if n == 0:
        return 0

    cache = [inf for i in range(n+1)]
    cache[0] = 0
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            cache[i] = min(cache[i], cache[i - j*j] + 1)
            j += 1

    return cache[n]

num_squares_naive(27)