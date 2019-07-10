def iterativeInOrderTraversal(tree, callback):
  current = tree
  previous = None
  while current:
    if previous and (previous is current.left):
      callback(tree)
      previous = current
      current = current.right if current.right else current.parent
    elif previous and (previous is current.right):
      previous = current
      current = current.parent
    elif current.left:
      previous = current
      current = current.left
    else:
      callback(tree)
      if current.right:
        previous = current
        current = current.right
      else:
        previous, current = current, previous


class BinaryTreeNode:
  def __init__(self, value, parent = None, left = None, right = None):
    self.value = value
    self.parent = parent
    self.left = left
    self.right = right