def wordBreak(s, wordDict):
  canBeBreak = [ True ]
  for _ in s:
    canBeBreak.append(False)

  for i in range(len(s)):
    for word in wordDict:
      if canBreakWithWord(s, word, i + 1, canBeBreak):
        canBeBreak[i+1] = True
        break

  return canBeBreak[-1]

def canBreakWithWord(s, word, subStrLen, canBeBreak):
  if len(word) > subStrLen:
    return False
  endWord = s[subStrLen-len(word):subStrLen]
  if endWord == word and canBeBreak[subStrLen - len(word)]:
    return True
  return False

wordBreak("leetcode", ["leet", "code"])