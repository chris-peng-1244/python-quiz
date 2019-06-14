class SuffixTrie:
  def __init__(self, string):
    self.root = {}
    self.endSymbol = "*"
    self.populateSuffixTrieFrom(string)

  def populateSuffixTrieFrom(self, string):
    for i in range(len(string)):
      node = self.root
      for j in range(i, len(string)):
        s = string[j]
        if s not in node:
          node[s] = {}
        node = node[s]
      node[self.endSymbol] = True

st = SuffixTrie("babc")
