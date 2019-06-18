def boggle_board(board, words):
  trie = SuffixTrie(words)

  visited_matrix = [
    [False for _ in board[0]] for _ in board
  ]

  final_words = set()
  for row in range(len(board)):
    for col in range(len(board[0])):
      dfs(board, visited_matrix, row, col, trie.root, final_words)
  return final_words

class SuffixTrie:
  def __init__(self, words):
    self.root = {}
    for word in words:
      self.add(word)

  def add(self, word):
    current_node = self.root
    for char in word:
      if char not in current_node:
        current_node[char] = {}
      current_node = current_node[char]
    current_node['*'] = word

def dfs(board, visited, row, col, node, final_words):
  if visited[row][col]:
    return
  char = board[row][col]
  if char not in node:
    return

  visited[row][col] = True
  node = node[char]
  if '*' in node:
    final_words.add(node['*'])

  neighbours = get_board_neighboards(board, row, col)
  for nrow, ncol in neighbours:
    dfs(board, visited, nrow, ncol, node, final_words)
  visited[row][col] = False


def get_board_neighboards(board, row, col):
  potential_neighbors = [
    (row-1, col-1),
    (row-1, col),
    (row-1, col+1),
    (row, col-1),
    (row, col+1),
    (row+1, col-1),
    (row+1, col),
    (row+1, col+1)
  ]
  return list(filter(lambda neighbour: is_inside_board(board, neighbour[0], neighbour[1]), potential_neighbors))

def is_inside_board(board, row, col):
  return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])

board = [
  ["y", "g", "f", "y", "e", "i"],
  ["c", "o", "r", "p", "o", "u"],
  ["j", "u", "z", "s", "e", "l"],
  ["s", "y", "u", "r", "h", "p"],
  ["e", "a", "e", "g", "n", "d"],
  ["h", "e", "l", "s", "a", "t"],
]

print(boggle_board(board, ["san", "sana", "at", "vomit", "yours"]))
