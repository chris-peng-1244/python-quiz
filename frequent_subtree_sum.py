from collections import Counter

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def frequent_subtree_sum(root):
  if root is None:
    return None

  c = Counter()

  def get_subtree_sum(node):
    if node is None:
      return 0
    s = node.val + get_subtree_sum(node.left) + get_subtree_sum(node.right)
    c[s] += 1
    return s
  
  get_subtree_sum(root)
  return c.most_common(1)[0]