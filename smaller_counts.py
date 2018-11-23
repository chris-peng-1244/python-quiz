import bisect

def smaller_counts(lst):
    results = []
    s = []
    for num in reversed(lst):
        i = bisect.bisect_left(s, num)
        results.append(i)
        bisect.insort(s, num)

    return list(reversed(results))

smaller_counts([3, 4, 9, 6, 1])