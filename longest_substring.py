def longest_substring(string):
  last_seen = {}
  longest_substring_start_index = 0
  longest_string = ""
  curr_longest_string = ""
  for i in range(len(string)):
    curr_char = string[i]
    if curr_char in last_seen:
      if (i - longest_substring_start_index) > len(longest_string):
        longest_string = string[longest_substring_start_index:i]
      longest_substring_start_index = max(
        longest_substring_start_index, 
        last_seen[curr_char] + 1) 
      curr_longest_string = string[longest_substring_start_index:i+1]
    else:
      curr_longest_string += curr_char
    last_seen[curr_char] = i
  if len(curr_longest_string) > len(longest_string):
    return curr_longest_string
  return longest_string

print(longest_substring("clementisacap"))
print(longest_substring("abcdabcef"))