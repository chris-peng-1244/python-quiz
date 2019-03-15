def getNthFib(n):
    fibs = [0, 1]
    if n <= 2:
        return fibs[n-1]
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[n-1]