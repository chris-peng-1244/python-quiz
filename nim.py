def update(heaps, pile, items):
    heaps = list(heaps)
    heaps[pile] -= items
    return tuple(heaps)

def get_moves(heaps):
    moves = []

    for pile, count in enumerate(heaps):
        for i in range(1, count + 1):
            moves.append(update(heaps, pile, i))

    return set(moves)

def nim(heaps, results = {}):
    # if heaps == (0, 0, 0,):
    #     return True
    
    # moves = get_moves(heaps)

    # return any([not nim(move) for move in moves])
    if tuple(heaps) in results:
        return results[tuple(heaps)]

    if heaps == (0, 0, 0):
        return 1

    moves = get_moves(heaps)
    results[tuple(heaps)] = max([1 - nim(move) for move in moves])

    return results[tuple(heaps)]