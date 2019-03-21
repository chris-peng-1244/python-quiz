def minNumberOfCoinsForChange(n, denoms):
    minNumber = [float("inf") for i in range(n+1)]
    minNumber[0] = 0
    for denom in denoms:
        for i in range(1, n+1):
            if i >= denom:
                minNumber[i] = min(minNumber[i], 1 + minNumber[i - denom])
    return minNumber[-1] if minNumber[-1] != float("inf") else -1

print(minNumberOfCoinsForChange(9, [3, 5]))