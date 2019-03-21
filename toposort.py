def helper(v, visited, stack, edges):
    visited[v] = True

    for neighbor, _ in edges[v]:
        if not visited[neighbor]:
            helper(neighbor, visited, stack, edges)

    stack.append(v)

def toposort(edges, num_vertices):
    visited = [False for _ in range(num_vertices)]
    stack = []

    for v in range(num_vertices):
        if not visited[v]:
            helper(v, visited, stack, edges)

    return stack

def get_distances(edges, stack):
    dist = [float('inf') for _ in range(len(stack))]
    dist[0] = 0

    while stack:
        curr = stack.pop()

        for neighbor, distance in edges[curr]:
            if dist[neighbor] > dist[curr] + distance:
                dist[neighbor] = dist[curr] + distance

    return dist[1:]

def shortest_route(elevations, paths):
    uphill_edges = defaultdict(list)
    downhill_edges = defaultdict(list)
    all_edges = defaultdict(list)

    for (start, end), distance in path.items():
        all_edges[start].append((end, distance))
        if elevations[start] < elevations[end]:
            uphill_edges[start].append((end, distance))
        else:
            downhill_edges[end].append((start, distance))

    num_vertices = len(all_edges.keys())
    stack = toposort(all_edges, num_vertices)

    uphill_distances = get_distances(uphill_edges, list(stack))
    downhill_distances = get_distances(downhill_edges, list(stack))

    return min(x + y for x, y in zip(uphill_distances, downhill_distances))

