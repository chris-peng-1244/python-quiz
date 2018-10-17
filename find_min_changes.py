DENOMINATIONS = [1, 5, 10, 25]

def minimum_coins(n):
    if n == 0:
        return 0
    elif n in DENOMINATIONS:
        return 1
    else:
        return min(1 + minimum_coins(n - d) for d in DENOMINATIONS if n - d >= 0)

def minimum_coins_dp(n):
    cache = [0 for _ in range(n + 1)]

    for d in DENOMINATIONS:
        if d < len(cache):
            cache[d] = 1

    for i in range(1, n + 1):
        cache[i] = min(1 + cache[i - d] for d in DENOMINATIONS if i >= d)

    return cache[n]

print(minimum_coins_dp(16))