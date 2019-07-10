def multiStringSearch(bigString, smallStrings):
  tries = buildTries(smallStrings)
  result = dict(zip(smallStrings, [ False for _ in smallStrings ]))

  current = tries
  for char in bigString:
    if char in current:
      current = current[char]
      if '*' in current:
        result[current['*']] = True
    else:
      current = tries
  return result.values()

def buildTries(strings):
  root = current = {}

  for string in strings:
    for char in string:
      if char not in current:
        current[char] = {}
      current = current[char]
    current['*'] = string
    current = root

  return root

print(multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]))
print(multiStringSearch("abcb akfkw afnmc fkadn vkaca jadf dacb cdba cbda", ["abcd", "acbd", "adbc", "dabc", "cbda", "cabd", "cdab"]))
print(multiStringSearch("Mary goes to the shopping center every week.", ["to", "Mary", "centers", "shop", "shopping", "string", "kappa"]))
