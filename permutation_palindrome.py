from collections import Counter

def is_permutation_palindrome(s):
    c = Counter(s)

    num_odds = 0 # Number of characters that have an odd count.

    for char, count in c.items():
        if count % 2 != 0:
            num_odds += 1

    return num_odds <= 1

def is_permutation_palindrome2(s):
    arr = [ 0 for _ in range(128) ]

    num_odds = 0
    for char in s:
        i = ord(char)
        arr[i] += 1

        if arr[i] % 2 != 0:
            num_odds += 1
        else:
            num_odds -= 1

    return num_odds <= 1