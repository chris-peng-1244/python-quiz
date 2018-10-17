def covering(intervals):
    intervals.sort(key=lambda x: x[0])

    result = []
    i = 0

    while i < len(intervals):
        interval = intervals[i]

        while i < len(intervals) and intersecting(intervals[i], interval):
            interval = (max(intervals[i][0], interval[0]), min(intervals[i][1], interval[1]))
            i += 1

        result.append(interval[1])
    return result


def intersecting(x, y):
    return not (x[0] > y[1] or y[0] > x[1])


print(covering([(0,3), (2,6), (3,4), (6,9)]))