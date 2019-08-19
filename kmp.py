def knuthMorrisPrattAlgorithm(string, substring):
  substring_pattern = find_substring_pattern(substring)
  j = 0
  for i in range(len(string)):
    if j == len(substring):
      return True
    if string[i] == substring[j]:
      j += 1
    elif j > 0:
      previous = substring_pattern[j - 1]
      if previous > -1 and string[i] == substring[previous + 1]:
        j = previous + 2
      elif string[i] == substring[0]:
        j = 1
      else:
        j = 0
  return j == len(substring)

def find_substring_pattern(string):
  pattern = [ -1 for _ in string ]
  j = 0

  for i in range(1, len(string)):
    if string[i] == string[j]:
      pattern[i] = j
      j += 1
    elif j > 0:
      if pattern[j-1] > -1:
        if string[pattern[j-1]+1] == string[i]:
          j = pattern[j - 1] + 1
          pattern[i] = j
          j += 1
      else:
        j = 0
  return pattern


print(knuthMorrisPrattAlgorithm("aefaefaefaedaefaedaefaefa", "aefaedaefaefa"))
print(knuthMorrisPrattAlgorithm("aefcdfaecdaefaefcdaefeaefcdcdeae", "aefcdaefeaefcd"))