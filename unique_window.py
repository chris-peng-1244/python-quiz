from collections import defaultdict

def unique_window(string):
  string = list(string)

  char_seen = 0
  char_total = len(set(string))
  char_counts = defaultdict(int)

  start = 0
  result = float("inf")

  for end, char in enumerate(string):
    char_counts[char] += 1
    if char_counts[char] == 1:
      char_seen += 1

    if char_seen == char_total:
      while char_counts[string[start]] > 1:
        char_counts[string[start]] -= 1
        start += 1
      
      window_length = end - start + 1
      if window_length < result:
        result = window_length
  
  return result

unique_window("jiujiustu")