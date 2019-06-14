def topologicalSort(jobs, deps):
  tree = buildTree(jobs, deps)
  ordered_jobs = []

  dep_num_map = getDepNumMap(tree)

  zero_dep_jobs = get_zero_dep_jobs(dep_num_map)
  while zero_dep_jobs:
    for zero_dep_job in zero_dep_jobs:
      ordered_jobs.append(zero_dep_job)
      for job in tree[zero_dep_job]:
        dep_num_map[job] -= 1
      tree.pop(zero_dep_job, None)
      dep_num_map.pop(zero_dep_job, None)
    zero_dep_jobs = get_zero_dep_jobs(dep_num_map)

  if tree and not zero_dep_jobs:
    return []
  return ordered_jobs

def get_zero_dep_jobs(dep_num_map):
  zero_dep_jobs = []
  for job, job_dep in dep_num_map.items():
    if job_dep == 0:
      zero_dep_jobs.append(job)
  return zero_dep_jobs

def buildTree(jobs: list, deps: list):
  tree = {}
  for job in jobs:
    tree[job] = []
  for job, dep in deps:
    tree[job].append(dep)
  return tree

def getDepNumMap(tree: dict):
  depNumMap = {}
  for vertext in tree:
    depNumMap[vertext] = 0

  for edges in tree.values():
    for edge in edges:
      depNumMap[edge] += 1
  return depNumMap

print(topologicalSort([1,2,3,4], [[1,2],[1,3],[3,2],[4,2],[4,3],[2,3]]))
print(topologicalSort([1,2,3,4], [[1,2],[1,3],[3,2],[4,2],[4,3]]))