def gray_code(n):
    if n == 0:
        return []
    elif n == 1:
        return [0, 1]

    prev_gray_code = gray_code(n - 1)

    result = []
    for code in prev_gray_code:
        result.append(code)

    for code in reversed(prev_gray_code):
        result.append((1 << n - 1) + code)

    return result

print(gray_code(2))
print(gray_code(3))