def levenshtainDistance(str1, str2):
    matrix = [[i for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]

    for i in range(len(str2) + 1):
        matrix[i][0] = i

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if str2[i-1] == str1[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i-1][j-1],
                                       matrix[i-1][j], matrix[i][j-1])
    return matrix[-1][-1]

# print(levenshtainDistance("abc", "abx"))
print(levenshtainDistance("abc", "abcx"))
