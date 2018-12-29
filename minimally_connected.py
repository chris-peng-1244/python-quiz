def minimally_connected(graph):
    n = len(graph)
    num_edges = 0
    for v, edges in graph.items():
        num_edges += len(edges)
    num_edges //= 2
    return n - 1 == num_edges