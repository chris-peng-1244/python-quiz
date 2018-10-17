def k_palindrome(s, k):
    # If s is already a palindrome, return true
    if len(s) <= 1:
        return True

    # Get rid of matching ends
    while s[0] == s[-1]:
        s = s[1:-1]
        if len(s) <= 1:
            return True

    if k == 0:
        return False

    # Try getting rid of the first and last character to see if we
    # can make a palindrome by removing k - 1 chars
    return k_palindrome(s[:-1], k - 1) or k_palindrome(s[1:], k - 1)


def k_palindrome2(s, k):
    return len(s) - longest_palindromic_subsequence(s) < k

def longest_palindromic_subsequence(s):
    if s == s[::-1]:
        return len(s)

    n = len(s)
    A = [[0 for j in range(n)] for i in range(n)]

    for i in range(n - 1, -1, -1):
        A[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                A[i][j] = 2 + A[i+1][j-1]
            else:
                A[i][j] = max(A[i+1][j], A[i][j-1])

    return A[0][n-1]


k_palindrome2("waterrfetawx", 2)