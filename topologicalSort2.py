def topologicalSort(jobs, deps):
  tree = buildTree(jobs, deps)
  result = []

  while tree.nodes:
    treeNode = tree.nodes.pop()
    containsCycle = dfs(treeNode, result)
    if containsCycle:
      return []
  return result

def dfs(node, result):
  if node.visited:
    return False
  if node.visiting:
    return True

  node.visiting = True
  for neighbour in node.neighbours:
    if dfs(neighbour, result):
      return True
  result.append(node.job)
  node.visited = True
  node.visiting = False
  return False

def buildTree(jobs, deps):
  tree = Tree(jobs)
  for job, dep in deps:
    tree.addDep(job, dep)
  return tree

class TreeNode:
  def __init__(self, job):
    self.job = job
    self.visited = False
    self.visiting = False
    self.neighbours = []

class Tree:
  def __init__(self, jobs):
    self.nodes = []
    self.nodeMap = {}
    for job in jobs:
      self.addNode(job)

  def addNode(self, job):
    node = TreeNode(job)
    self.nodes.append(node)
    self.nodeMap[job] = node

  def addDep(self, job, dep):
    node = self.nodeMap[dep]
    node.neighbours.append(self.nodeMap[job])

print(topologicalSort([1,2,3,4], [[1,2],[1,3],[3,2],[4,2],[4,3]]))
print(topologicalSort([1,2,3,4], [[1,2],[1,3],[3,2],[4,2],[4,3], [2,3]]))
