class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value > value:
      if self.left is None:
        self.left = BST(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BST(value)
      else:
        self.right.insert(value)
    return self

  def remove(self, value, parent=None):
    if self.value > value:
      if self.left:
        return self.left.remove(value, self)
    elif self.value < value:
      if self.right:
        return self.right.remove(value, self)
    else:
      if self.left and self.right:
        minVal = self.right.findMin()
        self.value = minVal
        self.right.remove(minVal, self)
      elif parent is None:
        if self.left is not None:
          self.value = self.left.value
          self.right = self.left.right
          self.left = self.left.left
        else:
          self.value = self.right.value
          self.left = self.right.left
          self.right = self.right.right
      elif parent.left == self:
        parent.left = self.left if self.left else self.right
      elif parent.right == self:
        parent.right = self.left if self.left else self.right
    return self

  def findMin(self):
    if self.left is None:
      return self.value
    return self.left.findMin()

  def contains(self, value):
    if self.value == value:
      return True
    if self.value > value:
      if self.left is None:
        return False
      else:
        return self.left.contains(value)
    else:
      if self.right is None:
        return False
      else:
        return self.right.contains(value)

# bst1 = BST(10).insert(5).insert(15).insert(22) \
#     .insert(17).insert(34).insert(7).insert(2).insert(5) \
#     .insert(1).insert(35).insert(27).insert(16) \
#     .insert(30).remove(22).remove(17)

# bst2 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)
# print(bst2.left.right.value)

bs3 = BST(10).insert(5).insert(7).insert(2).remove(10)
def traverse(bst):
  if bst is not None:
    traverse(bst.left)
    print(bst.value)
    traverse(bst.right)


traverse(bs3)