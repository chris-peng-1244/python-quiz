def take_steps(n: int, allowed_steps: tuple = (1, 2)) -> int:
    steps = list()
    steps.append(1)
    steps.append(1)

    if n <= 1:
        return steps[n]

    allowed_steps_length = len(allowed_steps)
    for i in range(2, n+1):
        step = 0
        for j in range(allowed_steps_length):
            if i - allowed_steps[j] >= 0:
                step += steps[i - allowed_steps[j]]
        steps.append(step)

    return steps[n]


def staircase(n: int, X: tuple)->int:
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]


print(take_steps(4))
print(take_steps(1))
print(take_steps(8, (1, 3, 5)))
print(staircase(100, (1, 7, 11)))
