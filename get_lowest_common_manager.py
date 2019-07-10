def getLowestCommonManager(topManager, reportOne, reportTwo):
  results = []
  countReportNum(topManager, reportOne, reportTwo, results)
  return results[0].value if results else None

def countReportNum(manager, reportOne, reportTwo, results):
  count = 0
  if manager == reportOne or manager == reportTwo:
    count = 1

  for report in manager.reports:
    count += countReportNum(report, reportOne, reportTwo, results)
  if count == 2:
    results.append(manager)
  return count

class Node:
  def __init__(self, value, reports=[]):
    self.value = value
    self.reports = reports

nodeO = Node('O')
nodeP = Node('P', [Node('T'), Node('U')])
nodeQ = Node('Q')
nodeH = Node('H', [nodeO, nodeP, nodeQ])
nodeG = Node('G')
nodeI = Node('I')
nodeB = Node('B', [nodeG, nodeH, nodeI])
nodeC = Node('C', [Node('J')])
nodeA = Node('A', [nodeB, nodeC])

print(getLowestCommonManager(nodeA, nodeI, nodeP))
