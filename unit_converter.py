from collections import defaultdict, deque

class Converter:

    def __init__(self, standard='foot'):
        self.graph = defaultdict(list)
        self.graph[standard] = [(standard, 1.0)]

    def add(self, unit, relative, multiplier):
        if relative in self.graph:
            self.graph[unit].append((relative, multiplier))
            self.graph[relative].append((unit, 1.0 / multiplier))

    def convert(self, unit):
        visited = set()
        results = { unit: 1.0 }
        queue = dequeue([ (unit, 1.0) ])

        while queue:
            curr, value = queue.popleft()
            neighbors = self.graph[curr]

            for neighbor, multiplier in neighbors:
                if neighbor not in visited:
                    results[neighbor] = value * multiplier
                    queue.append((neighbor, value * multiplier))

            visited.add(curr)
        return results
