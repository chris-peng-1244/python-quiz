cache = {}

def is_palindrome(s):
    return s == s[::-1]

def make_palindrome(s):
    if s in cache:
        return cache[s]

    if is_palindrome(s):
        cache[s] = s
        return s
    
    if s[0] == s[1]:
        result = s[0] + make_palindrome(s[1:-1]) + s[-1]
        cache[s] = result
        return result
    else:
        one = s[0] + make_palindrome(s[1:]) + s[0]
        two = s[-1] + make_palindrome(s[:-1]) + s[-1]
        cache[s] = min(one, two)
        return min(one, two)

def make_palindrome2(s):
    if len(s) <= 1:
        return s
    table = [['' for i in range(len(s) + 1)] for j in range(len(s)+1)]

    for i in range(len(s)):
        table[i][1] = s[i]

    for j in range(2, len(s) + 1):
        for i in range(len(s) - j + 1):
            term = s[i:i + j]
            first, last = term[0], term[-1]
            if first == last:
                table[i][j] = first + table[i + 1][j - 2] + last
            else:
                one = first + table[i + 1][j - 1] + first
                two = last + table[i][j-1] + last
                if len(one) < len(two):
                    table[i][j] = one
                elif len(one) > len(two):
                    table[i][i] = two
                else:
                    table[i][j] = min(one, two)

    return table[0][-1]