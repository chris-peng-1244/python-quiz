import re

def reverse(string, delimiters):
    # Parse the string into words between delimiters using regex
    # Keep adjacent delimiters together ("greedy match")
    words = re.split('[' + delimiters + ']+', string)
    if len(words) > 0 and words[-1] == '':
        words = words[:-1]
    
    # Reverse the list of words and convert to an iterator
    word_iter = reversed(words)

    output = []
    delimiter_found = True
    # Iterate through the original string
    for c in string:
        if c in delimiters:
            # When we reach a delimiter, then set the word length to 0
            delimiter_found = True
            output.append(c)
        else:
            # We've reached a non-delimiter character
            # If it's the first character of the word, add a word
            # from our reversed list of words(word_iter).
            if delimiter_found:
                try:
                    output.append(next(word_iter))
                except StopIteration:
                    pass
            delimiter_found = False

    return ''.join(output)


def reverse2(string, delimiters):
    # Parse the string into words between delimiters using regex
    # Keep adjacent delimiters together ("greed match")
    words = re.split('[' + delimiters + ']+', string)
    not_words = re.split('[^(' + delimiters + ')]+', string)
    if len(words) > 0 and words[-1] == '':
        words = words[:-1]

    # Reverse the list of words and convert to an iterator
    word_iter = reversed(words)

    output = []
    for d in not_words:
        output.append(d)
        try:
            output.append(next(word_iter))
        except StopIteration:
            pass
    
    return ''.join(output)


print(reverse('hello/world:here', '/:'))
print(reverse('hello/world:here/', '/:'))
print(reverse2('hello/world:here', '/:'))
print(reverse2('hello/world:here/', '/:'))