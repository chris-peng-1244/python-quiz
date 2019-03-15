def visit(graph, u, v, depth, reach, appeared, bridges):
  appeared[v] = reach[v] = depth

  for neighbor in graph[v]:
    if appeared[neighbor] == -1:
      visit(graph, v, neighbor, depth + 1, reach, appeared, bridges)

      if reach[neighbor] == appeared[neighbor]:
        bridges.append((v, neighbor))
      
      reach[v] = min(reach[v], reach[neighbor])

    elif neighbor != u:
      reach[v] = min(reach[v], appeared[neighbor])
      

def find_bridges(graph):
  reach = { v: -1 for v in graph }
  appeared = { v: -1 for v in graph }

  start = list(graph.keys())[0]
  depth = 0
  bridges = []

  visit(graph, start, start, depth, reach, appeared, bridges)
  return bridges