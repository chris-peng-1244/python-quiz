from collections import defaultdict
import heapq

def top_pairs(log, k):
    visitors = defaultdict(set)
    for site, user in log:
        visitors[site].add(user)

    pairs = []
    sites = list(visitors.keys())

    for _ in range(k):
        heapq.heappush(pairs, (0, ('', '')))

    for i in range(len(sites) - 1):
        for j in range(i + 1, len(sites)):
            score = compute_similarity(sites[i], sites[j], visitors)
            heapq.heappushpop(pairs, (score, (sites[i], sites[j])))

    return [pair[1] for pair in pairs]

def compute_similarity(a, b, visitors):
    return len(visitors[a] & visitors[b]) / len(visitors[a] | visitors[b])

lst = [('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e', 5), ('e', 6)]

print(top_pairs(lst, 1))

