def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
  # ancestors_one = getAncestors(descendantOne, topAncestor)
  # ancestors_two = getAncestors(descendantTwo, topAncestor)
  # return findCommonAncestor(ancestors_one, ancestors_two)
  depth_one = getDepth(descendantOne, topAncestor)
  depth_two = getDepth(descendantTwo, topAncestor)
  if depth_one > depth_two:
    descendantOne = ascend(descendantOne, depth_one - depth_two)
  elif depth_one < depth_two:
    descendantTwo = ascend(descendantTwo, depth_two - depth_one)
  return getCommonAncestor(descendantOne, descendantTwo).value

def getDepth(node, topAncestor):
  depth = 0
  while node != topAncestor:
    depth += 1
    node = node.ancestor
  return depth

def ascend(node, depth):
  while depth > 0:
    node = node.ancestor
    depth -= 1
  return node

def getCommonAncestor(node1, node2):
  while node1 != node2:
    node1 = node1.ancestor
    node2 = node2.ancestor
  return node1

def getAncestors(node, topAncestor):
  ancestors = [node]
  while node.ancestor and node.ancestor != topAncestor:
    ancestors.append(node.ancestor)
    node = node.ancestor
  if node != topAncestor:
    ancestors.append(topAncestor)
  return ancestors

def findCommonAncestor(list1, list2):
  rlist1 = list(reversed(list1))
  rlist2 = list(reversed(list2))
  for i in range(len(rlist1)):
    if i >= len(rlist2):
      break
    if rlist1[i] == rlist2[i]:
      commonAncestor = rlist1[i]
    else:
      break
  return commonAncestor.value


class Node:
  def __init__(self, value, ancestor=None):
    self.value = value
    self.ancestor = ancestor

nodeA = Node('A')
nodeB = Node('B', nodeA)
nodeC = Node('C', nodeA)
nodeD = Node('D', nodeB)
nodeE = Node('E', nodeB)
nodeF = Node('F', nodeC)
nodeG = Node('G', nodeC)
nodeH = Node('H', nodeD)
nodeI = Node('I', nodeD)

print(getYoungestCommonAncestor(nodeA, nodeA, nodeI))