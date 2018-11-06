def first_recurring(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

def first_recurring_bitwise(str):
    checker = 0
    for c in str:
        val = ord(c) - ord('a')
        if (checker & (1 << val)) > 0:
            return c
        checker |= (1 << val)

    return None