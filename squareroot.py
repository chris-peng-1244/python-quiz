def squareoort(n, error=0.00001):
    lo = 0.0
    hi = n
    guess = (lo + hi) / 2.0

    while abs(guess ** 2 - n) >= error:
        if guess ** 2 > n:
            hi = guess
        else:
            lo = guess
        guess = (lo + hi) / 2.0

    return guess