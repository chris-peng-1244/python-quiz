def is_palindrome(word):
    return word == word[::-1]

def palindrome_pairs_naive(words):
    result = []
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                result.append((i, j))
    return result

def palindrome_pairs(words):
    d = {}
    for i, word in enumerate(words):
        d[word] = i

    result = []

    for i, word in enumerate(words):
        for char_i in range(len(word)):
            prefix, postfix = word[:char_i], word[char_i:]
            reversed_prefix, reversed_postfix = prefix[::-1], postfix[::-1]

            if is_palindrome(postfix) and reversed_prefix in d:
                if i != d[reversed_prefix]:
                    result.append((i, d[reversed_prefix]))
            
            if is_palindrome(prefix) and reversed_postfix in d:
                if i != d[reversed_postfix]:
                    result.append((d[reversed_postfix], i))

    return result