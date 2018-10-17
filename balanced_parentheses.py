def balanced(s, count=0):
    if not s and count == 0:
        return True

    c = count
    for i, char in enumerate(s):
        if char == '(':
            c += 1
        elif char == ')':
            c -= 1
        elif char == '*':
            return balanced(s[i+1:], c) or balanced(s[i+1:], c + 1) or balanced(s[i+1:], c - 1)

        if c < 0:
            return False

    return c == 0

def balanced_faster(s):
    low = 0
    high = 0
    for char in s:
        if char == '(':
            low += 1
            high += 1
        elif char == ')':
            low = max(low - 1, 0)
            high -= 1
        elif char == '*':
            low = max(low - 1, 0)
            high += 1
        
        if high < 0:
            return False
    return low == 0