import heapq


def create_skyline(buildings):
    buildings += [(r, r, 0) for (_, r, _) in buildings]
    buildings.sort(key=lambda x: (x[0], -x[2]))

    skyline = []
    heap = [(0, float("inf"))]

    for left, right, height in buildings:
        while heap and left >= heap[0][1]:
            heapq.heappop(heap)

        heapq.heappush(heap, (-height, right))

        if not skyline or skyline[-1][1] != -heap[0][0]:
            skyline.append((left, -heap[0][0]))

    return skyline


create_skyline([(0, 15, 3), (4, 11, 5), (19, 23, 4)])
