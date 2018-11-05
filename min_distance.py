def min_distance(text, word0, word1):
    text_words = [w.strip() for w in text.split(' ')]
    print(text_words)

    word0_indices = [i for i, w in enumerate(text_words) if w == word0]
    word1_indices = [i for i, w in enumerate(text_words) if w == word1]

    if not word0_indices or not word1_indices:
        return float('inf')

    i = j = 0

    min_distance = abs(word0_indices[i] - word1_indices[j])

    while i < len(word0_indices) and j < len(word1_indices):
        current_distance = abs(word0_indices[i] - word1_indices[j])
        min_distance = min(min_distance, current_distance)

        if word0_indices[i] < word1_indices[j]:
            i += 1
        else:
            j += 1
        return min_distance - 1

min_distance("dog cat hello cat dog dog hello cat world", "hello", "world")