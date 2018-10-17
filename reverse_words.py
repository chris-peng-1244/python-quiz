def reverse_words(string_list):
    # Helper function to reverse string in place
    def reverse(l, start, end):
        # Reverses characters from index start to end (inclusive)
        while start < end:
            l[start], l[end] = l[end], l[start]
            start += 1
            end -= 1

    # Reverse the entire string
    reverse(string_list, 0, len(string_list) - 1)

    # Reverse each word in the string
    start = 0
    for end in range(len(string_list)):

        if string_list[end] == ' ':
            print(start, end)
            reverse(string_list, start, end - 1)
            start = end + 1

    # Reverse the last word
    reverse(string_list, start, len(string_list) - 1)

    return string_list

print(reverse_words("Hello world python"))